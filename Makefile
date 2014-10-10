main_lumi: main_lumi.cc
	g++ main_lumi.cc -o main_lumi `root-config --cflags --libs` -I /nfs/dust/cms/user/pooja/scratch/plot-macro/lib_AnalysisTool/include -L /nfs/dust/cms/user/pooja/scratch/plot-macro/lib_AnalysisTool/lib -lAnalysisTool -O3
