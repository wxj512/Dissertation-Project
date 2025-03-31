# Install script for directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set path to fallback-tool for dependency-resolution.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libfmt.so.10.1.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libfmt.so.10"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "/usr/local/lib")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/lib/libfmt.so.10.1.1"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/lib/libfmt.so.10"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libfmt.so.10.1.1"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libfmt.so.10"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "::::::::::::::"
           NEW_RPATH "/usr/local/lib")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/lib/libfmt.so")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/fmt" TYPE FILE FILES
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/args.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/chrono.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/color.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/compile.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/core.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/format.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/format-inl.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/os.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/ostream.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/printf.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/ranges.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/std.h"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include/fmt/xchar.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/fmt" TYPE FILE FILES
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/fmt-config.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/fmt-config-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/fmt/fmt-targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/fmt/fmt-targets.cmake"
         "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/CMakeFiles/Export/b834597d9b1628ff12ae4314c3a2e4b8/fmt-targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/fmt/fmt-targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/fmt/fmt-targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/fmt" TYPE FILE FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/CMakeFiles/Export/b834597d9b1628ff12ae4314c3a2e4b8/fmt-targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/fmt" TYPE FILE FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/CMakeFiles/Export/b834597d9b1628ff12ae4314c3a2e4b8/fmt-targets-relwithdebinfo.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/fmt.pc")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
