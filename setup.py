from setuptools import setup

setup(name='tail2kafka',
      version='0.1',
      author='TBD',
      author_email='TBD',
      url='https://github.com/mmlac/tail2kafka',
      py_modules=['tail2kafka'],
      package_dir={'': 'tail2kafka'},
      scripts=['bin/tail2kafka'],
      install_requires=['kafka-python==0.9.2']
      )
