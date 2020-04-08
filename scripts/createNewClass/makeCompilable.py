import copyFiles

class makeCompilable(object):

  def __init__(self, className):
    self.printDebug  = False
    self.cf = copyFiles.copyFiles(className) #import.class
    self.className =  self.cf.getClassName()
    self.nameSpace  = self.cf.getNameSpace()
    self.topLevelDir = self.cf.getTopLevelDir()
    self.headerFile, self.SrcFile, self.TestFile = self.cf.getDstDirs()
    self.origClassName = "Foo"
    self.origNameSpace = "fooNameSpace"
    self.newFuncName   = "revStr"
    self.origInludeGrd = "FOOGUARD"
    self.newIncludeGrd = self.className.upper()

  def replaceStrInFile(self, fullPathFName, origStr, replaceStr):
    # Read in the file
    with open(fullPathFName, 'r') as file :
      filedata = file.read()
    # Replace the target string
    filedata = filedata.replace(origStr, replaceStr)
    # Write the file out again
    with open(fullPathFName, 'w') as file:
      file.write(filedata)

  def updateHeaderClassName(self):
    if self.printDebug : print("\nIn: " + self.headerFile + "\nupdated " + self.origClassName + " to " + self.className)
    self.replaceStrInFile(self.headerFile, self.origClassName, self.className)
    # Update the include guarde as well
    self.replaceStrInFile(self.headerFile, self.origInludeGrd, self.newIncludeGrd)

  def updateSourceClassName(self):
    if self.printDebug : print("\nIn: " + self.SrcFile + "\nupdated " + self.origClassName + " to " + self.className)
    self.replaceStrInFile(self.SrcFile, self.origClassName, self.className)

  def updateTestClassName(self):
    if self.printDebug : print("\nIn: " + self.TestFile + "\nupdated " + self.origClassName + " to " + self.className)
    self.replaceStrInFile(self.TestFile, self.origClassName, self.className)

  def updateNameSpace(self):
    if self.printDebug : print("\nUdating namespace: " + self.origNameSpace + " to " + self.nameSpace)
    self.replaceStrInFile(self.headerFile, self.origNameSpace, self.nameSpace)
    self.replaceStrInFile(self.SrcFile, self.origNameSpace, self.nameSpace)
    self.replaceStrInFile(self.TestFile, self.origNameSpace, self.nameSpace)

  def updateCmake(self, srcName):
    cmakeFile = self.topLevelDir + "/codeQs/tests/CMakeLists.txt"
    if self.printDebug : print("TopLevelDir: " + cmakeFile)

    #if we already updated cmake with this class don't do it again
    if self.strExistsInFile(cmakeFile, self.className):
      if self.printDebug : print("CMake was already updated with " + self.className)
      return

    # update source file
    pyFlag = "#nextSource"
    srcStr = "../" + srcName + ".cpp" + "\n  #nextSource"
    self.replaceStrInFile(cmakeFile, pyFlag, srcStr)
    # update header file
    pyFlag = "#nextHeader"
    headerStr = "../" + srcName + ".h" + "\n  #nextHeader"
    self.replaceStrInFile(cmakeFile, pyFlag, headerStr)
    # update test file
    pyFlag = "#nextTest"
    testStr = srcName + "Test.cpp" + "\n  #nextTest"
    self.replaceStrInFile(cmakeFile, pyFlag, testStr)

  def strExistsInFile(self, file, str):
    with open(file) as f:
        if str in f.read():
            return True

  # This is the main function to be called by other classes
  def makeClassCompilable(self):
    self.updateHeaderClassName()
    self.updateSourceClassName()
    self.updateTestClassName()
    self.updateNameSpace()
    self.updateCmake(self.className)


###################################
# Run the code
##################################
#obj = makeCompilable()
#obj.updateHeaderClassName()
#obj.updateSourceClassName()
#obj.updateTestClassName()
#obj.updateNameSpace()
#obj.updateCmake(obj.className)





