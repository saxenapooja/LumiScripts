#!/usr/bin/env python

import os
import sys
import re
import subprocess
import shutil

#LUMIDIR = '/scratch/hh/dust/naf/cms/user/aburgmei/tautau-fullyhadronic/WH_Analysis/Lumi/new'
LUMIDIR = '/nfs/dust/cms/user/pooja/scratch/plot-macro/tau-hadronic/Lumi/new'

if len(sys.argv) < 2:
	print 'Usage: %s <Output Directory> [PATTERN]' % sys.argv[0]
	sys.exit(1)

pattern = '.*'
if len(sys.argv) >= 3:
	pattern = sys.argv[2]

inputs = {}
for x in os.listdir(sys.argv[1]):
	filename = os.path.basename(x)

	pmatch = re.match(pattern, filename)
	if not pmatch: continue

	match = re.match(r'(.*)_[0-9]+\.root', filename)
	#match = re.match(r'(.*)_[0-9]_+(.*)\.root', filename)
	print match
	print filename
	if not match: continue
	
	set = match.group(1) #first parenthesized in the filename
	if not set in inputs:
		inputs[set] = [os.path.join(sys.argv[1], filename)]
	else:
		inputs[set].append(os.path.join(sys.argv[1], filename))
		
# TODO: Run this in parallel? Do we gain something?
for input in inputs:
	print 'Processing %s...' % input
	process = subprocess.Popen(['./main_lumi'] + inputs[input], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	if process.returncode != 0:
		print 'Failed to run lumi for %s: %s' % (input, stderr)
	shutil.move('LUMI_INFO.root', os.path.join(LUMIDIR, 'LUMI_INFO_%s.root' % input))
