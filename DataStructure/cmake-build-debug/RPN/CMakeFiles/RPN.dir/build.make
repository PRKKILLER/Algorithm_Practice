# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.15

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Users/wonderful_xue/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/193.6911.21/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/wonderful_xue/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/193.6911.21/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/wonderful_xue/code_repo/Algorithm/DataStructure

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug

# Include any dependencies generated for this target.
include RPN/CMakeFiles/RPN.dir/depend.make

# Include the progress variables for this target.
include RPN/CMakeFiles/RPN.dir/progress.make

# Include the compile flags for this target's objects.
include RPN/CMakeFiles/RPN.dir/flags.make

RPN/CMakeFiles/RPN.dir/main.cpp.o: RPN/CMakeFiles/RPN.dir/flags.make
RPN/CMakeFiles/RPN.dir/main.cpp.o: ../RPN/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object RPN/CMakeFiles/RPN.dir/main.cpp.o"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && /Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/RPN.dir/main.cpp.o -c /Users/wonderful_xue/code_repo/Algorithm/DataStructure/RPN/main.cpp

RPN/CMakeFiles/RPN.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/RPN.dir/main.cpp.i"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/wonderful_xue/code_repo/Algorithm/DataStructure/RPN/main.cpp > CMakeFiles/RPN.dir/main.cpp.i

RPN/CMakeFiles/RPN.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/RPN.dir/main.cpp.s"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/wonderful_xue/code_repo/Algorithm/DataStructure/RPN/main.cpp -o CMakeFiles/RPN.dir/main.cpp.s

RPN/CMakeFiles/RPN.dir/RPN.cpp.o: RPN/CMakeFiles/RPN.dir/flags.make
RPN/CMakeFiles/RPN.dir/RPN.cpp.o: ../RPN/RPN.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object RPN/CMakeFiles/RPN.dir/RPN.cpp.o"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && /Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/RPN.dir/RPN.cpp.o -c /Users/wonderful_xue/code_repo/Algorithm/DataStructure/RPN/RPN.cpp

RPN/CMakeFiles/RPN.dir/RPN.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/RPN.dir/RPN.cpp.i"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/wonderful_xue/code_repo/Algorithm/DataStructure/RPN/RPN.cpp > CMakeFiles/RPN.dir/RPN.cpp.i

RPN/CMakeFiles/RPN.dir/RPN.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/RPN.dir/RPN.cpp.s"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/wonderful_xue/code_repo/Algorithm/DataStructure/RPN/RPN.cpp -o CMakeFiles/RPN.dir/RPN.cpp.s

# Object files for target RPN
RPN_OBJECTS = \
"CMakeFiles/RPN.dir/main.cpp.o" \
"CMakeFiles/RPN.dir/RPN.cpp.o"

# External object files for target RPN
RPN_EXTERNAL_OBJECTS =

RPN/RPN: RPN/CMakeFiles/RPN.dir/main.cpp.o
RPN/RPN: RPN/CMakeFiles/RPN.dir/RPN.cpp.o
RPN/RPN: RPN/CMakeFiles/RPN.dir/build.make
RPN/RPN: RPN/CMakeFiles/RPN.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable RPN"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/RPN.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
RPN/CMakeFiles/RPN.dir/build: RPN/RPN

.PHONY : RPN/CMakeFiles/RPN.dir/build

RPN/CMakeFiles/RPN.dir/clean:
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN && $(CMAKE_COMMAND) -P CMakeFiles/RPN.dir/cmake_clean.cmake
.PHONY : RPN/CMakeFiles/RPN.dir/clean

RPN/CMakeFiles/RPN.dir/depend:
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/wonderful_xue/code_repo/Algorithm/DataStructure /Users/wonderful_xue/code_repo/Algorithm/DataStructure/RPN /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/RPN/CMakeFiles/RPN.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : RPN/CMakeFiles/RPN.dir/depend
