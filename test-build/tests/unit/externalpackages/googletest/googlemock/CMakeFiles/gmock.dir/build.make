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
include tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/progress.make

# Include the compile flags for this target's objects.
include tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/flags.make

tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/codegen:
.PHONY : tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/codegen

tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o: tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/flags.make
tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/googletest/googlemock/src/gmock-all.cc
tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o: tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o -MF CMakeFiles/gmock.dir/src/gmock-all.cc.o.d -o CMakeFiles/gmock.dir/src/gmock-all.cc.o -c /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/googletest/googlemock/src/gmock-all.cc

tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/gmock.dir/src/gmock-all.cc.i"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/googletest/googlemock/src/gmock-all.cc > CMakeFiles/gmock.dir/src/gmock-all.cc.i

tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/gmock.dir/src/gmock-all.cc.s"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/googletest/googlemock/src/gmock-all.cc -o CMakeFiles/gmock.dir/src/gmock-all.cc.s

# Object files for target gmock
gmock_OBJECTS = \
"CMakeFiles/gmock.dir/src/gmock-all.cc.o"

# External object files for target gmock
gmock_EXTERNAL_OBJECTS =

lib/libgmock.so.1.15.2: tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o
lib/libgmock.so.1.15.2: tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/build.make
lib/libgmock.so.1.15.2: lib/libgtest.so.1.15.2
lib/libgmock.so.1.15.2: tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library ../../../../../lib/libgmock.so"
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gmock.dir/link.txt --verbose=$(VERBOSE)
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock && $(CMAKE_COMMAND) -E cmake_symlink_library ../../../../../lib/libgmock.so.1.15.2 ../../../../../lib/libgmock.so.1.15.2 ../../../../../lib/libgmock.so

lib/libgmock.so: lib/libgmock.so.1.15.2
	@$(CMAKE_COMMAND) -E touch_nocreate lib/libgmock.so

# Rule to build all files generated by this target.
tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/build: lib/libgmock.so
.PHONY : tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/build

tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/clean:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock && $(CMAKE_COMMAND) -P CMakeFiles/gmock.dir/cmake_clean.cmake
.PHONY : tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/clean

tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/depend:
	cd /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/googletest/googlemock /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : tests/unit/externalpackages/googletest/googlemock/CMakeFiles/gmock.dir/depend

