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
include examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/compiler_depend.make

# Include the progress variables for this target.
include examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/progress.make

# Include the compile flags for this target's objects.
include examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/flags.make

examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/codegen:
.PHONY : examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/codegen

examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o: examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/flags.make
examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/conducting-wall-mode/cwm.cxx
examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o: examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o -MF CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o.d -o CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/conducting-wall-mode/cwm.cxx

examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/conducting-wall-mode.dir/cwm.cxx.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/conducting-wall-mode/cwm.cxx > CMakeFiles/conducting-wall-mode.dir/cwm.cxx.i

examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/conducting-wall-mode.dir/cwm.cxx.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/conducting-wall-mode/cwm.cxx -o CMakeFiles/conducting-wall-mode.dir/cwm.cxx.s

# Object files for target conducting-wall-mode
conducting__wall__mode_OBJECTS = \
"CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o"

# External object files for target conducting-wall-mode
conducting__wall__mode_EXTERNAL_OBJECTS =

examples/conducting-wall-mode/conducting-wall-mode: examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/cwm.cxx.o
examples/conducting-wall-mode/conducting-wall-mode: examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/build.make
examples/conducting-wall-mode/conducting-wall-mode: lib/libbout++.so.5.1.0
examples/conducting-wall-mode/conducting-wall-mode: lib/libfmt.so.10.1.1
examples/conducting-wall-mode/conducting-wall-mode: lib/libpvode.so.1.0.0
examples/conducting-wall-mode/conducting-wall-mode: lib/libpvpre.so.1.0.0
examples/conducting-wall-mode/conducting-wall-mode: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so
examples/conducting-wall-mode/conducting-wall-mode: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi.so
examples/conducting-wall-mode/conducting-wall-mode: /usr/lib/x86_64-linux-gnu/libnetcdf_c++4.so
examples/conducting-wall-mode/conducting-wall-mode: /usr/lib/x86_64-linux-gnu/libnetcdf_mpi.so.19
examples/conducting-wall-mode/conducting-wall-mode: /usr/local/lib/libfftw3.so
examples/conducting-wall-mode/conducting-wall-mode: examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable conducting-wall-mode"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/conducting-wall-mode.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/build: examples/conducting-wall-mode/conducting-wall-mode
.PHONY : examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/build

examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/clean:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode && $(CMAKE_COMMAND) -P CMakeFiles/conducting-wall-mode.dir/cmake_clean.cmake
.PHONY : examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/clean

examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/depend:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/conducting-wall-mode /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : examples/conducting-wall-mode/CMakeFiles/conducting-wall-mode.dir/depend

