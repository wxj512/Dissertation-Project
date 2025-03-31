#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "bout++::bout++" for configuration "RelWithDebInfo"
set_property(TARGET bout++::bout++ APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(bout++::bout++ PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libbout++.so.5.1.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libbout++.so.5.1.0"
  )

list(APPEND _cmake_import_check_targets bout++::bout++ )
list(APPEND _cmake_import_check_files_for_bout++::bout++ "${_IMPORT_PREFIX}/lib/libbout++.so.5.1.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
