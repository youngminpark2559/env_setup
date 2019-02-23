
mkdir how-to-cmake-good-0b
cd how-to-cmake-good-0b
vim CmakeLists.txt

# ======================================================================
# You need this lowerest version to run this CmakeLists.txt file
cmake_minimum_required(VERSION 3.12)

# You set your project name as MyProject and version as 1.0.0
project(MyProject VERSION 1.0.0)

# ======================================================================
mkdir build
cd build
# You specify directory where CmakeLists.txt file is located in
cmake ..

# ======================================================================
Go into build directory

You will see 1 directory (CMakeFiles) and 3 files (CMakeCache.txt, cmake_install.cmake, Makefile)

# ======================================================================
You can use ccmake which is command-line based cmake

Press c to configure

But ccmake look not convinient

# ======================================================================
You can use GUI cmake by typing cmake-gui

configure "where is the source code" to target your source directory

configure "where to build the binaries" for example, /build directory which you used from above

Press "Configure"
Use default option

Press "Generate"

# ======================================================================


