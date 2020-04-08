#include "gtest/gtest.h"
#include "utils.h"

#include "ReverseStr.h" // for reverseString

#define PRINT_SEARCH_DEBUG 0

namespace codeQs
{

class utilsTest : public ::testing::Test {

 public:

  utilsTest() {}
  ~utilsTest(){}

 protected:
  virtual void SetUp() 
  {
  
  }

  virtual void TearDown() 
  {

  }
  
  utils obj;
  ReverseStr objRevStr;
};

TEST_F(utilsTest, opOnStdFromCharTest){

  // convert std::string to char* string and operate on it.
  // That is operate on the char* and it will affect std::string

  //char strRev[] = "87654321"; // SYNTAX declar char* cpp way
  char* strRev = (char*) "87654321";
  std::string stdStr = "12345678";

  // convert std::string to char*, reverse it using pointers and check that it is reversed
  char* charStr = utils::opOnStdFromChar(stdStr);
  objRevStr.reverseString(charStr, stdStr.length());
  EXPECT_TRUE(strcmp(charStr, strRev)==0); 
  // convert char* back to std and compare against original std, they shoudl be the same
  // since modifying the char* modifies the std string
  std::string converteCharStr(charStr); // SYNTAX convert char* to std::string
  EXPECT_TRUE(converteCharStr.compare(stdStr)==0); 
}

TEST_F(utilsTest, strsAreEqTest){
  std::string str1 = "abcdefg";
  std::string str2 = "abcdefg";
  std::string str3 = "abcdefgg";
  EXPECT_TRUE(utils::strsAreEq(str1, str2));
  EXPECT_FALSE(utils::strsAreEq(str1, str3));
}

} // utils end