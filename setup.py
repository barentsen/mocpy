#!/usr/bin/env python

from distutils.core import setup

version = '0.1.5'

setup(name='MOCPy',
      version=version,
      description='MOC parsing and manipulation in Python',
      author='Thomas Boch',
      author_email='thomas.boch@astro.unistra.fr',
      license='GPL v3',
      url='https://github.com/tboch/mocpy',
      packages=['mocpy'],
      #package_data={'mocpy.tests':['data/*.fits']},
      requires=['astropy', 'numpy', 'matplotlib'],
      provides=['mocpy'],
      long_description="MOCPy is a Python library allowing easy creation and manipulation of MOCs (Multi-Order Coverage maps).MOC is an `IVOA standard <http://ivoa.net/documents/MOC/>` enabling description of arbitrary sky regions. Based on the HEALPix sky tessellation, it maps regions on the sky into hierarchically grouped predefined cells.",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Topic :: Scientific/Engineering :: Astronomy',
      ],
      )
