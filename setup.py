import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "fastly-python",
	version = "1.0.4",
	author = "Chris Zacharias and Arthur Freyman",
	author_email = "afreyman@spokeo.com",
	description = ("A Python client libary for the Fastly API."),
	license = "BSD",
	keywords = "fastly",
	url = "https://github.com/Spokeo/fastly-python",
	packages=['fastly', 'tests'],
	scripts=['bin/fastly_upload_vcl.py', 'bin/fastly_purge_url.py', 'bin/fastly_tool.py'],
	long_description=read('README.md'),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"License :: OSI Approved :: BSD License",
	],
)
