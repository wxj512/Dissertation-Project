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
include examples/advdiff2/CMakeFiles/advdiff2.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include examples/advdiff2/CMakeFiles/advdiff2.dir/compiler_depend.make

# Include the progress variables for this target.
include examples/advdiff2/CMakeFiles/advdiff2.dir/progress.make

# Include the compile flags for this target's objects.
include examples/advdiff2/CMakeFiles/advdiff2.dir/flags.make

examples/advdiff2/CMakeFiles/advdiff2.dir/codegen:
.PHONY : examples/advdiff2/CMakeFiles/advdiff2.dir/codegen

examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.o: examples/advdiff2/CMakeFiles/advdiff2.dir/flags.make
examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/init.cxx
examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.o: examples/advdiff2/CMakeFiles/advdiff2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.o -MF CMakeFiles/advdiff2.dir/init.cxx.o.d -o CMakeFiles/advdiff2.dir/init.cxx.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/init.cxx

examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/advdiff2.dir/init.cxx.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/init.cxx > CMakeFiles/advdiff2.dir/init.cxx.i

examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/advdiff2.dir/init.cxx.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/init.cxx -o CMakeFiles/advdiff2.dir/init.cxx.s

examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.o: examples/advdiff2/CMakeFiles/advdiff2.dir/flags.make
examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/rhs.cxx
examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.o: examples/advdiff2/CMakeFiles/advdiff2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.o -MF CMakeFiles/advdiff2.dir/rhs.cxx.o.d -o CMakeFiles/advdiff2.dir/rhs.cxx.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/rhs.cxx

examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/advdiff2.dir/rhs.cxx.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/rhs.cxx > CMakeFiles/advdiff2.dir/rhs.cxx.i

examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/advdiff2.dir/rhs.cxx.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2/rhs.cxx -o CMakeFiles/advdiff2.dir/rhs.cxx.s

# Object files for target advdiff2
advdiff2_OBJECTS = \
"CMakeFiles/advdiff2.dir/init.cxx.o" \
"CMakeFiles/advdiff2.dir/rhs.cxx.o"

# External object files for target advdiff2
advdiff2_EXTERNAL_OBJECTS =

examples/advdiff2/advdiff2: examples/advdiff2/CMakeFiles/advdiff2.dir/init.cxx.o
examples/advdiff2/advdiff2: examples/advdiff2/CMakeFiles/advdiff2.dir/rhs.cxx.o
examples/advdiff2/advdiff2: examples/advdiff2/CMakeFiles/advdiff2.dir/build.make
examples/advdiff2/advdiff2: lib/libbout++.so.5.1.0
examples/advdiff2/advdiff2: lib/libfmt.so.10.1.1
examples/advdiff2/advdiff2: lib/libpvode.so.1.0.0
examples/advdiff2/advdiff2: lib/libpvpre.so.1.0.0
examples/advdiff2/advdiff2: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so
examples/advdiff2/advdiff2: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi.so
examples/advdiff2/advdiff2: /usr/lib/x86_64-linux-gnu/libnetcdf_c++4.so
examples/advdiff2/advdiff2: /usr/lib/x86_64-linux-gnu/libnetcdf_mpi.so.19
examples/advdiff2/advdiff2: /usr/local/lib/libfftw3.so
examples/advdiff2/advdiff2: examples/advdiff2/CMakeFiles/advdiff2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable advdiff2"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/advdiff2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
examples/advdiff2/CMakeFiles/advdiff2.dir/build: examples/advdiff2/advdiff2
.PHONY : examples/advdiff2/CMakeFiles/advdiff2.dir/build

examples/advdiff2/CMakeFiles/advdiff2.dir/clean:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 && $(CMAKE_COMMAND) -P CMakeFiles/advdiff2.dir/cmake_clean.cmake
.PHONY : examples/advdiff2/CMakeFiles/advdiff2.dir/clean

examples/advdiff2/CMakeFiles/advdiff2.dir/depend:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples/advdiff2 /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2 /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2/CMakeFiles/advdiff2.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : examples/advdiff2/CMakeFiles/advdiff2.dir/depend

