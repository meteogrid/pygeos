from unittest import TestSuite
from geos.tests import suite as geos_suite
from _geos_gdal.tests import suite as gdal_suite

test_suites = [
    geos_suite(),
    gdal_suite(),
    ]

def suite():
    "Builds a test suite for the GEOS and gdal tests."
    s = TestSuite()
    map(s.addTest, test_suites)
    return s
