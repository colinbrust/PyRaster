from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

data_files = [str(x) for x in pathlib.Path(here / 'data').glob('*.tif')]

setup(
    name='PyRaster', 
    version='1.0.0',
    description='Wrapper around Rasterio functions for simple raster processing in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/colinbrust/PyRaster',
    author='Colin Brust',
    author_email='colin.brust@gmail.com',
    keywords='raster, rasterio, simplified',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['rasterio', 'numpy', 'matplotlib'],  # Optional
    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    package_data={
        '': data_files,
    },
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
