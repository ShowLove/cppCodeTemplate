import copyFiles
import glob  # to list files in directory
import os

class utils(object):

  def __init__(self):
    self.printDebug  = True
    # using class for paths only no need to feed it a class name 
    self.cf = copyFiles.copyFiles("NA") #import.class
    self.topLevelDir = self.cf.getTopLevelDir()
    self.repoDir = self.cf.getRepoDir()
    self.testDir = self.cf.getTestDir()

  def getRepoClassList(self):
    if self.printDebug : print("Current Classes: \n")
    cppFilesPattern = self.repoDir + "*.cpp"
    return glob.glob(cppFilesPattern)

  def printRepoClassList(self):
    repoList = self.getRepoClassList()
    # printing the list using loop 
    for x in range(len(repoList)): 
        print(repoList[x])

  def deleteClass(self, className):
    srcFile = self.repoDir + className + ".cpp"
    headerFile = self.repoDir + className + ".h"
    testFile = self.testDir + className + "Test.cpp"
    if self.fileExists(srcFile):
      os.remove(srcFile)
    if self.fileExists(headerFile):
      os.remove(headerFile)
    if self.fileExists(testFile):
      os.remove(testFile)

    self.removeClassFromCMake(className)

  # removes line that has class name in it
  def removeClassFromCMake(self, className):
    cmakeFile = self.testDir + "CMakeLists.txt"
    cmakeFile2 = self.testDir + "CMakeLists2.txt"
    classToDelete = "../" + className + ".cpp"
    headerToDelete = "../" + className + ".h"
    testToDelete = className + "Test.cpp"
    # remove lines that conains these strings
    bad_words = [classToDelete, headerToDelete, testToDelete]
    with open(cmakeFile) as oldfile, open(cmakeFile2, 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
    # If you scared you can comment below code and check cmakeFile2
    os.remove(cmakeFile)
    os.rename(cmakeFile2, cmakeFile)

  def fileExists(self, path):
    if os.path.isfile(path):
        print ("File exists:\t\t" + path)
        return True
    else:
        print ("File does not exist:\t\t" + path)
        return False 



###################################
# Run the code
##################################
#obj = utils()
#obj.removeClassFromCMake("StrHasUniqueChars")


