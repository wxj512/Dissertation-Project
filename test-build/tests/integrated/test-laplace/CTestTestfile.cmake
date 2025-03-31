# CMake generated Testfile for 
# Source directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-laplace
# Build directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/integrated/test-laplace
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test-laplace "./runtest")
set_tests_properties(test-laplace PROPERTIES  ENVIRONMENT "PYTHONPATH=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tools/pylib:/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tools/pylib:" PROCESSORS "4" PROCESSOR_AFFINITY "ON" _BACKTRACE_TRIPLES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/BOUT++functions.cmake;215;add_test;/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/BOUT++functions.cmake;246;bout_add_integrated_or_mms_test;/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-laplace/CMakeLists.txt;1;bout_add_integrated_test;/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/integrated/test-laplace/CMakeLists.txt;0;")
