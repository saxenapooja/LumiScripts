#!/bin/bash

for f in *_M-130_*.root; do
    keep="${f%_?_???.root}"
    if [[ "$keep" != "$f" ]]; then
        mv "$f" "${keep}.root"
    fi
done

#OIFS=$IFS
#for ofile in TTFH_MC_SUSYGluGluToHToTauTau_M-130_8TeV-pythia6-tauola_*.root
#do
#    IFS=_
#    set $ofile
#    IFS=$OIFS
#    nfile="$1_$2_$3.root"
##    mv "${ofile}" "${nfile}"
#    printf "mv %s %s\n" ${ofile} ${nfile}
#done
#

#for file in TTFH_MC_SUSYGluGluToHToTauTau_M-130_8TeV-pythia6-tauola_118_*.root
#  do
#  n_file="${file%_*}"
#  n_file="${n_file%_*}"
#  mv "$file" "${n_file}.root"
#done

# workiing version
#for FILE in TTFH_MC_SUSYGluGluToHToTauTau_M-130*.root;
#do mv "$FILE" $(echo "$FILE" | sed 's/TTFH_MC_SUSYGluGluToHToTauTau_M-130_/TTFH_MC_SUSYGluGluToHToTauTau_M-130_8TeV-pythia6-tauola_/'); 
#done


#f in *.cpp; do
# echo Renaming $f to $g.jpg...
# mv $f $g.jpg
