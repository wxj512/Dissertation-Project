# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 4.0

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /snap/cmake/1457/bin/cmake

# The command to remove a file.
RM = /snap/cmake/1457/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build

# Include any dependencies generated for this target.
include tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/progress.make

# Include the compile flags for this target's objects.
include tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/flags.make

tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/codegen:
.PHONY : tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/codegen

tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.o: tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/flags.make
tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-invpar/test_invpar.cxx
tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.o: tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.o -MF CMakeFiles/test-invpar.dir/test_invpar.cxx.o.d -o CMakeFiles/test-invpar.dir/test_invpar.cxx.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-invpar/test_invpar.cxx

tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/test-invpar.dir/test_invpar.cxx.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-invpar/test_invpar.cxx > CMakeFiles/test-invpar.dir/test_invpar.cxx.i

tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/test-invpar.dir/test_invpar.cxx.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-invpar/test_invpar.cxx -o CMakeFiles/test-invpar.dir/test_invpar.cxx.s

# Object files for target test-invpar
test__invpar_OBJECTS = \
"CMakeFiles/test-invpar.dir/test_invpar.cxx.o"

# External object files for target test-invpar
test__invpar_EXTERNAL_OBJECTS =

tests/integrated/test-invpar/test_invpar: tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/test_invpar.cxx.o
tests/integrated/test-invpar/test_invpar: tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/build.make
tests/integrated/test-invpar/test_invpar: lib/libbout++.so.5.1.0
tests/integrated/test-invpar/test_invpar: lib/libfmt.so.10.1.1
tests/integrated/test-invpar/test_invpar: lib/libpvode.so.1.0.0
tests/integrated/test-invpar/test_invpar: lib/libpvpre.so.1.0.0
tests/integrated/test-invpar/test_invpar: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so
tests/integrated/test-invpar/test_invpar: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi.so
tests/integrated/test-invpar/test_invpar: /usr/lib/x86_64-linux-gnu/libnetcdf_c++4.so
tests/integrated/test-invpar/test_invpar: /usr/lib/x86_64-linux-gnu/libnetcdf_mpi.so.19
tests/integrated/test-invpar/test_invpar: /usr/local/lib/libfftw3.so
tests/integrated/test-invpar/test_invpar: tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test_invpar"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-invpar.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/build: tests/integrated/test-invpar/test_invpar
.PHONY : tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/build

tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/clean:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar && $(CMAKE_COMMAND) -P CMakeFiles/test-invpar.dir/cmake_clean.cmake
.PHONY : tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/clean

tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/depend:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-invpar /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : tests/integrated/test-invpar/CMakeFiles/test-invpar.dir/depend

