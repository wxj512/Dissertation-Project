# Install script for directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/examples

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
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/2Dturbulence_multigrid/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/6field-simple/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/advection-diffusion/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/advection-reaction/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/diffusion-nl/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/IMEX/drift-wave-constraint/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/advdiff2/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/backtrace/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/blob2d/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/blob2d-outerloop/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/blob2d-laplacexz/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/boundary-conditions/advection/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conducting-wall-mode/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conduction/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/conduction-snb/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/constraints/alfven-wave/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/constraints/laplace-dae/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/dalf3/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/eigen-box/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/elm-pb/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/elm-pb-outerloop/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/em-drift/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/fci-wave/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/fci-wave-logn/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/diffusion/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/fluid/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/finite-volume/test/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/gas-compress/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/gravity_reduced/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/gyro-gem/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/hasegawa-wakatani/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/hasegawa-wakatani-3d/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/invertable_operator/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/jorek-compare/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/lapd-drift/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/laplacexy/alfven-wave/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/laplacexy/laplace_perp/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/laplacexy/simple/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/laplacexy/simple-hypre/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/monitor/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/monitor-newapi/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/orszag-tang/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/preconditioning/wave/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/reconnect-2field/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/shear-alfven-wave/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/staggered_grid/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/subsampling/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/tokamak-2fluid/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/uedge-benchmark/cmake_install.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for the subdirectory.
  include("/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/wave-slab/cmake_install.cmake")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
if(CMAKE_INSTALL_LOCAL_ONLY)
  file(WRITE "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/examples/install_local_manifest.txt"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
endif()
