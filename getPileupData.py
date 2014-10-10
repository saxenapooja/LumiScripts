# Just to make sure we have a CMSSW environment:
from FWCore.PythonUtilities.LumiList import LumiList

import tempfile
import sys
import os

tmpDir=tempfile.gettempdir()

tasks = { '2011':
	{ 'min-bias-xsec': 68000, 'pileup-json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/PileUp/pileup_2011_JSON_pixelLumi.txt', 'cert-jsons': [
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.txt',
		 'run-range': (160404, 163869)},
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt',
		 'run-range': (165088, 167913)},
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v3.txt',
		 'run-range': (170826, 172619)},
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt',
		 'run-range': (172620, 173692)},
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt',
		 'run-range': (175832, 180252)},
	]}, '2012': { 'min-bias-xsec': 69400, 'pileup-json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/PileUp/pileup_JSON_DCSONLY_190389-208686_All_2012_pixelcorr.txt', 'cert-jsons': [
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt',
		 'run-range': (190456, 193621)},
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt',
		 'run-range': (193833, 196531)},
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt',
		 'run-range': (198022, 203742)},
		{'json': '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt',
		 'run-range': (203768, 208686)},
	]}
}

task = '2012'

prevJson = None
for index, component in enumerate(tasks[task]['cert-jsons']):
	json = component['json']
	runmin, runmax = component['run-range']

	tmpFilteredJson = os.path.join(tmpDir, "filteredJSON.json")
	thisJson = os.path.join(tmpDir, "pileupJson%d.json" % index)

	os.system("filterJSON.py --min=%i --max=%i --output=%s %s" % (runmin, runmax, tmpFilteredJson, json))
	if prevJson is not None:
		os.system("compareJSON.py --or %s %s %s" % (tmpFilteredJson, prevJson, thisJson))
	else:
		os.rename(tmpFilteredJson, thisJson)
	prevJson = thisJson

print 'Final JSON: %s' % prevJson
print 'Running pileupCalc.py...'

os.system('pileupCalc.py -i %s --inputLumiJSON %s --calcMode true --minBiasXsec %d --maxPileupBin 100 --numPileupBins 100  pileup/Pileup_%s.root' % (prevJson, tasks[task]['pileup-json'], tasks[task]['min-bias-xsec'], task))
