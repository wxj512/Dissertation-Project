# CMake generated Testfile for 
# Source directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/MMS/diffusion
# Build directory: /mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tests/MMS/diffusion
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(MMS-diffusion "./runtest")
set_tests_properties(MMS-diffusion PROPERTIES  ENVIRONMENT "PYTHONPATH=/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tools/pylib:/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tools/pylib:" PROCESSORS "1" PROCESSOR_AFFINITY "ON" _BACKTRACE_TRIPLES "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/BOUT++functions.cmake;215;add_test;/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/cmake/BOUT++functions.cmake;251;bout_add_integrated_or_mms_test;/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/MMS/diffusion/CMakeLists.txt;1;bout_add_mms_test;/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tests/MMS/diffusion/CMakeLists.txt;0;")
