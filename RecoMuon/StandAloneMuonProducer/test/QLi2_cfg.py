import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
#process = cms.Process("RecoSTAMuon",eras.phase2_muon)
process = cms.Process("STARECO")
process.load("RecoMuon.Configuration.RecoMuon_cff")
process.load("RecoMuon.Configuration.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.EventContent.EventContent_cff')
#process.load('Configuration.Geometry.GeometryExtended2023tiltedReco_cff')
#process.load('Configuration.Geometry.GeometryExtended2023tilted_cff')
#process.load('Configuration.Geometry.GeometryExtended2015MuonGEMDevReco_cff')
#process.load('Configuration.Geometry.GeometryExtended2015MuonGEMDev_cff')
process.load('Configuration.Geometry.GeometryExtended2023D1Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D1_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
      'file:seed-cscgem.root'
  #     '/store/user/qili/Smu-GEN-v22/seed-cscgem/161224_121619/0000/seed-cscgem_207.root '
#      '/store/user/qili/Smu-GEN-v22/seed-csc/161224_122042/0000/seed-csc_118.root'
    )
)
#process.UpdaterService = cms.Service( "UpdaterService",
#)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('INFO'),
        noLineBreaks = cms.untracked.bool(True)
    ),
    destinations = cms.untracked.vstring('cout')
)

#process.out = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string('RecoSTAMuons.root')
#)

process.load("RecoMuon.StandAloneMuonProducer.standAloneMuons_cff")

## Analyzer to produce pT and 1/pT resolution plots
process.STAMuonAnalyzer = cms.EDAnalyzer("STAMuonAnalyzer",
                                         DataType = cms.untracked.string('SimData'),
                                         StandAloneTrackCollectionLabel = cms.InputTag('standAloneMuons'),
                                         simLabel = cms.InputTag('g4SimHits'),
                                         NoGEMCase = cms.untracked.bool(True),
#                                         rootFileName = cms.untracked.string('STAMuonAnalyzer.root')
                                         )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("RStree.root")
                                   )




process.standAloneMuons.InputObjects = cms.InputTag("MSeed") 

#process.p = cms.Path(process.standAloneSETMuons)
process.p = cms.Path(process.standAloneMuons* process.STAMuonAnalyzer)
## default path (no analyzer)
#process.p = cms.Path(process.MuonSeed * process.standAloneMuons * process.STAMuonAnalyzer)  ## path with analyzer
#process.this_is_the_end = cms.EndPath(process.out)
