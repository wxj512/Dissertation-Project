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
include tests/integrated/test-squash/CMakeFiles/test-squash.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/integrated/test-squash/CMakeFiles/test-squash.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/integrated/test-squash/CMakeFiles/test-squash.dir/progress.make

# Include the compile flags for this target's objects.
include tests/integrated/test-squash/CMakeFiles/test-squash.dir/flags.make

tests/integrated/test-squash/CMakeFiles/test-squash.dir/codegen:
.PHONY : tests/integrated/test-squash/CMakeFiles/test-squash.dir/codegen

tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.o: tests/integrated/test-squash/CMakeFiles/test-squash.dir/flags.make
tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-squash/squash.cxx
tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.o: tests/integrated/test-squash/CMakeFiles/test-squash.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.o -MF CMakeFiles/test-squash.dir/squash.cxx.o.d -o CMakeFiles/test-squash.dir/squash.cxx.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-squash/squash.cxx

tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/test-squash.dir/squash.cxx.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-squash/squash.cxx > CMakeFiles/test-squash.dir/squash.cxx.i

tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/test-squash.dir/squash.cxx.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-squash/squash.cxx -o CMakeFiles/test-squash.dir/squash.cxx.s

# Object files for target test-squash
test__squash_OBJECTS = \
"CMakeFiles/test-squash.dir/squash.cxx.o"

# External object files for target test-squash
test__squash_EXTERNAL_OBJECTS =

tests/integrated/test-squash/squash: tests/integrated/test-squash/CMakeFiles/test-squash.dir/squash.cxx.o
tests/integrated/test-squash/squash: tests/integrated/test-squash/CMakeFiles/test-squash.dir/build.make
tests/integrated/test-squash/squash: lib/libbout++.so.5.1.0
tests/integrated/test-squash/squash: lib/libfmt.so.10.1.1
tests/integrated/test-squash/squash: lib/libpvode.so.1.0.0
tests/integrated/test-squash/squash: lib/libpvpre.so.1.0.0
tests/integrated/test-squash/squash: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so
tests/integrated/test-squash/squash: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi.so
tests/integrated/test-squash/squash: /usr/lib/x86_64-linux-gnu/libnetcdf_c++4.so
tests/integrated/test-squash/squash: /usr/lib/x86_64-linux-gnu/libnetcdf_mpi.so.19
tests/integrated/test-squash/squash: /usr/local/lib/libfftw3.so
tests/integrated/test-squash/squash: tests/integrated/test-squash/CMakeFiles/test-squash.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable squash"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-squash.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/integrated/test-squash/CMakeFiles/test-squash.dir/build: tests/integrated/test-squash/squash
.PHONY : tests/integrated/test-squash/CMakeFiles/test-squash.dir/build

tests/integrated/test-squash/CMakeFiles/test-squash.dir/clean:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash && $(CMAKE_COMMAND) -P CMakeFiles/test-squash.dir/cmake_clean.cmake
.PHONY : tests/integrated/test-squash/CMakeFiles/test-squash.dir/clean

tests/integrated/test-squash/CMakeFiles/test-squash.dir/depend:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-squash /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash/CMakeFiles/test-squash.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : tests/integrated/test-squash/CMakeFiles/test-squash.dir/depend

