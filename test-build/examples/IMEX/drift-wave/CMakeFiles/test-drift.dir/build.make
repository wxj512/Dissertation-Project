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
include examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/compiler_depend.make

# Include the progress variables for this target.
include examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/progress.make

# Include the compile flags for this target's objects.
include examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/flags.make

examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/codegen:
.PHONY : examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/codegen

examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.o: examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/flags.make
examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/IMEX/drift-wave/test-drift.cxx
examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.o: examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.o -MF CMakeFiles/test-drift.dir/test-drift.cxx.o.d -o CMakeFiles/test-drift.dir/test-drift.cxx.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/IMEX/drift-wave/test-drift.cxx

examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/test-drift.dir/test-drift.cxx.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/IMEX/drift-wave/test-drift.cxx > CMakeFiles/test-drift.dir/test-drift.cxx.i

examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/test-drift.dir/test-drift.cxx.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/IMEX/drift-wave/test-drift.cxx -o CMakeFiles/test-drift.dir/test-drift.cxx.s

# Object files for target test-drift
test__drift_OBJECTS = \
"CMakeFiles/test-drift.dir/test-drift.cxx.o"

# External object files for target test-drift
test__drift_EXTERNAL_OBJECTS =

examples/IMEX/drift-wave/test-drift: examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/test-drift.cxx.o
examples/IMEX/drift-wave/test-drift: examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/build.make
examples/IMEX/drift-wave/test-drift: lib/libbout++.so.5.1.0
examples/IMEX/drift-wave/test-drift: lib/libfmt.so.10.1.1
examples/IMEX/drift-wave/test-drift: lib/libpvode.so.1.0.0
examples/IMEX/drift-wave/test-drift: lib/libpvpre.so.1.0.0
examples/IMEX/drift-wave/test-drift: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so
examples/IMEX/drift-wave/test-drift: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi.so
examples/IMEX/drift-wave/test-drift: /usr/lib/x86_64-linux-gnu/libnetcdf_c++4.so
examples/IMEX/drift-wave/test-drift: /usr/lib/x86_64-linux-gnu/libnetcdf_mpi.so.19
examples/IMEX/drift-wave/test-drift: /usr/local/lib/libfftw3.so
examples/IMEX/drift-wave/test-drift: examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test-drift"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-drift.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/build: examples/IMEX/drift-wave/test-drift
.PHONY : examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/build

examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/clean:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave && $(CMAKE_COMMAND) -P CMakeFiles/test-drift.dir/cmake_clean.cmake
.PHONY : examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/clean

examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/depend:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/IMEX/drift-wave /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : examples/IMEX/drift-wave/CMakeFiles/test-drift.dir/depend

