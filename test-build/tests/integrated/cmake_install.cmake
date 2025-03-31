# Install script for directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated

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
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-backtrace/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-beuler/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-boutpp/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-bout-override-default-option/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-command-args/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-communications/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-coordinates-initialization/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-cyclic/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-delp2/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-datafilefacade/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-drift-instability/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-drift-instability-staggered/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-fieldgroupComm/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-griddata/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-griddata-yboundary-guards/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-gyro/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-initial/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-interchange-instability/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-interpolate/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-interpolate-z/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invertable-operator/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-invpar/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplace/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplace-petsc3d/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplace-hypre3d/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplacexy2-hypre/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplacexy-fv/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplacexy-short/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplacexz/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-multigrid_laplace/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-naulin-laplace/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-options-netcdf/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-petsc_laplace/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-petsc_laplace_MAST-grid/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-restart-io/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-restarting/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-slepc-solver/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-smooth/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-snb/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-solver/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-squash/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-stopCheck/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-stopCheck-file/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-twistshift/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-twistshift-staggered/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-vec/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-yupdown/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-yupdown-weights/cmake_install.cmake")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
