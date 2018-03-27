import bibtexparser
from fabric.api import run, sudo, local, settings
from fabric.api import roles, execute
import logging
import sys
import tabulate
from prompter import prompt, yesno
from termcolor import colored
import config
import lib.util as util

logging.basicConfig()



def archive_test():
	pdfkit.from_url('https://www.google.com/', 'out.pdf')

def archive_all_citations():
	with open(config.refs_path + '/library.bib') as bibtex_file:
		bibtex_database = bibtexparser.load(bibtex_file)

	for i, entry in enumerate(bibtex_database.entries):
		if 'url' in entry:
			if not 'archive-url' in entry:
				cite_key = str(entry['ID'])
				url = str(entry['url'])
				if "dx.doi.org" in url: 
					print "\n\n{} does not need archive as it's a DOI url: \n{}".format(cite_key,url)
				else:
					cmd = "archivenow --ia \'{}\'".format(url)
					archive_url = local(cmd,capture=True)
					bibtex_database.entries[i]["archive-url"] = archive_url
					print "Archived as {} \n\n".format(archive_url)
			

	with open(config.refs_path + '/library.bib', 'w') as bibtex_file:
		bibtexparser.dump(bibtex_database, bibtex_file)


def generate_cite_md():
	with open(config.refs_path + '/library.bib') as bibtex_file:
		bibtex_database = bibtexparser.load(bibtex_file)

	for i, entry in enumerate(bibtex_database.entries):
		cite_key = str(entry['ID'])
		print "Updating {} md file....".format(cite_key),
		entry_items = [ [key,value] for key, value in entry.iteritems()]
		headers = ['Item', 'Value']
		table = tabulate.tabulate(entry_items, headers, tablefmt="pipe")
		table = str(table)
		file = open(config.refs_path + "/cite-md/" + cite_key + ".md", 'w')
		file.write(table)
		file.close()
	print "Complete"


def update_requirements():
	util.header('Updating requirements file')
	local('pip freeze -r ' + config.root_path + '/devel-req.txt > ' + config.root_path + '/requirements_local.txt')

def update():
	util.header('Archiving citations')
	execute(archive_all_citations)

	util.header('Updating requirements file')
	local('pip freeze -r ' + config.root_path + '/devel-req.txt > ' + config.root_path + '/requirements.txt')

	util.header('Updating citations md files')
	execute(generate_cite_md)

	util.header('Adding to git')
	local('git add .')
	local('git status')
	m = prompt("Commit message:", default='Autoupdate')
	# if not yesno('Continue?'):
		# return
	local('git commit -m \'' + m + "\'")
	local('git push origin master')
	print colored('............................. Done','green')


