
# REPL dependencies
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from num2words import num2words
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from titlecase import titlecase
from bs4 import BeautifulSoup
import urllib2
import csv

# CLI dependencies
import bibtexparser
from fabric.api import run, sudo, local, settings
import logging
import sys
import tabulate

# required to use as module
if __name__ == '__main__': 
	print "hello world"