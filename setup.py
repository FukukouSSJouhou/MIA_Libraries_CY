from Cython.Build import cythonize
from setuptools import setup, find_packages
from setuptools.extension import Extension


def _requires_from_file(filename):
    return open(filename).read().splitlines()
setup(
    name='mia_libraries_cy',
    version='0.0.0.2',
    license='MIT',
    description='mia_libraries_cy',
    author='fukukoussjouhou',
    author_email='umekoujouhouhan@gmail.com',
    url='None.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    setup_requires=["Cython"],
    install_requires=_requires_from_file('requirements.txt'),
    ext_modules=cythonize([
        Extension(
            "MIA_Libraries_CY.KyokoLoggingkun",
            sources=["src/MIA_Libraries_CY/KyokoLoggingkun.pyx"]
        ),

        Extension(
            "MIA_Libraries_CY.Face_Process",
            sources=["src/MIA_Libraries_CY/Face_Process.pyx"]
        ),
        Extension(
            "MIA_Libraries_CY.FACEmod",
            sources=["src/MIA_Libraries_CY/FACEmod.pyx"]
        )
    ],compiler_directives={'language_level' : "3"})
)
