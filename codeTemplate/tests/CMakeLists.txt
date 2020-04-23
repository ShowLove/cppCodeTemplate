cmake_minimum_required(VERSION 2.6)

set(GTEST_PROJECT gtestProject)

enable_testing()

message("Gtest Cmake")

find_package(GTest REQUIRED)

# The utils, test, and gtests directories
include_directories("${CMAKE_CURRENT_SOURCE_DIR}")
include_directories("/usr/local/Cellar/gtest/include")
include_directories("/usr/local/Cellar/gtest/lib")

set(SOURCES
  gtestsMain.cpp
  ../utils.cpp
  ../StrHasUniqueChars.cpp
  ../ReverseStr.cpp
  ../StrIsPermutation.cpp
  ../ReplaceSubString.cpp
  #nextSource
  utilsTest.cpp
  StrHasUniqueCharsTest.cpp
  ReverseStrTest.cpp
  StrIsPermutationTest.cpp
  ReplaceSubStringTest.cpp
  #nextTest
)

set(HEADERS
  ../utils.h
  ../StrHasUniqueChars.h
  ../ReverseStr.h
  ../StrIsPermutation.h
  ../ReplaceSubString.h
  #nextHeader
)

add_executable(${GTEST_PROJECT} ${SOURCES})
target_link_libraries(${GTEST_PROJECT} PUBLIC
  gtest
  gtest_main
)

add_test(${GTEST_PROJECT} ${GTEST_PROJECT})

