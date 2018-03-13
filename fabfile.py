import bibtexparser
import pdfkit
from fabric.api import run, sudo, local, settings
import logging
import sys
logging.basicConfig()



def archive_test():
	pdfkit.from_url('https://www.google.com/', 'out.pdf')

def archive_all_citations():


	with open('refs/library.bib') as bibtex_file:
		bibtex_database = bibtexparser.load(bibtex_file)

	for i, entry in enumerate(bibtex_database.entries):
		if 'url' in entry:
			cite_key = str(entry['ID'])
			url = str(entry['url'])
			cmd = "archivenow --ia {}".format(url)

			archive_url = local(cmd,capture=True)

			bibtex_database.entries[i]["archive-url"] = archive_url
			print "Archived as {} \n\n".format(archive_url)
			

	with open('refs/library.bib', 'w') as bibtex_file:
		bibtexparser.dump(bibtex_database, bibtex_file)

