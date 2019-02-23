

# To see your cmake version
cmake --version

# To search cmake
sudo apt search cmake
But result might display not-latest version of cmake

# ======================================================================
You can download latest version of cmake via https://cmake.org/download/
Direct link is
wget https://github.com/Kitware/CMake/releases/download/v3.13.4/cmake-3.13.4-Linux-x86_64.sh

Or using curl
curl https://github.com/Kitware/CMake/releases/download/v3.13.4/cmake-3.13.4-Linux-x86_64.sh -o cmake.sh

# ======================================================================
sh cmake-3.13.4-Linux-x86_64.sh --help

sh cmake-3.13.4-Linux-x86_64.sh --version

To install cmake into current_directory_pwd/cmake-test-install
# Note that replace young with your user name
sh cmake-3.13.4-Linux-x86_64.sh --prefix=/home/young/cmake-test-install

# ======================================================================
By default the CMake will be installed in:
  "/home/young/cmake-test-install/cmake-3.13.4-Linux-x86_64"
Do you want to include the subdirectory cmake-3.13.4-Linux-x86_64?
Saying no will install in: "/home/young/cmake-test-install" [Yn]:

type y

# ======================================================================
cd /home/young/cmake-test-install

You can see structure of directories 

You can make this installed cmake globally

# ======================================================================
To install cmake globally, first remove test cmake
rm -rf cmake-test-install

# ======================================================================
It's important to use "/usr/local/" not "/usr"
Linux specification says all packages 
which are not managed by global system package manager
should go to "/usr/local/"
exclude-subdir: you exclude subdir when installing
sudo sh cmake-3.13.4-Linux-x86_64.sh --prefix=/usr/local/ --exclude-subdir

Result:
This is a self-extracting archive.
The archive will be extracted to: /usr/local/

Using target directory: /usr/local/
Extracting, please wait...

Unpacking finished successfully

# ======================================================================
# See version of cmake you installed just ago
/usr/local/bin/cmake --version

cmake-gui --version
