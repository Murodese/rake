#!/Users/zhaoy10/ENV/bin/python

import os
from setuptools import setup,find_packages

README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(name= 'rake',
	version='1.0',
	author ='yilan',
	author_email="zhaoyinlan@live.cn",
	license="MIT",
	keywords="Rapid automatic keywords extraction",
	url="https://github.com/fishkao/rake",
	packages = find_packages(),
	package_data = {'':['*.*'],'rake':['*.*']},
	namespace_packages=['rake'],
	long_description=open(README).read() + "\n\n",
	description = 'Rapid Automatic Keywords Extraction',
	classifiers=[
		"Programming Language :: Python",
		("Topic :: Software Development :: Libraries :: Python Modules"),
	],
    )
