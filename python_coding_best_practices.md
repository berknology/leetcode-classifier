# Python Coding Best Practices

Coding best practices ensure that your code is readable, maintainable, and scalable. Moreover, following the best 
engineering practices will make your code has less or no bug and streamline the code review process. 
This article summarizes the best practices and conventions of programming in Python.


## Python IDE

PyCharm, Anaconda/Spyder and VS Code are among the most popular IDEs for Python programming. Personally, I use PyCharm 
Professional version since I enjoyed its features such as Docker integration, PEP 8 style checking, Jupyter notebook 
support, interactive Python console, VCS support, test-driving coding support, and database & SQL support, etc. BTW, 
PyCharm Professional version is free for students and open source project contributors.


## Use Docker or virtual environments

Every project should be self-contained. I highly recommend to use Docker to containerize your application, and unify 
your development, test, and production environments. If this is not possible, you should at least create a virtual 
environment for each project. This will avoid any clashes, since different projects may need different versions 
of python or library.


## Architect and Design Mindset

Before we implement anything, it is important to have the architect and design mindset in the first place. 
We need to think about questions like who will use our system or service, how do we use it, how does the component 
to-be-implemented integrate with the rest of the system, how can we make code more modular, do we need a base class, 
what abstract methods do we need to have, how can we make functions as independent and decoupled as possible, what test
cases should I have, what could possibly go wrong with my code, etc. 

**Simplicity, readability, consistency, extensibility, modularity, and scalability** are key factors to consider when 
programming.


## Style Guides

[PEP 8](https://www.python.org/dev/peps/pep-0008/) is the de facto coding style guide for Python.

### Library imports
Importing libraries should be at the top of the file, just after any module comments and docstrings, and before module 
globals and constants. Different modules should be on separate lines, and imports should be grouped in the following 
order and separated by a blank line to make it clear where each module is coming from:

1. Python standard libraries (e.g., os, sys, and time, etc.)
2. Third party libraries (e.g., pandas, numpy, and seaborn, etc.)
3. Self developed modules 

Absolute imports are recommended, and wildcard imports (from <module> import *) should be avoided.

A good example of library imports are shown as below:
```python
import os
import sys

import pandas as pd
import numpy as np

from utils import get_logger, get_config
from foo.bar.your_class import YourClass
```

### Naming conventions

#### Names to avoid

Avoid one-letter variables such as `l`, `O`, `I` since they are indistinguishable from the numerals one and zero in 
some fonts.

#### Package and module names

Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. 
Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

#### Class and exception names

Class and exception/error names should normally use the CapWords convention, e.g., `MyClass`.

#### Function names

Function names should be lowercase, with words separated by underscores if necessary. Additionally, use single leading 
underscore for protected and internal methods (e.g., `_single_leading_underscore(self, ...)`) and double leading 
underscore for private methods (e.g., `__double_leading_underscore(self, ...)`). 

#### Variable names

Variable names follow the same convention as function names.

#### Constants

Constants are usually defined on a module level and written in all capital letters with underscores separating words. 
Examples include `MAX_OVERFLOW` and `TOTAL`.

### Blank lines

* Top-level functions and class definitions should be separated by **two** blank lines.
* Method definitions inside a class should be separated by **one** blank line.
* Blank lines can be used in functions, sparingly, to indicate logical sections.
* The end of a python script should be followed by **one** blank line.

### Python Typing

Although it is not required, having typing for public functions will substantially improve readability and reusability. 
Below is an example of python typing:

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
``` 

Please refer to python [typing](https://docs.python.org/3/library/typing.html) module for various types of typings such 
as `List`, `Tuple`, `Dict`, `Iterable`, `Callable` and `Optional`, etc.

### Docstrings

Please refer to [PEP 257](https://www.python.org/dev/peps/pep-0257/) for docstring guidelines. 
Use one-line docstrings for obvious functions. For example,

```python
"""Return the pathname of ``foo``."""
```

Multiline docstrings should include the following items:
* Summary line
* Use case
* Arguments
* Return type

```python
"""Train a model to classify Foos and Bars.

Usage::

    >>> import klassify
    >>> data = [("green", "foo"), ("orange", "bar")]
    >>> classifier = klassify.train(data)

:param train_data: A list of tuples of the form ``(color, label)``.
:rtype: A :class:`Classifier <Classifier>`
"""
```

### Maximum Line Length

Limit all lines to a maximum of 79 characters (72 for docstrings/comments). 
The preferred way of wrapping long lines is by using Python's implied line continuation inside parentheses, brackets 
and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses. These should be used in 
preference to using a backslash for line continuation.

### Useful Tools

Personally, I recommend to use PyCharm IDE, which will automatically check PEP 8 conventions for your code. Open source 
libraries such as [autopep8](https://github.com/hhatto/autopep8), [pep8](https://github.com/treyhunner/pep8), 
and [flake8](https://gitlab.com/pycqa/flake8) are also very helpful to check if your code follows the PEP 8 best 
practices and conventions.


## Pull Request & Code Review

In reality, few reviewer will spend more than 20 minutes to review your PR or CR. To facilitate the review process, 
make sure your PR or CR focuses on one thing and your commits are small and incremental. To enable this, it is a good 
practice to make your user story or task simple, small, and independent, and connected with the PR or CR. It is also 
helpful to add description, acceptance criteria, and test cases, etc. to facilitate reviewers, scrum master, and testers 
to review and test your code.


## Security

NEVER put passwords, API keys, database connections string or other credentials in your code. Additionally, do not 
commit and push any sensitive data into your repositories. These confidential info will be seen by others when they are 
pushed to your remote repositories. Use online service such as Azure Key Vault and Azure Data Lake or Blob storage 
instead. 


## Testing

It is extremely important to write unit tests for your code. For each function you implement, you should add test cases 
such as edge cases, special cases, normal cases, and any test cases could possibly lead to a bug. Strive for 100% code 
coverage, but don't get obsessed with the coverage score. It is a good practice to make each function independent of 
other functions, and make sure a unit test focuses on one tiny bit of functionality and your tests are isolated. 
Moreover, don't interact with a real database or network. Use a separate in-memory or test database that gets torn down 
or use mock objects. Use mock and patch when you want to control or replace parts of your code under test. Generally, 
each class or model should have one test case class.


## Common mistakes

* Keeping commented code
* Having unused imports
* Inconsistency in naming
* Long and involved function
* Missing whitespace around operator or after comma in arguments, etc.
* Using `print()` in production code
