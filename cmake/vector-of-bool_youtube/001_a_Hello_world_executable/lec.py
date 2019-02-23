vim main.cpp
#include <iostream>

int main()
{
  std::cout<<"Hello, world\n";
}

# ======================================================================
vim CMakeLists.txt

cmake_minimum_required(VERSION 3.12)

project(MyProject VERSION 1.0.0)

# cmake-good: executable file name
# main.cpp: target source file
add_executable(cmake-good main.cpp)

# ======================================================================
mkdir build && cd build && cmake ..

You will succeed with configuration with seeing messages


-- The C compiler identification is GNU 5.4.0 # CMake detects C compiler
-- The CXX compiler identification is GNU 5.4.0 # CMake detects C++ compiler (CMake uses XX because ++ creates parsing error in some cases)
-- Check for working C compiler: /usr/bin/cc # location of C compiler
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /mnt/1T-5e7/mycodehtml/os/cmake/vector-of-bool_youtube/001_a_Hello_world_executable/test/build

CMake creates Makefile then you can use make

# ======================================================================
For sidenotes, you can delete config files
rm CMakeCache.txt
rm CMakeFiles/

Then you can reconfigure
cmake ..

# ======================================================================
# .: filder where CMakeCache.txt is
cmake --build .

Scanning dependencies of target cmake-good
[ 50%] Building CXX object CMakeFiles/cmake-good.dir/main.cpp.o
[100%] Linking CXX executable cmake-good # cmake creates cmake-good executable file
[100%] Built target cmake-good # "target cmake-good" has been built

# ======================================================================
# Run executable file
./cmake-good

Hello, world

# ======================================================================

