# Python - Exceptions :page_with_curl: 0x05-python-exceptions
## About this project:
In this project i learnt znd practiced;
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need #g exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception
## Tasks file description:

  * [0-safe_print_list.py](./0-safe_print_list.py): Python function that prints `x` elements
  of a list on the same line, followed by a new line.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Returns the real nrinted.
  * Without importing modules or using `len()`.

  * [1-safe_print_integer.py](./1-safe_print_integer.py): Python function that prints an integer in `"{:d}".format()` format.
  * The parameter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer),
  `False` otherwise.
  * Without importing modules or using `type()`.

  * [2-safe_print_list_integers.py](./2-safe_print_list_integers.py): Python function that prints the first `x` elements of a list
  that are ollowed by a new line.
  * The parameter `my_list` can contain any type.
  * The parameter `x` represents the number of elements to print - can be
  bigger than the length of `my_list`.
  * Reutnrs the real number of integers printed.
  * Without importing modules or using `len()`.

  * [3-safe_print_division.py](./3-safe_print_division.py): Python function that divides two integers and prints the result using `finally:`.
  * The function assumes that thss, returns the value of the division; otherwise - returns `None`.
  * Without importing modules.

  * [4-list_division.py](./4-list_division.py): Python function that divides two lists element by element.
  * Returns a new list of length `list_length` with all divisions.
  * The lists `my_list_1` and `my_list_2` can contain any type.
  * The parameter `list_length` can be larger than the lengths of either list.
  * If an elementult of the division is `0` and the
  function prints: `division by 0`.
  * If either of `my_list_1` or `my_list_2` are too short, the function prints:
  `out of range`.
  * Without importing modules.

  * [5-raise_exception.py](./5-raise_exception.py): Python function that raises
  a type exception.
  * Without importing modules.

  * [6-raise_exception_msg.py](./6-raise_exception_msg.py): Python function that raises a
  naption with a message.
  * Without importing modules.

  * [100-safe_print_integer_err.py](./100-safe_print_integer_err.py): Python function that
  prints an integer with type-checking in `"{:d}".format())` format.
  * The paramter `value` can be any type.
  * Returns `True` if `value` was printed correctly (ie. was an integer).
  * Otherwisen error to `stderr` and returns `False`.
  * Without importing modules.

  * [101-safe_function.py](./101-safe_function.py): Python function that executes
  a function safely.
  * Thehat the paramter `fct` is always a pointer to a function.
  * Upon success, returns the result of the function.
  * Otherwise, prints an en exception error to `stderr` and returns `None`.

  * [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a
  bytecode provided by Holberton School.

  * [103-python.c](./103-python.c): C funcnformation
  about Python lists, bytes, and float objects.
