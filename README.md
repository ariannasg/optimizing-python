[![CI Workflow](https://github.com/ariannasg/optimizing-python/workflows/CI%20Workflow/badge.svg)](https://github.com/ariannasg/optimizing-python/actions?query=workflow%3A%22CI+Workflow%22)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

# Optimizing Python Code - Course

* [Description](#description)
* [Objectives](#objectives)
* [Local setup](#local-setup)
* [Security](#security)
* [Using IPython](#using-ipython)
* [License](#license)

## Description
Understanding how to optimise Python by following the course https://www.linkedin.com/learning/faster-python-code/.

## Objectives
- Rules of optimization
- Measuring time
- Using line_profiler
- Picking the right data structure
- Using the bisect module
- Memory allocation in Python
- Caching, cheating, and parallel computing
- NumPy, Numba, and Cython
- Design and code reviews

## Local setup
- Install python 3: https://www.python.org/downloads/.
- Create and activate a virtual environment, then install project dependencies:
    ```
    python3 -m venv ~/.python-envs/<name>
    source  ~/.python-envs/<name>/bin/activate
    (<name>) ➜  make install
    ```
- Configure the IDE Interpreter to use the virtual environment as project interpreter.
- Setup the run configuration in the IDE if needed: https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html?keymap=secondary_macos.

## Security
Command for running security checks on installed dependencies:
```
make security
```

## Using IPython
This is an example of trying out a timeit calculation using the IPython Notebook. 
To load the code we use the "run" magic method. 
The "-n" tells run not to run the main part of the code, just to load the functions in the file.
```
(optimizing-python) ➜ ipython
Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %run -n src/using_timeit.py                                                                                                                                                                  

In [2]: %timeit use_get('a')                                                                                                                                                                         
206 ns ± 9.75 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

In [3]: %timeit use_catch('a')                                                                                                                                                                       
167 ns ± 5.37 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

## License
This project is licensed under the terms of the MIT License.
Please see [LICENSE](LICENSE.md) for details.