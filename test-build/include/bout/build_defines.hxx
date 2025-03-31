#pragma once
#ifndef BOUT_BUILD_CONFIG_HXX
#define BOUT_BUILD_CONFIG_HXX

#define BOUT_CHECK_LEVEL 2
// #define BOUT_FLAGS_STRING $<$<NOT:$<COMPILE_LANGUAGE:CUDA>>: $<$<OR:$<CXX_COMPILER_ID:GNU>,$<CXX_COMPILER_ID:Clang>,$<CXX_COMPILER_ID:AppleClang>>: -Wall -Wextra > > $<$<CXX_COMPILER_ID:MSVC>: /W4 > $<$<COMPILE_LANGUAGE:CUDA>:-Xcompiler=-Wall -Xcompiler=-Wextra > $<$<NOT:$<COMPILE_LANGUAGE:CUDA>>:-Wnull-dereference > $<$<COMPILE_LANGUAGE:CUDA>:-Xcompiler=-Wnull-dereference > $<$<NOT:$<COMPILE_LANGUAGE:CUDA>>:-Wno-cast-function-type > $<$<COMPILE_LANGUAGE:CUDA>:-Xcompiler=-Wno-cast-function-type > -DCHECK=2 -fPIC-O2 -g -DNDEBUG
#define BOUT_OPENMP_SCHEDULE static
#define BOUT_HAS_ARKODE 0
#define BOUT_HAS_CVODE 0
#define BOUT_HAS_FFTW 1
#define BOUT_HAS_GETTEXT 0
#define BOUT_HAS_HYPRE 0
#define BOUT_HAS_IDA 0
#define BOUT_HAS_LAPACK 0
#define BOUT_HAS_NETCDF 1
#define BOUT_HAS_PETSC 0
#define BOUT_HAS_PRETTY_FUNCTION 1
#define BOUT_HAS_PVODE 1
#define BOUT_HAS_SCOREP 0
#define BOUT_HAS_SLEPC 0
#define BOUT_HAS_SUNDIALS 0
#define BOUT_HAS_UUID_SYSTEM_GENERATOR 0
#define BOUT_USE_BACKTRACE 1
#define BOUT_USE_COLOR 1
#define BOUT_USE_OPENMP 0
#define BOUT_USE_OUTPUT_DEBUG 0
#define BOUT_USE_SIGFPE 0
#define BOUT_USE_SIGNAL 1
#define BOUT_USE_TRACK 1
#define BOUT_HAS_UMPIRE 0
#define BOUT_HAS_CALIPER 0
#define BOUT_HAS_RAJA 0
#define BOUT_HAS_CUDA 0
#define BOUT_METRIC_TYPE 2D
#define BOUT_USE_METRIC_3D 0
#define BOUT_USE_MSGSTACK 1

// CMake build does not support legacy interface
#define BOUT_HAS_LEGACY_NETCDF 0

#endif // BOUT_BUILD_CONFIG_HXX
