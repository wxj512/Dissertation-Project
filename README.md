Repository to version control Dissertation Project progress
- Compiled BOUT++ builds
  - test-build (BOUT++ ver. 5.1.1, default cmake)
  - test-blob2d (BOUT++ ver. 5.1.1, default cmake)
- Project log (latex file, compiled with xelatex in Overleaf)
  - Figs (png for all figure used in project log)
  - References (BibLaTex file)
- Literature review and lay summary (latex file, compiled with xelatex in Overleaf)
  - Figs (png for all figure used in literature review)
  - References (BibLaTex file)
- Miscellaneous files
  - vel_out/ (contains .py file for processing and calculating velocity of blob)
  - model_run/ (contains .py file for creating inp file and for executing blob2d model runs)
    - delta_*/ (input files for v_data.py, contains BOUT.dmp.x.nc, .inp and .setting files)
    - delta_1_B0_*/ (input files for v_data.py, contains BOUT.dmp.x.nc, .inp and .setting files)
  - blob2d.cxx (source file for blob2d model)

Created 30/03/2025
