/** \class STAMuonAnalyzer
 *  Analyzer of the StandAlone muon tracks
 *
 *  \author R. Bellan - INFN Torino <riccardo.bellan@cern.ch>
 */

#include "RecoMuon/StandAloneMuonProducer/test/STAMuonAnalyzer.h"

// Collaborating Class Header
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"

#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "DataFormats/TrajectorySeed/interface/TrajectorySeedCollection.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "RecoMuon/TrackingTools/interface/MuonPatternRecoDumper.h"

#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "SimDataFormats/Track/interface/SimTrack.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"

using namespace std;
using namespace edm;

/// Constructor
STAMuonAnalyzer::STAMuonAnalyzer(const ParameterSet& pset){
//  theSTAMuonLabel = pset.getUntrackedParameter<string>("StandAloneTrackCollectionLabel");
  staSrc_=consumes<edm::View<reco::Track>>(pset.getParameter<edm::InputTag>( "StandAloneTrackCollectionLabel") ) ;
  simSrc_=consumes<edm::View<SimTrack>>(pset.getParameter<edm::InputTag>( "simLabel") ) ;

//  theRootFileName = pset.getUntrackedParameter<string>("rootFileName");
  edm::Service<TFileService> fs;
  theDataType = pset.getUntrackedParameter<string>("DataType");
  
  if(theDataType != "RealData" && theDataType != "SimData")
    //cout<<"Error in Data Type!!"<<endl;

  numberOfSimTracks=0;
  numberOfRecTracks=0;
}

/// Destructor
STAMuonAnalyzer::~STAMuonAnalyzer(){
}

void STAMuonAnalyzer::beginJob(){
  // Create the root file
//  theFile = new TFile(theRootFileName.c_str(), "RECREATE");
//  theFile->cd();

  hPtRec = new TH1F("pTRec","p_{T}^{rec}",40,0,200);
  hPtRec_new = new TH1F("pTRec_matched","p_{T}^{rec}",40,0,200);
  hPtRec_newB = new TH1F("pTRec_matchedB","p_{T}^{rec}",40,0,200);

  hChi2Rec = new TH1F("Chi2","Chi2",60,0,6);
  hChi2Rec_new = new TH1F("Chi2_matched","Chi2",60,0,6);
  hChi2Rec_newB = new TH1F("Chi2_matchedB","Chi2",60,0,6);

  hPtSim = new TH1F("pTSim","p_{T}^{gen} ",40,0,200);
  hPtSim_new = new TH1F("pTSim_matched","p_{T}^{gen} ",40,0,200);
  hPtSim_newB = new TH1F("pTSim_matchedB","p_{T}^{gen} ",40,0,200);


  hEtaSim = new TH1F("eTaSim","eta_{T}^{gen} ",20,1.6,2.4);
  hEtaSim_new = new TH1F("eTaSim_matched","eta_{T}^{gen} ",20,1.6,2.4);
  hEtaSim_newB = new TH1F("eTaSim_matchedB","eta_{T}^{gen} ",20,1.6,2.4);


  hPTDiff = new TH1F("pTDiff","p_{T}^{rec} - p_{T}^{gen} ",200,-200,200);
  hEtaDiff = new TH1F("EtaDiff","#eta^{rec} - #eta^{gen} ",20,-0.2,0.2);
  hPhiDiff = new TH1F("PhiDiff","#phi^{rec} - #phi^{gen} ",40,0.,1.);
  hDrDiff = new TH1F("DrDiff","DR^{rec,gen}",40,0.,1.);

  hPTDiff2 = new TH1F("pTDiff2","p_{T}^{rec} - p_{T}^{gen} ",200,-200,200);
  hPTDiffvsEta = new TH2F("PTDiffvsEta","p_{T}^{rec} - p_{T}^{gen} VS #eta",100,-2.5,2.5,250,-120,120);
  hPTDiffvsPhi = new TH2F("PTDiffvsPhi","p_{T}^{rec} - p_{T}^{gen} VS #phi",100,-6,6,250,-120,120);

  hPres = new TH1F("pTRes","pT Resolution",100,-2,2);
  hPres_new = new TH1F("pTRes_matched","pT Resolution",100,-2,2);
  hPres_newB = new TH1F("pTRes_matchedB","pT Resolution",100,-2,2);

  h1_Pres = new TH1F("invPTRes","1/pT Resolution",100,-2,2);
}

void STAMuonAnalyzer::endJob(){
  if(theDataType == "SimData"){
    cout << endl << endl << "Number of Sim tracks: " << numberOfSimTracks << endl;
  }

  cout << "Number of Reco tracks: " << numberOfRecTracks << endl << endl;
    
  // Write the histos to file
  //theFile->cd();
  hPtRec->Write();
  hPtRec_new->Write();
  hPtRec_newB->Write();

  hChi2Rec->Write();
  hChi2Rec_new->Write();
  hChi2Rec_newB->Write();

  hPtSim->Write();
  hPtSim_new->Write();
  hPtSim_newB->Write();

  hEtaSim->Write();
  hEtaSim_new->Write();
  hEtaSim_newB->Write();

  hPres->Write();
  hPres_new->Write();
  hPres_newB->Write();

  h1_Pres->Write();
  hPTDiff->Write();
  hEtaDiff->Write();
  hPhiDiff->Write();
  hDrDiff->Write();

  hPTDiff2->Write();
  hPTDiffvsEta->Write();
  hPTDiffvsPhi->Write();
 // theFile->Close();
}
 

