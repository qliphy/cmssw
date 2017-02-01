import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
#process = cms.Process("RecoSTAMuon",eras.phase2_muon)
process = cms.Process("STARECO")
process.load("RecoMuon.Configuration.RecoMuon_cff")
process.load("RecoMuon.Configuration.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.EventContent.EventContent_cff')
#process.load('Configuration.Geometry.GeometryExtended2023D1Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2023D1_cff')
process.load('Configuration.Geometry.GeometryExtended2023D7Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D7_cff') 
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_10.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_102.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_103.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_104.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_105.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_106.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_107.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_108.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_109.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_11.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_110.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_114.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_115.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_116.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_117.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_119.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_12.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_120.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_122.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_123.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_124.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_125.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_126.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_127.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_128.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_13.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_130.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_132.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_134.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_136.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_137.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_14.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_140.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_141.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_142.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_143.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_147.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_149.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_15.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_151.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_152.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_153.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_154.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_156.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_157.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_158.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_159.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-csc-v1/170130_151106/0000/seed-csc_16.root',
#      'file:../../MuonSeedGenerator/test/seed-csc.root'
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
