import shutil # to copy files
import os     # to change directories using os

# TODO
# 1 should be only one getDir function
# 2 update other classes that use this to use conditional parameters
#   a. currently we have to update defaultRepoName
# 3. Add a class that writes a build script
# 4. Add a class that deletes a directory
# 5. Add a class that adds a new directory with infrastructure

##########################################
# assuming the following folder structure
# topDir -> scripts -> createNewClass
# topDir -> repo1
# topDir -> repo2
##########################################

class copyFiles(object):

  def __init__(self, newClassName, repositoryName="na"):
    self.printDebug  = False
    # set the repo you want to add code to, if none give as param use default
    self.defaultRepoName = "fooRepo"                  # changes when you are working on a different repo
    if repositoryName == "na":
      self.repoName = self.defaultRepoName
    else:
      self.repoName = self.repositoryName
    if self.printDebug : print("using repo:" + "\t\t" + self.repoName)

    self.fooVar = 2    
    self.nameSpace  = self.repoName
    self.headerFile = "Foo.h"
    self.srcFile    = "Foo.cpp"
    self.testFile   = "FooTest.cpp"
    #name of new class
    self.className  = newClassName                    # change with new class
    self.pathToTopLevlDir = "../../"
    self.pathToScriptDir  = "/scripts/createNewClass/"
    self.pathToRepoDir    = "/" +self.repoName +"/"         # changes with new repo
    self.pathToTestDir    = "/" +self.repoName+ "/tests/"   # changes with new repo
    self.pathToGenericCodeDir = "/codeTemplate/"     
    self.topLevelDir = self.getTopLevelDir()

  def getFullPathName(self, dirPath):
    return self.topLevelDir + dirPath

  def getTestDir(self):
    return self.pathToTestDir

  def getSriptDir(self):
    # get script directory
    pythonDir = os.getcwd()
    if self.printDebug : print("scriptDir:" + "\t\t" + pythonDir)
    return pythonDir

  def getTopLevelDir(self):
    # get top level directory
    scriptDir = os.getcwd()
    os.chdir(self.pathToTopLevlDir)
    topLevelDir = os.getcwd()
    # return to script dir and return top level dir
    os.chdir(scriptDir)
    if self.printDebug : print("topLevelDir:" + "\t\t" + topLevelDir)
    return topLevelDir

  def getRepoDir(self):
    # get repo directory
    repoDir = self.getFullPathName(self.pathToRepoDir)
    if self.printDebug : print("repoDir:" + "\t\t" + repoDir)
    return repoDir

  def getTestDir(self):
    # get test directory
    testDir = self.getFullPathName(self.pathToTestDir)
    if self.printDebug : print("testDir:" + "\t\t" + testDir)
    return testDir

  def getGenericCodeDir(self):
    # get generic code directory
    templateCodeDir = self.getFullPathName(self.pathToGenericCodeDir)
    if self.printDebug : print("templateCodeDir:" + "\t" + templateCodeDir)
    return templateCodeDir

  def getSourceDirs(self):
    # Get all relevant directories (path + fileName)
    sourceDir = self.getGenericCodeDir()
    sourceHeader = sourceDir + self.headerFile
    sourceSrc    = sourceDir + self.srcFile
    sourceTest   = sourceDir + self.testFile
    #return the directories that will be used by shutil
    return sourceHeader, sourceSrc, sourceTest  

  def getDstDirs(self):
    # Get all relevant directories (path + fileName)
    dstDir   = self.getRepoDir()
    testDir  = self.getTestDir()
    dstHeader    = dstDir  + self.className + ".h"
    dstSrc       = dstDir  + self.className + ".cpp"
    dstTest      = testDir + self.className + "Test.cpp"
    #return the directories that will be used by shutil
    return dstHeader, dstSrc, dstTest

  def fileExists(self, path):
    if os.path.isfile(path):
        if self.printDebug : print ("File exists:\t\t" + path)
        return True
    else:
        if self.printDebug : print ("File does not exist:\t\t" + path)
        return False 

  # This is the main function to be called by other classes
  def moveFiles(self):
    # get source and destination directories
    dstHeader, dstSrc, dstTest = self.getDstDirs()
    sourceHeader, sourceSrc, sourceTest = self.getSourceDirs()

    if self.printDebug : print("\nmoving: \n" + sourceHeader + "\n"+ sourceSrc + "\n"+ sourceTest + "\n")
    if self.printDebug : print("to: \n" + dstHeader + "\n"+ dstSrc + "\n"+ dstTest + "\n")

    # Copy files over
    shutil.copy(sourceHeader, dstHeader)
    shutil.copy(sourceSrc, dstSrc)
    shutil.copy(sourceTest, dstTest)

    # Check that all files are there
    self.fileExists(dstHeader)
    self.fileExists(dstSrc)
    self.fileExists(dstTest)

  # for other classes to use
  def getClassName(self):
    return self.className

  def getNameSpace(self):
    return self.nameSpace

###################################
# Run the code
##################################
#if self.printDebug : print("Copy Files Script: \n")
#obj = copyFiles()
#obj.moveFiles()





