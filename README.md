Repository to version control Dissertation Project progress
- Compiled BOUT++ builds used for model runs:
  - test-build (BOUT++ ver. 5.1.1, default cmake)
  - test-blob2d (BOUT++ ver. 5.1.1, default cmake)
  - BOUT++5.1.1 (BOUT++ ver. 5.1.1, default cmake)
- Overleaf repository
  - (Token:olp_4s5GTBpsRzOXbp9YV6efZvKvASJ1dg3VNYs3)
  - Project log (latex file, compiled with xelatex in Overleaf)
    - Figs (png for all figure used in project log)
    - References (BibLaTex file)
  - Literature review and lay summary (latex file, compiled with xelatex in Overleaf)
    - Figs (png for all figure used in literature review)
    - References (BibLaTex file)
- Miscellaneous files
  - Wrapped as test_blob2dgp module
    - vel_out/ (contains .py files for processing and calculating velocity of blob)
    - model_run/ (contains .py files for creating inp file and for executing blob2d model runs)
    - GP/ (contains .py files for performing gaussian process on data for machine learning on blob velocity)
  - Data folder
    - Inputs
      - delta_*/ (input files for v_data.py, contains BOUT.dmp.x.nc, .inp and .setting files)
      - delta_1_B0_*/ (input files for v_data.py, contains BOUT.dmp.x.nc, .inp and .setting files)
    - Outputs
      - vel_max_avg/ (output files from v_process.py and used as input for GP_regression.py, contains v_all.nc within corresponding folders for inp conditions) 
  - blob2d.cxx (source file for blob2d model)

Created 30/03/2025
