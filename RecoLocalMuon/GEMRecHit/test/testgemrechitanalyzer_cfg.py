import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
#  8 eta partitions :: command line option :: --geometry Geometry/GEMGeometry/cmsExtendedGeometryPostLS1plusGEMr08v01XML_cfi.py
# 10 eta partitions :: command line option :: --geometry Geometry/GEMGeometry/cmsExtendedGeometryPostLS1plusGEMr10v01XML_cfi.py
# process.load('Geometry.GEMGeometry.cmsExtendedGeometryPostLS1plusGEMr08v01XML_cfi')
# process.load('Geometry.GEMGeometry.cmsExtendedGeometryPostLS1plusGEMr10v01XML_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D1Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D1_cff')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/user/q/qili/workspace/GEMTEST/201611/pre10/sample/src/singlemugun.root'
    )
)

process.demo = cms.EDAnalyzer('MyGEMRecHitAnalyzer',
                              RootFileName = cms.untracked.string("TestGEMRecHitHistograms.root"),
)


process.p = cms.Path(process.demo)
