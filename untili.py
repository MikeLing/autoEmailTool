# -*- coding: UTF-8 -*-


import os
import yaml
import logging
import svn.remote
import subprocess

# fix the encoding issue in python 2.7
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

LOG = logging.getLogger(__name__)
def loadConfig(configPath):
    """
        Load config from yaml
    """
    with open(configPath, 'r') as stream:
        try:
            metaConfig = yaml.load(stream)
            return metaConfig
            
        except yaml.YAMLError as exc:
            LOG.error(exc)


def fetch_code_from_svn(repoPath, svnAddress, rev=None):
    """
        Fetch latest code from svn server
    """
    if not os.path.exists(repoPath):
        r = svn.remote.RemoteClient('svn://223.84.134.45:10032/group3/data/group3directory/编码/serverCode/maintaincar/%s' % repoPath.split('/')[-1])
        info = r.info()
        print "the latest commit revision is {} and the author is {}".format(info['commit_revision'], info['commit_author'])
        os.makedirs(repoPath)
        r.checkout(repoPath)
    else:
        # I have really no idea why pysvn doesn't help :(
        pwd = os.getcwd()
        os.chdir(repoPath)
        subprocess.call(["svn update"], shell=True)
        os.chdir(pwd)


def build_repo(repo, svnAddress, repoPath, revision):
    """
        Build repo
    """
    pppwd = os.getcwd()
    fetch_code_from_svn(repoPath=repoPath, 
                        svnAddress=svnAddress, 
                        rev=revision)
    os.chdir(repoPath)
    subprocess.call(["mvn clean install -Dmaven.taskskip"], shell=True)
    #os.system("mvn clean install -Dmaven.taskskip")
    os.chdir(pppwd)
    return True