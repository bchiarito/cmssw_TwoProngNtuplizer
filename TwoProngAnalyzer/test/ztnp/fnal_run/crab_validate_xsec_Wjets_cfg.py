from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.workArea = 'crab_multi_validate_xsec_dec19_WJets'
config.section_('JobType')
config.JobType.psetName = '../../cmssw_twoprongntuplizer_cfg.py'
config.JobType.pyCfgParams = ['globalTag=mc2016', 'mcInfo=True', 'tauTnPselection=False', 'standardTwoProng=False', 'tauModifiedTwoProng=False', 'includeCands=False', 'includeTauTau=False']
config.JobType.pluginName = 'Analysis'
config.section_('Data')
config.Data.outLFNDirBase = '/store/user/bchiari1/twoprong/ztagandprobe/Dec19_trees/validateWJets/'
config.Data.outputDatasetTag = "twoprongntuplizer"
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 200000
config.Data.totalUnits =  -1
config.Data.publication = False
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'


if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    config.General.requestName = 'WJets'
    config.Data.outputDatasetTag = "twoprongntuplizer"
    config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=29705748','mcXS=50320'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'WJets_ext2'
    config.Data.outputDatasetTag = "twoprongntuplizer_ext2"
    config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=57026058','mcXS=50320'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W1Jets'
    config.Data.outputDatasetTag = "twoprongntuplizer"
    config.Data.inputDataset = '/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W2Jets'
    config.Data.outputDatasetTag = "twoprongntuplizer"
    config.Data.inputDataset = '/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W2Jets_ext1'
    config.Data.outputDatasetTag = "twoprongntuplizer_ext1"
    config.Data.inputDataset = '/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W3Jets'
    config.Data.outputDatasetTag = "twoprongntuplizer"
    config.Data.inputDataset = '/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W3Jets_ext1'
    config.Data.outputDatasetTag = "twoprongntuplizer_ext1"
    config.Data.inputDataset = '/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W4Jets'
    config.Data.outputDatasetTag = "twoprongntuplizer"
    config.Data.inputDataset = '/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W4Jets_ext1'
    config.Data.outputDatasetTag = "twoprongntuplizer_ext1"
    config.Data.inputDataset = '/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]

    config.General.requestName = 'W4Jets_ext2'
    config.Data.outputDatasetTag = "twoprongntuplizer_ext2"
    config.Data.inputDataset = '/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM'
    config.JobType.pyCfgParams.extend(['mcN=1','mcXS=1'])
    submit(config)
    config.JobType.pyCfgParams = config.JobType.pyCfgParams[:-2]
