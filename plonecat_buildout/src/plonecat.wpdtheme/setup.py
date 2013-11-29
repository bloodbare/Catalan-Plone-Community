from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='plonecat.wpdtheme',
      version=version,
      description="Plone.Cat WPD Theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Iskra Desenvolupament SCCL',
      author_email='info@iskra.cat',
      url='http://github.com/bloodbare/Catalan-Plone_Community',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonecat'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
