#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "PVODE::pvode" for configuration "RelWithDebInfo"
set_property(TARGET PVODE::pvode APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(PVODE::pvode PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libpvode.so.1.0.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libpvode.so.1.0.0"
  )

list(APPEND _cmake_import_check_targets PVODE::pvode )
list(APPEND _cmake_import_check_files_for_PVODE::pvode "${_IMPORT_PREFIX}/lib/libpvode.so.1.0.0" )

# Import target "PVODE::pvpre" for configuration "RelWithDebInfo"
set_property(TARGET PVODE::pvpre APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(PVODE::pvpre PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libpvpre.so.1.0.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libpvpre.so.1.0.0"
  )

list(APPEND _cmake_import_check_targets PVODE::pvpre )
list(APPEND _cmake_import_check_files_for_PVODE::pvpre "${_IMPORT_PREFIX}/lib/libpvpre.so.1.0.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
