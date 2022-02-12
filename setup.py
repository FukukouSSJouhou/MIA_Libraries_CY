from Cython.Build import cythonize
from setuptools import setup, find_packages
from setuptools.extension import Extension

setup(
    name='mia_libraries_cy',
    version='0.0.1',
    license='MIT',
    description='mia_libraries_cy',
    author='fukukoussjouhou',
    author_email='umekoujouhouhan@gmail.com',
    url='None.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    ext_modules=cythonize([
        Extension(
            "MIA_Libraries_CY.KyokoLoggingkun",
            sources=["src/MIA_Libraries_CY/KyokoLoggingkun.pyx"]
        )
    ])
)
