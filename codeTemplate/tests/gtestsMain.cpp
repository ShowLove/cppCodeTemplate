#include "gtest/gtest.h"

/* g++ -lgtest gtestsMain.cpp -o gtestsMain.out */
int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv); 
  return RUN_ALL_TESTS();
}
