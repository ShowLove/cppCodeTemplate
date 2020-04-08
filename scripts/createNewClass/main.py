import subprocess # to run bash script
import copyFiles as cFiles
import makeCompilable as compilable
import utils # delete class or print class info

def main():
  # initialize info class
  infoObj = utils.utils()
  infoObj.printRepoClassList()
  
  
  # prompt user
  print("\n0 = exit\n1 = info\n2 = create new class\n3 = delete class\n4 = test compile")
  userInput = input("\nEnter your value: ") 

  # prompt loop
  while userInput != 0:
    if userInput == 0: #exit
      break
    elif userInput == 1: #info
      print("\n0 = exit\n1 = info\n2 = create new class\n3 = delete class\n4 = test compile")
      # print info
      infoObj.printRepoClassList()
      userInput = input("\nEnter your value: ")
    elif userInput == 2: # create new class
      className = raw_input("\nClassName you want to create (minus the extesion) e.g FooClass not FooClass.cpp: ")
      copyObj = cFiles.copyFiles(className)
      compObj = compilable.makeCompilable(className)
      # Copy and rename template files to src and test directory 
      copyObj.moveFiles()
      # Update the src header and test file such that it will compile 
      compObj.makeClassCompilable()
      userInput = input("\nEnter your value: ")
    elif userInput == 3: # delete class
      className = raw_input("\nClassName you want to delet (minus the extesion) e.g FooClass not FooClass.cpp: ")
      print("deleting class " + className)
      infoObj.deleteClass(className)
      userInput = input("\nEnter your value: ")
    elif userInput == 4: # test compile
      # Test compile 
      rc = subprocess.call("./runCodeQsTests.sh")
      userInput = input("\nEnter your value: ")
    else:
      print("Invalid input")
      userInput = input("\nEnter your value: ")


if __name__ == "__main__":
    # execute only if run as a script
    main()