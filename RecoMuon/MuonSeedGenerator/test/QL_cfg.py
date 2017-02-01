import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")

# Messages
process.load("RecoMuon.Configuration.MessageLogger_cfi")
process.load("Configuration.StandardSequences.Services_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load('Configuration.EventContent.EventContent_cff')
#process.load('Configuration.Geometry.GeometryExtended2023D1Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2023D1_cff')
process.load('Configuration.Geometry.GeometryExtended2023D7Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D7_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#      '/store/user/qili/Smu-GEN-vnew3/step3-VB/170122_022123/0000/step3_84.root' 
      '/store/user/qili/S9-GEN-v1/step3-VB/170125_085127/0000/step3_84.root',
      '/store/user/qili/S9-GEN-v1/step3-VB/170125_085127/0000/step3_85.root',
      '/store/user/qili/S9-GEN-v1/step3-VB/170125_085127/0000/step3_86.root',
      '/store/user/qili/S9-GEN-v1/step3-VB/170125_085127/0000/step3_87.root',
      '/store/user/qili/S9-GEN-v1/step3-VB/170125_085127/0000/step3_88.root',
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
process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('seed-cscgem.root')
                               )


#process.CosmicMuonSeed = cms.EDProducer("CosmicMuonSeedGenerator",
#    MaxSeeds = cms.int32(1000),
#    CSCRecSegmentLabel = cms.InputTag("cscSegments"),
#    EnableDTMeasurement = cms.bool(True),
#    MaxCSCChi2 = cms.double(300.0),
#    MaxDTChi2 = cms.double(300.0),
#    DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
#    EnableCSCMeasurement = cms.bool(True)
#)

from RecoMuon.MuonSeedGenerator.ptSeedParameterization_cfi import *
from RecoMuon.MuonSeedGenerator.MuonSeedPtScale_cfi import *

process.MSeed = cms.EDProducer("MuonSeedGenerator",
     ptSeedParameterization,
     dphiScale,
     beamSpotTag = cms.InputTag("offlineBeamSpot"),
     EnableDTMeasurement = cms.bool(False),
     EnableCSCMeasurement = cms.bool(True),
     EnableGEMMeasurement = cms.bool(True),
     DTRecSegmentLabel = cms.InputTag("dt4DSegments"),
     CSCRecSegmentLabel = cms.InputTag("cscSegments"),
     GEMRecSegmentLabel = cms.InputTag("gemSegments"),
     #GEMRecSegmentLabel = cms.InputTag("gemRecHits"),
     crackEtas = cms.vdouble(0.2, 1.6, 1.7),
     crackWindow = cms.double(0.04),
     scaleDT = cms.bool(True),
     deltaPhiSearchWindow = cms.double(0.25),
     deltaEtaSearchWindow = cms.double(0.2),
     deltaEtaCrackSearchWindow = cms.double(0.25),
)

process.cm = cms.Path(process.MSeed)
process.endjob_step  = cms.Path(process.endOfProcess)
process.out_step = cms.EndPath(process.out)

process.schedule = cms.Schedule (
     process.cm,
     process.endjob_step,
     process.out_step
)
