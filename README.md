[![CI Workflow](https://github.com/ariannasg/optimizing-python/workflows/CI%20Workflow/badge.svg)](https://github.com/ariannasg/optimizing-python/actions?query=workflow%3A%22CI+Workflow%22)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

# Optimizing Python Code - Course

* [Description](#description)
* [Objectives](#objectives)
* [Local setup](#local-setup)
* [Security](#security)
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

## License
This project is licensed under the terms of the MIT License.
Please see [LICENSE](LICENSE.md) for details.