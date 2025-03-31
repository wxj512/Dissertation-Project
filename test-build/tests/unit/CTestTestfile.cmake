# CMake generated Testfile for 
# Source directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/unit
# Build directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(serial_tests "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/unit/serial_tests" "--gtest_brief=1")
set_tests_properties(serial_tests PROPERTIES  _BACKTRACE_TRIPLES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/unit/CMakeLists.txt;107;add_test;/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/unit/CMakeLists.txt;0;")
subdirs("externalpackages/googletest")
