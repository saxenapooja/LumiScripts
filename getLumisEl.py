from FWCore.PythonUtilities.LumiList import LumiList

import os, sys, tempfile

"""
	call with
		python getLumis.py
"""

# please note that runMin and runMax do not have to be the same
# as the json file
tasks = [
	{
		"fileGC": None, #"jsons/processed_SingleMu_2011A_May10thRR.json",
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.txt",
		"runMin": 160404,
		"runMax": 163869,
		"comment": "Run 2011A 10May ReReco",
		"HLT": "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None, #"jsons/processed_SingleMu_2011A_PR_v4.json",
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt",
		"runMin": 165088,
		"runMax": 167913,
		"comment": "Run 2011A PromptReco v4",
		"HLT": "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None, #"jsons/processed_DoubleMu_2011A_RR_2012-01-16_v1.json",
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Reprocessing/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v3.txt",
		"runMin": 170826,
		"runMax": 172619,
		"comment": "Run 2011A 05Aug ReReco",
		"HLT": "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TightIsoPFTau20_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None, #"jsons/processed_DoubleMu_2011A_RR_2012-01-16_v1.json",
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt",
		"runMin": 172620,
		"runMax": 173198,
		"comment": "Run 2011A 03Oct ReReco (1/2)",
		"HLT": "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_TightIsoPFTau20_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None, #"jsons/processed_DoubleMu_2011A_RR_2012-01-16_v1.json",
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt",
		"runMin": 173236,
		"runMax": 173692,
		"comment": "Run 2011A 03Oct ReReco (2/2)",
		"HLT": "HLT_Ele20_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None, #"jsons/processed_DoubleMu_2011B_RR_2012-01-16_v1.json",
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions11/7TeV/Prompt/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt",
		"runMin": 175832, 
		"runMax": 180252,
		"comment": "Run 2011B PromptReco v1",
		"HLT": "HLT_Ele20_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_MediumIsoPFTau20_v*",
		"PixelLumi": True,
	},
	# 2012 53X
	{
		"fileGC": None,
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt",
		"runMin": 190456,
		"runMax": 193621,
		"comment": "Run 2012A 22Jan ReReco",
		"HLT": "HLT_Ele20_CaloIdVT_CaloIsoRhoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None,
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt",
		"runMin": 193833,
		"runMax": 196531,
		"comment": "Run 2012B 22Jan ReReco",
		"HLT": "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None,
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt",
		"runMin": 198022,
		"runMax": 203742,
		"comment": "Run 2012C 22Jan ReReco",
		"HLT": "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*",
		"PixelLumi": True,
	},
	{
		"fileGC": None,
		"fileJSON": "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt",
		"runMin": 203768,
		"runMax": 208686,
		"comment": "Run 2012D 22Jan ReReco",
		"HLT": "HLT_Ele22_eta2p1_WP90Rho_LooseIsoPFTau20_v*",
		"PixelLumi": True
	},
]

tmpDir=tempfile.gettempdir()

tmpLumiResult = os.path.join(tmpDir, "luminosityInformation.txt")

if os.path.exists(tmpLumiResult):
	os.remove(tmpLumiResult)

for task in tasks:
	if task["fileGC"] is not None and not os.path.exists(task["fileGC"]):
		print "skip task as file could not be found: %s" % task["fileGC"]
		continue
	print "processing %s..." % task["comment"]

	tmpFilteredOfficialJSON = os.path.join(tmpDir, "filteredOfficialJSON.json")
	tmpFilteredGCJSON = os.path.join(tmpDir, "filteredGCJSON.json")

	os.system("filterJSON.py --min=%i --max=%i --output=%s %s" % (task["runMin"], task["runMax"], tmpFilteredOfficialJSON, task["fileJSON"]))

	tmpFilteredCombinedJSON = os.path.join(tmpDir, "filteredCombinedJSON_%s.json" % os.path.basename(task["comment"].replace(' ','').replace('/','-').replace('(','_').replace(')','_')))
	if task["fileGC"] is not None:
		os.system("filterJSON.py --min=%i --max=%i --output=%s %s" % (task["runMin"], task["runMax"], tmpFilteredGCJSON, task["fileGC"]))
		os.system("compareJSON.py --and %s %s %s" % (tmpFilteredGCJSON, tmpFilteredOfficialJSON, tmpFilteredCombinedJSON))
	else:
		open(tmpFilteredCombinedJSON, 'w').write(open(tmpFilteredOfficialJSON, 'r').read())

	os.system(r"echo -e '\n\n%s:\n' >> %s" % (task["comment"], tmpLumiResult))

	if task["PixelLumi"]:
		os.system("pixelLumiCalc.py --hltpath %s -i %s recorded | tail -n 5 >> %s" % (task["HLT"], tmpFilteredCombinedJSON, tmpLumiResult))
	else:
		os.system("lumiCalc2.py -b stable --hltpath %s -i %s recorded | tail -n 5 >> %s" % (task["HLT"], tmpFilteredCombinedJSON, tmpLumiResult))
	
print "\nyou can find the luminosity information in %s\n" % tmpLumiResult
