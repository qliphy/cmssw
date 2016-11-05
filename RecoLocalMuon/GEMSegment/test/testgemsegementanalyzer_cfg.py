import FWCore.ParameterSet.Config as cms

process = cms.Process("TestGEMSegment")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.Geometry.GeometryExtended2015MuonGEMDevReco_cff')
process.load('Configuration.Geometry.GeometryExtended2015MuonGEMDev_cff')
process.load("Alignment.CommonAlignmentProducer.FakeAlignmentSource_cfi") 
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(400) )
# process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )



process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
         'file:/afs/cern.ch/user/q/qili/workspace/GEMTEST/201611/pre10/sample/src/singlemugun.root'
    )
)

process.gemseg = cms.EDAnalyzer('TestGEMSegmentAnalyzer',
                              # ----------------------------------------------------------------------
                              RootFileName = cms.untracked.string("TestGEMSegmentHistograms.root"),
                              # RootFileName = cms.untracked.string("TestGEMSegmentHistograms_Noise.root"),
                              # RootFileName = cms.untracked.string("TestGEMSegmentHistograms_5000evt.root"),
                              # RootFileName = cms.untracked.string("TestGEMSegmentHistograms_Test.root"),
                              # ----------------------------------------------------------------------
                              printSegmntInfo = cms.untracked.bool(False),
                              printResidlInfo = cms.untracked.bool(False),
                              printSimHitInfo = cms.untracked.bool(False),
                              printEventOrder = cms.untracked.bool(False),
                              # ----------------------------------------------------------------------

)


process.p = cms.Path(process.gemseg)
