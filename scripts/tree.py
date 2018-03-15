#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""FileTreeMaker.py: ..."""

__author__  = "legendmohe"

import os
import argparse
import time
import yaml

document = """
./data : desc
./data/gis : desc
./data/gis/Ug_District-boundaries2006 : desc
./data/ihris : desc
./data/umdpc : desc
./docs : desc
./docs/archive : desc
./misc : desc
./model : desc
./model/py : desc
./refs : desc
./refs/doc-archive : desc
./refs/misc : desc
./scripts : desc
./tmp : desc
./data/gis/Ug_District-boundaries2006/Ug_District-boundaries2006.dbf : desc
./data/gis/Ug_District-boundaries2006/Ug_District-boundaries2006.prj : desc
./data/gis/Ug_District-boundaries2006/Ug_District-boundaries2006.sbn : desc
./data/gis/Ug_District-boundaries2006/Ug_District-boundaries2006.sbx : desc
./data/gis/Ug_District-boundaries2006/Ug_District-boundaries2006.shp : desc
./data/gis/Ug_District-boundaries2006/Ug_District-boundaries2006.shp.xml : desc
./data/gis/Ug_District-boundaries2006/Ug_District-boundaries2006.shx : desc
./data/ihris/licensed-allied-health-professionals-11-3-2018.csv : desc
./data/ihris/registered-allied-health-professionals-11-3-2018.csv : desc
./data/ihris/registered-medical-and-dental-professionals-11-3-2018.csv : desc
./data/umdpc/full-register-3-13-2018.xls : desc
./data/umdpc/licenced-medical-and-dental-practitioners-3-13-2018.xls : desc
./data/umdpc/registered-health-units-3-13-2018.xls : desc
./data/umdpc/specialist-register-3-13-2018.xls : desc
./data/umdpc/temporary-registration-certificates-3-13-2018.xls : desc
./data/umdpc/ucmb-hospitals-3-13-2018.xls : desc
./data/umdpc/ummb-hospitals-3-13-2018.xls : desc
./data/umdpc/upmb-hospitals-3-13-2018.xls : desc
./docs/archive/registered-allied-professionals-11-3-2018.htm : desc
./docs/training.graffle : desc
./docs/training.jpg : desc
./misc/notes.md : desc
./model/py/index.py : desc
./model/py/latex-cite.tpl : desc
./model/py/notebook.tex : desc
./model/py/output_11_0.png : desc
./model/py/output_8_0.png : desc
./model/py/uganda-model.ipynb : desc
./model/state-info.yml : desc
./refs/misc/budgethealthsectorBFP2015.pdf : desc
./refs/misc/nursingentryreq.png : desc
./refs/misc/pensionpayments2017.pdf : desc
./refs/library (Autosaved).bib : desc
./refs/library.bib : desc
./refs/plain-bib.html : desc
./refs/plain-bib.tex : desc
./refs/style.csl : desc
./scripts/extract-table-from-html-to-csv.py : desc
./scripts/tree.py : desc
./tmp/tmp.py : desc
./fabfile.py : desc
./fabfile.pyc : desc
./ms.tex : desc
./postBuild : desc
./README.md : desc
./requirements.txt : desc
./runtime.txt : desc
./uganda-model.sublime-project : desc
./uganda-model.sublime-workspace : desc
./variables.md : desc
"""
desc = yaml.load(document)

class FileTreeMaker(object):

	def _recurse(self, parent_path, file_list, prefix, output_buf, level):
		if len(file_list) == 0 \
			or (self.max_level != -1 and self.max_level <= level):
			return
		else:
			file_list = [f for f in file_list if not f.startswith('.')]
			file_list.sort(key=lambda f: os.path.isfile(os.path.join(parent_path, f)))
			for idx, sub_path in enumerate(file_list):
				if any(exclude_name in sub_path for exclude_name in self.exn):
					continue

				full_path = os.path.join(parent_path, sub_path)
				idc = "┣━"
				if idx == len(file_list) - 1:
					idc = "┗━"

				if os.path.isdir(full_path) and sub_path not in self.exf:
					output_buf.append("%s%s%s - %s" % (prefix, idc, sub_path, desc[full_path]))
					# print full_path
					if len(file_list) > 1 and idx != len(file_list) - 1:
						tmp_prefix = prefix + "┃  "
					else:
						tmp_prefix = prefix + "    "
					self._recurse(full_path, os.listdir(full_path), tmp_prefix, output_buf, level + 1)
				elif os.path.isfile(full_path):
					# print full_path
					output_buf.append("%s%s%s - %s" % (prefix, idc, sub_path,desc[full_path]))

	def make(self, args):
		self.root = args.root
		self.exf = args.exclude_folder
		self.exn = args.exclude_name
		self.max_level = args.max_level

		print("root:%s" % self.root)

		buf = []
		path_parts = self.root.rsplit(os.path.sep, 1)
		buf.append("[%s]" % (path_parts[-1],))
		self._recurse(self.root, os.listdir(self.root), "", buf, 0)

		output_str = "\n".join(buf)
		if len(args.output) != 0:
			with open(args.output, 'w') as of:
				of.write(output_str)
		return output_str

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-r", "--root", help="root of file tree", default=".")
	parser.add_argument("-o", "--output", help="output file name", default="")
	parser.add_argument("-xf", "--exclude_folder", nargs='*', help="exclude folder", default=[])
	parser.add_argument("-xn", "--exclude_name", nargs='*', help="exclude name", default=[])
	parser.add_argument("-m", "--max_level", help="max level",
						type=int, default=-1)
	args = parser.parse_args()

	print(FileTreeMaker().make(args))