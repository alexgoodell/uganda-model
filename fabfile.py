import bibtexparser
import pdfkit






def archive_test():
	pdfkit.from_url('https://www.google.com/', 'out.pdf')

def archive_all_citations():
	

#with open('bibtex.bib') as bibtex_file:
#   bibtex_database = bibtexparser.load(bibtex_file)