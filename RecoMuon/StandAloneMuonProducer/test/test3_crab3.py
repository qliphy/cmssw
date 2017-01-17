from WMCore.Configuration import Configuration

config = Configuration()

config.section_("General")
config.General.requestName   = 'STAS1-cscgem-v5'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'QLi2_cfg.py'


config.section_("Data")
config.Data.inputDataset = '/Smu-GEN-vnew/qili-seedS1-cscgem-fc39cfc59369aa38e10a06b18559f601/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1
config.Data.publication = False
#config.Data.outputDatasetTag = 'seed-cscgem'

config.section_("Site")
# Where the output files will be transmitted to
config.Site.storageSite = 'T2_CH_CERN'
