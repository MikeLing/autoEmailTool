import logging

logger = logging.getLogger(__name__)

class Config(object):
    def __init__(self):
        self._svn = None
        self._repoPath = None
        self._warName = None
        self._stageServer = None
        self._warPath = None

    def loadConfig(self, meta):
        if meta == None:
            logger.error("the config file shouldn't not be empty")
            return
        
        self._svn = meta['svn']
        self._repoPath = meta['repoPath']
        self._warName = meta['warName']
        self._stageServer = meta['stageServer']
        self._warPath = meta['warPath']

    # getter and setter for svn
    @property
    def svn(self):
        return self._svn
    
    @svn.setter
    def svn(self, newSVN):
        self._svn = newSVN

    # getter and setter for repoPath
    @property
    def repoPath(self):
        return self._repoPath

    @repoPath.setter
    def repoPath(self, repoPath):
        self._repoPath = repoPath

    # getter and setter for warName
    @property
    def warName(self):
        return self._warName

    @warName.setter
    def warName(self, warName):
        self._warName = warName

    # getter and setter for stageServer
    @property
    def stageServer(self):
        return self._stageServer
    
    @stageServer.setter
    def stageServer(self, stageServer):
        self._stageServer = stageServer

    # getter and setter for warPath
    @property
    def warPath(self):
        return self._warPath
    
    @warPath.setter
    def warPath(self, warPath):
        self._warPath = warPath