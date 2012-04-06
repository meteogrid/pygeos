from setuptools import setup, find_packages

version = '1.4'

setup(
    name = 'pygeos',
    version = version,
    description = "A fork of django.contrib.gis.geos to make it easily usable without Django",
    long_description="""\
    """,
    classifiers = [],
    keywords = '',
    author = 'Alberto Valverde Gonzalez (original code by Justin Bronn and contributors.)',
    author_email = 'alberto@meteogrid.com',
    license = 'BSD',
    packages = ['_geos_gdal', '_geos_gdal.prototypes', '_geos_gdal.tests',
                '_geos_geometry',
                'geos', 'geos.prototypes', 'geos.tests'],
    # Avoid conflict with osgeo.gdal
    package_dir = {'_geos_gdal':'gdal',
                   '_geos_geometry': 'geometry'},
    zip_safe = True,
    test_suite="tests.suite",
)
