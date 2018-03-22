import bibtexparser
from fabric.api import run, sudo, local, settings
from fabric.api import roles, execute
import logging
import sys
import tabulate
from prompter import prompt, yesno
from termcolor import colored
import config

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
				cmd = "archivenow --ia {}".format(url)

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

def update():
	m = prompt("Message:", default='Autoupdate')

	print colored('Updating requirements file............................','blue')
	local('pip freeze -r ' + config.root_path + '/devel-req.txt > ' + config.root_path + '/requirements.txt')

	print colored('Updating citations md files............................','blue')
	execute(generate_cite_md)

	print colored('Adding to git.............................','blue')
	local('git add .')
	local('git status')
	if not yesno('Continue?'):
		return
	local('git commit -m \'' + m + "\'")
	local('git push origin master')
	print colored('............................. Done','blue')

def root():
	print config.root_path

