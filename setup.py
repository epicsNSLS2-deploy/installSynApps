import setuptools

with open('requirements.txt') as reqf:
    requirements = reqf.readlines()

with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name='installSynApps',
    description='A Python program for building EPICS and synApps',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.2.5',
    author='Jakub Wlodek',
    author_email='jwlodek@bnl.gov',
    license='BSD (3-clause)',
    url='https://github.com/epicsNSLS2-deploy/installSynApps',
    packages=setuptools.find_packages(exclude=['tests', 'docs']),
    py_modules=['installCLI', 'installGUI'],
    python_requires='>=3.4',
    install_requires=requirements,
    keywords='epics install build deploy scripting automation',
    entry_points={
        'console_scripts': [
            'installEPICS = installCLI:main',
            'installEPICSGUI = installGUI:main',
        ],
    },
    extras_require={
        'test': ['pytest'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
