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
CMAKE_COMMAND = "/Users/wonderful_xue/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/193.6494.38/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/wonderful_xue/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/193.6494.38/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/wonderful_xue/code_repo/Algorithm/DataStructure

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug

# Include any dependencies generated for this target.
include Stack/CMakeFiles/stack.dir/depend.make

# Include the progress variables for this target.
include Stack/CMakeFiles/stack.dir/progress.make

# Include the compile flags for this target's objects.
include Stack/CMakeFiles/stack.dir/flags.make

Stack/CMakeFiles/stack.dir/main.cpp.o: Stack/CMakeFiles/stack.dir/flags.make
Stack/CMakeFiles/stack.dir/main.cpp.o: ../Stack/main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Stack/CMakeFiles/stack.dir/main.cpp.o"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/Stack && /Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/stack.dir/main.cpp.o -c /Users/wonderful_xue/code_repo/Algorithm/DataStructure/Stack/main.cpp

Stack/CMakeFiles/stack.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/stack.dir/main.cpp.i"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/Stack && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/wonderful_xue/code_repo/Algorithm/DataStructure/Stack/main.cpp > CMakeFiles/stack.dir/main.cpp.i

Stack/CMakeFiles/stack.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/stack.dir/main.cpp.s"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/Stack && /Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/wonderful_xue/code_repo/Algorithm/DataStructure/Stack/main.cpp -o CMakeFiles/stack.dir/main.cpp.s

# Object files for target stack
stack_OBJECTS = \
"CMakeFiles/stack.dir/main.cpp.o"

# External object files for target stack
stack_EXTERNAL_OBJECTS =

Stack/stack: Stack/CMakeFiles/stack.dir/main.cpp.o
Stack/stack: Stack/CMakeFiles/stack.dir/build.make
Stack/stack: Stack/CMakeFiles/stack.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable stack"
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/Stack && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/stack.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Stack/CMakeFiles/stack.dir/build: Stack/stack

.PHONY : Stack/CMakeFiles/stack.dir/build

Stack/CMakeFiles/stack.dir/clean:
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/Stack && $(CMAKE_COMMAND) -P CMakeFiles/stack.dir/cmake_clean.cmake
.PHONY : Stack/CMakeFiles/stack.dir/clean

Stack/CMakeFiles/stack.dir/depend:
	cd /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/wonderful_xue/code_repo/Algorithm/DataStructure /Users/wonderful_xue/code_repo/Algorithm/DataStructure/Stack /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/Stack /Users/wonderful_xue/code_repo/Algorithm/DataStructure/cmake-build-debug/Stack/CMakeFiles/stack.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Stack/CMakeFiles/stack.dir/depend

