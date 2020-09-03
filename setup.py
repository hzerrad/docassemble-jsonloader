import os
from distutils.core import setup


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as read_me:
        return read_me.read()


setup(name='docassemble-jsonloader',
      version='0.0.1',
      description="Python interface to the Firebase's REST API.",
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Legal Industry',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Natural Language :: English',
      ],
      keywords='docassemble python json',
      author='Houssem Eddine Zerrad',
      author_email='hzerrad96@gmail.com',
      maintainer='Houssem Eddine Zerrad',
      maintainer_email='hzerrad96@gmail.com',
      url='https://github.com/hzerrad/docassemble-jsonloader',
      license='MIT',
      packages=['jsonloader'],
      install_requires=['orjson>=3.0.0'],
      zip_safe=False,
      )