void STAMuonAnalyzer::analyze(const Event & event, const EventSetup& eventSetup){
  
  cout << "Run: " << event.id().run() << " Event: " << event.id().event() << endl;
  MuonPatternRecoDumper debug;
  
  // Get the RecTrack collection from the event
  Handle<edm::View<reco::Track>> staTracks;
//  event.getByLabel(theSTAMuonLabel, staTracks);
   event.getByToken(staSrc_, staTracks);

  ESHandle<MagneticField> theMGField;
  eventSetup.get<IdealMagneticFieldRecord>().get(theMGField);

  ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  eventSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);
  
  double recPt=0.;
  double recChi2=-5.0;
  double simPt=0.;
  double simEta=-100.;
  double simPhi=-100.;

  // Get the SimTrack collection from the event
  if(theDataType == "SimData"){
    Handle<edm::View<SimTrack>> simTracks;
//    event.getByLabel("g4SimHits",simTracks);
    event.getByToken(simSrc_,simTracks);
  
    numberOfRecTracks += staTracks->size();

//    SimTrackContainer::const_iterator simTrack;
   edm::View<SimTrack>::const_iterator  simTrack;
    cout<<"Simulated tracks: "<<endl;
    for (simTrack = simTracks->begin(); simTrack != simTracks->end(); ++simTrack){
      if (abs((*simTrack).type()) == 13) {
//	cout<<"Sim pT: "<<(*simTrack).momentum().pt()<<endl;
	simPt=(*simTrack).momentum().pt();
        hPtSim->Fill(simPt);
        simEta=(*simTrack).momentum().eta();
        simPhi=(*simTrack).momentum().phi();
        hEtaSim->Fill(simEta);
//	cout<<"Sim Eta: "<<(*simTrack).momentum().eta()<<endl;
	numberOfSimTracks++;
        cout<<"--a--"<<" "<<numberOfSimTracks<<endl;
      }    
    }
    cout << endl;
  }
  
//  reco::TrackCollection::const_iterator staTrack;
   edm::View<reco::Track>::const_iterator staTrack;
  cout<<"Reconstructed tracks: " << staTracks->size() << endl;

  for (staTrack = staTracks->begin(); staTrack != staTracks->end(); ++staTrack){
    reco::TransientTrack track(*staTrack,&*theMGField,theTrackingGeometry); 
  //  cout << debug.dumpFTS(track.impactPointTSCP().theState());
    recPt = track.impactPointTSCP().momentum().perp();   
    recChi2 = track.chi2()/track.ndof(); 
    
  //  cout<<" eta: "<<track.impactPointTSCP().position().eta()<<" "<<track.impactPointTSCP().momentum().eta()<<endl;
  //  cout<<" p: "<<track.impactPointTSCP().momentum().mag()<< " pT: "<<recPt<<endl;
  //  cout<<" chi2: "<<track.chi2()<<endl;
    
    hPtRec->Fill(recPt);
    hChi2Rec->Fill(recChi2);
    TrajectoryStateOnSurface innerTSOS = track.innermostMeasurementState();
    //cout << "Inner TSOS:"<<endl;
    //cout << debug.dumpTSOS(innerTSOS);
    //cout<<" p: "<<innerTSOS.globalMomentum().mag()<< " pT: "<<innerTSOS.globalMomentum().perp()<<endl;

    trackingRecHit_iterator rhbegin = staTrack->recHitsBegin();
    trackingRecHit_iterator rhend = staTrack->recHitsEnd();
    
    //cout<<"RecHits:"<<endl;
    for(trackingRecHit_iterator recHit = rhbegin; recHit != rhend; ++recHit){
      const GeomDet* geomDet = theTrackingGeometry->idToDet((*recHit)->geographicalId());
      double r = geomDet->surface().position().perp();
      double z = geomDet->toGlobal((*recHit)->localPosition()).z();
      cout<<"r: "<< r <<" z: "<<z <<endl;
    }
    
//      hPtSim->Fill(simPt);


    if(recPt && theDataType == "SimData"){  

      hPres->Fill( (recPt-simPt)/simPt);
//      hPtSim->Fill(simPt);

      hPTDiff->Fill(recPt-simPt);
//cout<<track.impactPointTSCP().position().eta()<<" .... "<<track.impactPointTSCP().position().phi()<<endl;
      double etadiff=(track.impactPointTSCP().momentum().eta())-(simEta);
      double phidiff=fabs(track.impactPointTSCP().momentum().phi()-(simPhi));
      if(phidiff>3.141593654){phidiff=2*3.141592654-phidiff;}
      double drdiff=sqrt(etadiff*etadiff+phidiff*phidiff);
      hEtaDiff->Fill(etadiff);
      hPhiDiff->Fill(phidiff);
      hDrDiff->Fill(drdiff);

      if(fabs(drdiff)<0.1) {
          hPtRec_new->Fill(recPt);
          hChi2Rec_new->Fill(recChi2);
          hPtSim_new->Fill(simPt);
          hEtaSim_new->Fill(simEta);
          hPres_new->Fill( (recPt-simPt)/simPt);
      }

      if(fabs(drdiff)<0.05) {
          hPtRec_newB->Fill(recPt);
          hChi2Rec_newB->Fill(recChi2);
          hPtSim_newB->Fill(simPt);
          hEtaSim_newB->Fill(simEta);
          hPres_newB->Fill( (recPt-simPt)/simPt);
      }


      hPTDiff2->Fill(track.innermostMeasurementState().globalMomentum().perp()-simPt);
      hPTDiffvsEta->Fill(track.impactPointTSCP().position().eta(),recPt-simPt);
      hPTDiffvsPhi->Fill(track.impactPointTSCP().position().phi(),recPt-simPt);
      if( ((recPt-simPt)/simPt) <= -0.4)
      h1_Pres->Fill( ( 1/recPt - 1/simPt)/ (1/simPt));
    }

    
  }
  //cout<<"---"<<endl;  
}

DEFINE_FWK_MODULE(STAMuonAnalyzer);
