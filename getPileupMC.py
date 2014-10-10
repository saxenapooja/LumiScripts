# Just to make sure we have a CMSSW environment:

import sys
files = [x for x in sys.argv[1:]]

sys.argv.append('-b')
import ROOT

import numpy

if '7TeV' in files[0]:
	era = 'Fall11'
elif '8TeV' in files[0]:
	era = 'Summer12'
else:
	raise Exception('Unknown MC era')	

chain = ROOT.TChain()
for x in files:
	chain.AddFile('%s/makeroottree/AC1B' % x)

numTrueInteractions = numpy.array(1, dtype=numpy.float32)
chain.SetBranchStatus('*', 0)
chain.SetBranchStatus('numtruepileupinteractions', 1)
chain.SetBranchAddress("numtruepileupinteractions", numTrueInteractions)

histo = ROOT.TH1D('pileup', 'PileUp distribution', 100, 0.0, 100.0)

for x in range(0, chain.GetEntries()):
	if x % 10000 == 0:
		print '%d/%d...' % (x, chain.GetEntries())
	chain.GetEntry(x)

	histo.Fill(numTrueInteractions)

outfile = ROOT.TFile('pileup/Pileup_%s.root' % era, 'RECREATE')
histo.Write()
outfile.Close()
