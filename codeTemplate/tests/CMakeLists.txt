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
  #nextSource
  #nextTest
)

set(HEADERS
  #nextHeader
)

add_executable(${GTEST_PROJECT} ${SOURCES})
target_link_libraries(${GTEST_PROJECT} PUBLIC
  gtest
  gtest_main
)

add_test(${GTEST_PROJECT} ${GTEST_PROJECT})

