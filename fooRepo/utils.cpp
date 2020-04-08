#include "utils.h"

namespace codeQs
{

const int utils::MAX_CHAR;

std::string utils::getRandomStr(const int size) const
{ // TODO test this function
  char c = 'c';
  char* s = new char[size];
  std::string str(s); // SYNTAX: convert char* to std::string at init

  for (int i = 0; i < str.length(); i++)
  {
    str[i] = getRandomNumInRange(a_ASCII_INT, MAX_ASCII_INT);
  }
  return str;
}

int utils::getRandomNumInRange(const int min, const int max) const
{
  return min + rand() % (( max + 1 ) - min); // SYNTAX: get range of random numbers
}

char* utils::convertToCString(std::string str)
{ //TODO test this function
  char *cstr = new char[str.length() + 1];
  strcpy(cstr, str.c_str());

  return cstr;
  //  delete [] cstr; // dont forget to clean up later
}

char* utils::opOnStdFromChar(std::string& strStd)
{
  // To get a non-const conversion we use const_cast conversion
  // This works in constant time as no copying is involved
  // Note that this gives us access to the underlying data structure
  // i.e an array behind std::string. 
  // This means any change to char* will be reflected in the 
  // string object and vice versa.
  return const_cast<char*>(strStd.c_str());
}

void utils::swapP( char *a, char *b )
{
  char tmp = *a;
  *a = *b;
  *b = tmp;
}

bool utils::strsAreEq(const std::string str1, const std::string str2)
{
  if(str1.length() != str2.length())
    return false;

  for(int i = 0; i < str1.length(); i++)
    if(static_cast<int>(str1[i]) != static_cast<int>(str2[i]))
      return false;

  return true;
}

char* utils::getSubstr(const char* arr, const int begin, const int len)
{
    char* res = new char[len];
    for (int i = 0; i < len; i++)
        res[i] = *(arr + begin + i);
    res[len] = 0;
    return res;
}
  
} // codeQs end