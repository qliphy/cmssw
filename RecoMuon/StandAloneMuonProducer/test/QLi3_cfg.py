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
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_1.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_10.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_100.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_101.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_102.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_104.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_106.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_107.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_108.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_109.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_11.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_110.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_111.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_113.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_115.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_116.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_117.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_118.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_119.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_12.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_121.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_122.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_124.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_125.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_128.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_129.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_13.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_130.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_131.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_133.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_135.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_137.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_138.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_139.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_14.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_140.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_142.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_143.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_144.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_145.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_147.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_148.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_149.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_150.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_151.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_152.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_153.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_155.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_156.root',
'/store/user/qili/S9-GEN-vB/KseedSS2-cscgem-v1/170130_151050/0000/seed-cscgem_157.root',
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
