# Install script for directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev

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

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tools/pylib/_boutpp_build/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/mpark.variant/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/fmt/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/externalpackages/PVODE/cmake_install.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbout++.so.5.1.0" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbout++.so.5.1.0")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbout++.so.5.1.0"
         RPATH "/usr/local/lib:/usr/lib/x86_64-linux-gnu/openmpi/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/lib/libbout++.so.5.1.0")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbout++.so.5.1.0" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbout++.so.5.1.0")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbout++.so.5.1.0"
         OLD_RPATH "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/lib:/usr/local/lib:/usr/lib/x86_64-linux-gnu/openmpi/lib:"
         NEW_RPATH "/usr/local/lib:/usr/lib/x86_64-linux-gnu/openmpi/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libbout++.so.5.1.0")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/lib/libbout++.so")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/include/" FILES_MATCHING REGEX "/[^/]*\\.hxx$")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/include/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE DIRECTORY FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/bin/" USE_SOURCE_PERMISSIONS REGEX "bout-squashoutput" EXCLUDE REGEX "bout-config.in" EXCLUDE REGEX "bout-pylib-cmd-to-bin" EXCLUDE)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE PROGRAM RENAME "bout-config" FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/bin/bout-config-install")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.13/site-packages/boutconfig" TYPE FILE RENAME "__init__.py" FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tools/pylib/boutconfig/__init__.py-install")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++/bout++Targets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++/bout++Targets.cmake"
         "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles/Export/e31d3f53a7e0788863762a6aedb22c76/bout++Targets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++/bout++Targets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++/bout++Targets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++" TYPE FILE FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles/Export/e31d3f53a7e0788863762a6aedb22c76/bout++Targets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++" TYPE FILE FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/CMakeFiles/Export/e31d3f53a7e0788863762a6aedb22c76/bout++Targets-relwithdebinfo.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++" TYPE FILE FILES
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/bout++ConfigVersion.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/BOUT++functions.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/CorrectWindowsPaths.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindClangFormat.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindFFTW.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindHYPRE.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindnetCDF.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindnetCDFCxx.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindPackageMultipass.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindLibuuid.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindPETSc.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindScoreP.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindSLEPc.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindSUNDIALS.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/FindSphinx.cmake"
    "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/ResolveCompilerPaths.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/bout++" TYPE FILE RENAME "bout++Config.cmake" FILES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/bout++Config.cmake-install")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
if(CMAKE_INSTALL_COMPONENT)
  if(CMAKE_INSTALL_COMPONENT MATCHES "^[a-zA-Z0-9_.+-]+$")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
  else()
    string(MD5 CMAKE_INST_COMP_HASH "${CMAKE_INSTALL_COMPONENT}")
    set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INST_COMP_HASH}.txt")
    unset(CMAKE_INST_COMP_HASH)
  endif()
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
