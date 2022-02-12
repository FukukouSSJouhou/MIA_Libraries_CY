from setuptools import setup, find_packages
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
)
