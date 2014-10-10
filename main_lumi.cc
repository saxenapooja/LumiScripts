/*This is an example how to use the AC1B Root-Tree structure. We provide this interface to have an easy access to 
 * data stored in the new Root-Trees.*/
//Include Analyse.h to make the interface available. 
#include "AnalysisTool/Analyse.h"
#include <TH1D.h>
#include <TH2D.h>
#include <TH3D.h>
#include <TMinuit.h>
#include <iostream>
#include <vector>
#include <sstream>
#include <boost/algorithm/string.hpp>


using namespace std;

// You should derive your own class from Analyse.
class MyAnalysis : public Analyse
{
private:
  string currfilename;
public:
  MyAnalysis() {}
  virtual ~MyAnalysis() {}
  // AnalyseEvent is a virtual function which is called for each event.
  virtual Int_t AnalyseEvent() {return(1);}
};

int main(int argc, char* argv[])
{
  // Create an instance of your analysis class.
  TTree::SetMaxTreeSize(4830000000);
  string namebuf;
  string filename;
  string dirname;
  MyAnalysis ana;

  for (int i = 1; i < argc; ++i)
    {
      namebuf = argv[i];
      cout << namebuf << endl;
      
      UInt_t slashpos = namebuf.find_last_of("/");
      if(slashpos == namebuf.size())
	{
	  filename = namebuf;
	}
      else
	{
	  filename = namebuf.substr(slashpos+1);
	  dirname = namebuf.substr(0,slashpos+1);
	}

      if(filename.find("LUMI_") == 0) continue;
      else
	{
	  ana.AddLumiFile(namebuf.c_str(), "makeroottree/");
	}
    } // for (int i = 1; i < argc; ++i)
  cout << "Reading Lumi from text file" << endl;
  
  fstream file("lumi.cvs");
  char line[1000];
  Float_t lumirecorded;
  UInt_t run;
  UInt_t block;
  if(file.is_open())
    {
      file.getline(line, 1000);
      
      while(!file.eof())
	{
	  file.getline(line,1000);
	  vector<std::string> strs;
	  boost::split(strs, line, boost::is_any_of(","));
	  if(strs.size() != 7) continue;
	  run = atoi(strs[0].c_str());
	  vector<std::string> blocks;
	  boost::split(blocks, strs[1], boost::is_any_of(":"));
	  block = atoi(blocks[0].c_str());
	  lumirecorded = atof(strs[6].c_str());
	  //cout << run << " " << block << " " << lumirecorded << endl;
	  ana.SetLumi(run, block, lumirecorded/1000000.);
	}

      file.close();
    }
  else
    {
      cout << "ERROR: lumi.cvs could not be opened!" << endl;
    }
  ana.PrintLumiOfRuns();
  //ana.WriteLumiFile(dirname + string("LUMI_INFO.root"));
  ana.WriteLumiFile("LUMI_INFO.root");
}

