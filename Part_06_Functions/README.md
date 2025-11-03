# Functions

## Defining and Calling Functions
- [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/#calling-functions-in-python)
- [The Python return Statement: Usage and Best Practices](https://realpython.com/python-return-statement/#returning-multiple-values)

A Python function is a named block of code that performs specific tasks and can be reused in other parts of your code. Python has several built-in functions that are always available, and you can also create your own. These are known as user-defined functions.

To define a function in Python, you use the def keyword, followed by the function name and an optional list of parameters enclosed in a required pair of parentheses. You can call and reuse a function by using its name, a pair of parentheses, and the necessary arguments.

## Optional Arguments
- [Using Python Optional Arguments When Defining Functions](https://realpython.com/python-optional-arguments/)

You define Python functions with optional arguments to make them flexible and reusable. By assigning default values, using *args for variable arguments, or **kwargs for keyword arguments, you let your functions handle different inputs without rewriting code.

## Built-in Functions
- [Python's Built-in Functions: A Complete Exploration](https://realpython.com/python-built-in-functions/)

Python has many built-in functions that you can use directly without importing anything. These functions cover a wide variety of common programming tasks that include performing math operations, working with built-in data types, processing iterables of data, handling input and output in your programs, working with scopes, and more.

## Scopes and Namespaces
- [Python Scope and the LEGB Rule: Resolving Names in Your Code](https://realpython.com/python-scope-legb-rule/#understanding-the-concept-of-scope)
- [Namespaces in Python](https://realpython.com/python-namespace/)

The scope of a variable in Python determines where in your code that variable is visible and accessible. Python has four general scope levels: local, enclosing, global, and built-in. When searching for a name, Python goes through these scopes in order. It follows the LEGB rule, which stands for Local, Enclosing, Global, and Built-in.

Understanding how Python manages the scope of variables and names is a fundamental skill for you as a Python developer. It helps you avoid unexpected behavior and errors related to name collisions or referencing the wrong variable.

## Type Checking
- [Python Type Checking (Guide)](https://realpython.com/python-type-checking/#type-theory)

In Python, a type hint is a syntactic construct that allows you to indicate the expected data types of variables, function arguments, and return values. They provide a way to improve your code’s maintainability by explicitly declaring the data type of variables, arguments, and return values.

Python doesn’t enforce type hints at runtime, but static type checkers, like mypy, can use them to detect potential type errors in your code before you run it.

Using type hints, you also create self-documented code, making it more clear for you and others to understand how to use functions and classes correctly.

## Lambda Functions
- [How to Use Python Lambda Functions](https://realpython.com/python-lambda/)

Python and other languages like Java, C#, and even C++ have had lambda functions added to their syntax, whereas languages like LISP or the ML family of languages, Haskell, OCaml, and F#, use lambdas as a core concept.

Python lambdas are little, anonymous functions, subject to a more restrictive but more concise syntax than regular Python functions.
