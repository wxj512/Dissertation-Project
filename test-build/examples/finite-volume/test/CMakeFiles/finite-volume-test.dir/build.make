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
include examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/compiler_depend.make

# Include the progress variables for this target.
include examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/progress.make

# Include the compile flags for this target's objects.
include examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/flags.make

examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/codegen:
.PHONY : examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/codegen

examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o: examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/flags.make
examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/finite-volume/test/finite_volume.cxx
examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o: examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o -MF CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o.d -o CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/finite-volume/test/finite_volume.cxx

examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/finite-volume-test.dir/finite_volume.cxx.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/finite-volume/test/finite_volume.cxx > CMakeFiles/finite-volume-test.dir/finite_volume.cxx.i

examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/finite-volume-test.dir/finite_volume.cxx.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/finite-volume/test/finite_volume.cxx -o CMakeFiles/finite-volume-test.dir/finite_volume.cxx.s

# Object files for target finite-volume-test
finite__volume__test_OBJECTS = \
"CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o"

# External object files for target finite-volume-test
finite__volume__test_EXTERNAL_OBJECTS =

examples/finite-volume/test/finite-volume-test: examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/finite_volume.cxx.o
examples/finite-volume/test/finite-volume-test: examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/build.make
examples/finite-volume/test/finite-volume-test: lib/libbout++.so.5.1.0
examples/finite-volume/test/finite-volume-test: lib/libfmt.so.10.1.1
examples/finite-volume/test/finite-volume-test: lib/libpvode.so.1.0.0
examples/finite-volume/test/finite-volume-test: lib/libpvpre.so.1.0.0
examples/finite-volume/test/finite-volume-test: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so
examples/finite-volume/test/finite-volume-test: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi.so
examples/finite-volume/test/finite-volume-test: /usr/lib/x86_64-linux-gnu/libnetcdf_c++4.so
examples/finite-volume/test/finite-volume-test: /usr/lib/x86_64-linux-gnu/libnetcdf_mpi.so.19
examples/finite-volume/test/finite-volume-test: /usr/local/lib/libfftw3.so
examples/finite-volume/test/finite-volume-test: examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable finite-volume-test"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/finite-volume-test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/build: examples/finite-volume/test/finite-volume-test
.PHONY : examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/build

examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/clean:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test && $(CMAKE_COMMAND) -P CMakeFiles/finite-volume-test.dir/cmake_clean.cmake
.PHONY : examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/clean

examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/depend:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/finite-volume/test /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : examples/finite-volume/test/CMakeFiles/finite-volume-test.dir/depend

