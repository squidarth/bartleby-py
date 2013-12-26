from distutils.core import setup

setup(
     name="Bartleby-py",
     version="0.0.2",
     author="Sid Shanker",
     author_email="sid.p.shanker@gmail.com",
     description="Python bindings for Bartleby",
     packages=['bartleby'],
     install_requires=['redis'],
     license='Creative Commons Attribution-Noncommercial-Share Alike license',
     long_description=open("README.md").read(),
)
