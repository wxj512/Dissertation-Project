"""Functions for getting the config used for compiling BOUT++

"""
# Created by cmake
_yesno = {"TRUE": True, "ON": True, "FALSE": False, "OFF": False}

config = {
    "cc": "/usr/bin/cc",
    "cxx": "/usr/bin/c++",
    "ld": "/usr/bin/c++",
    "checks": "2",
    "cflags": " -I${BOUT_INCLUDE_PATH} -I/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/include -fPIC -I${MPARK_VARIANT_INCLUDE_PATH} -I${FMT_INCLUDE_PATH}",
    "libs": "",
    "version": "5.1.2",
    "git": "eae6e9dea74f55565498ee01cfe135351d22210a",
    "idlpath": "",
    "pythonpath": "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/Dissertation_Project/test-build/tools/pylib:/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/tools/pylib",
    "has_netcdf": "ON",
    "has_legacy_netcdf": "OFF",
    "has_pnetcdf": "OFF",
    "has_pvode": "ON",
    "has_cvode": "OFF",
    "has_ida": "OFF",
    "has_lapack": "OFF",
    "has_petsc": "OFF",
    "has_slepc": "OFF",
    "has_mumps": "OFF",
    "has_arkode": "OFF",
    "has_openmp": "OFF",
    "has_nls": "OFF",
    "has_fftw": "ON",
    "petsc_has_sundials": "",
    "metric_type": "2D",
}

for k, v in config.items():
    config[k] = (
        v.replace(
            "${BOUT_INCLUDE_PATH}", "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/include"
        )
        .replace(
            "${MPARK_VARIANT_INCLUDE_PATH}", "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/mpark.variant/include"
        )
        .replace(
            "${FMT_INCLUDE_PATH}", "/mnt/c/Users/enlan/University/York/Dissertation/Repositories/BOUT-dev/externalpackages/fmt/include"
        )
    )


"""Get a dict of the enabled features"""
has = {}
for k in config:
    if k.startswith("has_"):
        has[k[4:]] = _yesno[config[k].upper()]


def isMetric2D():
    """Is the metric 2D?"""
    return config["metric_type"] == "2D"


def isMetric3D():
    """Is the metric 3D?"""
    return config["metric_type"] == "3D"
