from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import sys

from os import path
this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, "VERSION"), encoding='utf-8') as version_file:
    version = version_file.read().strip()


with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

class BuildExt(build_ext):
    """A custom build extension for adding compiler-specific options."""
    c_opts = {
        'msvc': ['/EHsc', '/O2', '/std:c++17'],
        'unix': ['-O3', '-std=c++17'],
    }
    l_opts = {
        'msvc': [],
        'unix': [],
    }

    if sys.platform == 'darwin':
        darwin_opts = ['-stdlib=libc++', '-mmacosx-version-min=10.14']
        c_opts['unix'] += darwin_opts
        l_opts['unix'] += darwin_opts

    def build_extensions(self):
        ct = self.compiler.compiler_type
        opts = self.c_opts.get(ct, [])
        link_opts = self.l_opts.get(ct, [])
        if ct == 'unix':
            opts.append('-DVERSION_INFO="%s"' % self.distribution.get_version())
        elif ct == 'msvc':
            opts.append('/DVERSION_INFO=\\"%s\\"' % self.distribution.get_version())
        for ext in self.extensions:
            ext.extra_compile_args = opts
            ext.extra_link_args = link_opts
        build_ext.build_extensions(self)

setup(
    name='rapidfuzz',
    version=version,
    author='Max Bachmann',
    author_email='contact@maxbachmann.de',
    url='https://github.com/rhasspy/rapidfuzz',
    description='rapid fuzzy string matching',
    long_description=long_description,
    long_description_content_type='text/markdown',
    ext_modules = [
		Extension(
			'rapidfuzz.levenshtein',
			['python/src/py_levenshtein.cpp', 'cpp/src/levenshtein.cpp', 'cpp/src/utils.cpp'],
        	include_dirs=["cpp/src"],
        	language='c++',
		),
		Extension(
			'rapidfuzz.fuzz',
			['python/src/py_fuzz.cpp', 'cpp/src/fuzz.cpp', 'cpp/src/levenshtein.cpp', 'cpp/src/utils.cpp'],
        	include_dirs=["cpp/src"],
        	language='c++',
		),
		Extension(
			'rapidfuzz._process',
			['python/src/py_process.cpp', 'cpp/src/process.cpp', 'cpp/src/fuzz.cpp', 'cpp/src/levenshtein.cpp', 'cpp/src/utils.cpp'],
        	include_dirs=["cpp/src"],
        	language='c++',
		),
	],
	cmdclass={'build_ext': BuildExt},
	package_data={'': ['LICENSE', 'VERSION']},
    package_dir={'': 'python/src'},
	packages=['rapidfuzz'],
	include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.5",
)