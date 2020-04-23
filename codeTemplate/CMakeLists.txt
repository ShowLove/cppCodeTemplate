cmake_minimum_required(VERSION 2.6)

project(${GTEST_PROJECT} C CXX)

set(CMAKE_C_STANDARD 98)
set(CMAKE_CXX_STANDARD 98)

#include .h and .cpp files in util folder
include_directories("${CMAKE_CURRENT_SOURCE_DIR}")

##########
# GTests
#########
add_subdirectory(tests)