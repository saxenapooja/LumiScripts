#!/bin/bash 
date

usage () {
    echo "@@@@@@ Higgs_tau_tau "
    echo "              ==Possible arguments=="
    echo "  makelib                                 - to build lib of MainAnalyzer"
    echo "  lumi                                    - to create_lumi"
    echo "  help                                    - shows this help"
}


SetupEnv() {
    source $LIB
}


MakeLib() {
    cd /nfs/dust/cms/user/pooja/scratch/plot-macro/AnalysisTool_WH
    source AnalysisToolUseThis
    ./configure --prefix=/nfs/dust/cms/user/pooja/scratch/plot-macro/lib_AnalysisTool
    make
    make install
    echo '@@@@@@@@@@@@@ LIBERARIES ARE BUILD @@@@@@@@@@@@@@@@@@@@@@'
    popd
}

LUMI() {
#    python create-lumi.py /nfs/dust/cms/user/pooja/samples/higgs_cp_study/GluGluToHToTauTau_M-125_tauPolarOff_MC_v8_vtxWithBS GluGluToHToTauTau_M-125_tauPolarOff_MC_v8_vtxWithBS

# working test
#    python create-lumi.py /nfs/dust/cms/user/pooja/samples/vbf_tautau_reproduce TTFH_MC_VBF_HToTauTau_M-125_8TeV-powheg-pythia6
    python create-lumi.py /nfs/dust/cms/user/pooja/samples/syncEx_tautau_Christian_Oct2014/output_crab TTFH_MC_SUSYGluGluToHToTauTau_M-130_8TeV-pythia6-tauola
}

if [ "$1" = "help" ]; then
    usage

elif [ "$1" = "makelib" ]; then
    SetupEnv
    MakeLib

#create_lumi
elif [ "$1" = "lumi" ]; then
    SetupEnv
    LUMI
fi
