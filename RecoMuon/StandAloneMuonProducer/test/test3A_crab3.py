from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'STAS2-cscgem-A1'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'QLi2_cfg.py'


config.section_("Data")
config.Data.inputDataset = '/S9-GEN-vB/qili-KseedSS2-cscgem-v1-82334dea49757a23ecbea2c2167b87a1/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
#config.Data.outputDatasetTag = 'seed-cscgem'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_CH_CERN'
