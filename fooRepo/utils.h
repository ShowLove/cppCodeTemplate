#ifndef UTILS
#define UTILS

#include <iostream>

namespace codeQs
{

class utils
{
 public:

  utils()
  {
     // SYNTAX: Seed rand in constructor once 
     static bool firstRandomSeed = true;
     if (firstRandomSeed) 
     {  //seeding for the first time only!
        srand( time(NULL) ); // SYNTAX: seed rand
        firstRandomSeed = false;
     }
  }// Default constructor
  ~utils(){}

  ///////////////////////////////////////
  // constants SYNTAX: Constants to know
  //////////////////////////////////////
  static const int MAX_CHAR = 256; // The number of chars
  static const int a_ASCII_INT = static_cast<int>('a'); // smallest ascii
  static const int MAX_ASCII_INT = static_cast<int>('~' + 1); // largest ascii

  
  /* Generate a string of random chars of size "size"
   * @param size size of the string
   * @return a string of random characters
   */
  std::string getRandomStr(const int size) const;

  /* Generate a random number in a range
   * @param min minimun in range
   * @param max in range
   * @return an int random number in range [min, max]
   */
  int getRandomNumInRange(const int min, const int max) const;

  /* Swaps the contents of two pointers. e.g chars in a string
   * @param a pointer 1 to swap
   * @param b pointer 2 to swap
   * @return void
   */ 
  static void swapP( char *a, char *b ); // SYNTAX: use static in header not in src 

  /* Convert an std::string to char*, user is responsible for clean up
   * @param str string you are converting to char*
   * @return returns a char* version of std::string
   */
  static char* convertToCString(std::string str);

  /* Convert an std::string to a char* such that you can modify std from char*
   * @param strStd string to be converted
   * @return returns a char* string that changes std::string
   */
  static char* opOnStdFromChar(std::string& strStd);

  /* Checks if str1 and str2 are equal
   * @param str1 check agains str2
   * @param str2 check agains str1
   * @return returns true if 2 strings are equal flase otherwise
   */ 
  static bool strsAreEq(const std::string str1, const std::string str2);

  /* Gets sub string from begin index to length, up to user to clean up
   * @param arr pointer to a string array
   * @param begin where the substrings begings 
   * @param len length of the substring
   * @return returns a char* to the substring
   */
  static char* getSubstr(const char* arr, const int begin, const int len);


 private:
};

} //codeQs end

#endif