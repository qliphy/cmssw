from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'KseedSS2-csc-v1'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'QLB_cfg.py'


config.section_("Data")
config.Data.inputDataset = '/S9-GEN-vB/qili-step3-VB-7cd84c7ad3673e90aca8e6660e168632/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = True
config.Data.outputDatasetTag = 'KseedSS2-csc-v1'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_CH_CERN'
