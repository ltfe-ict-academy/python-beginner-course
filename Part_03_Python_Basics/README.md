# Python Basics

## Basic Data Types
- [Basic Data Types in Python: A Quick Exploration](https://realpython.com/python-data-types/)

Python has several built-in data types that you can use out of the box because they’re built into the language. From all the built-in types available, you’ll find that a few of them represent basic objects, such as numbers, strings and characters, bytes, and Boolean values.

In Python, the built-in data types that you can consider basic are the following:

<div>
<table>
<thead>
<tr>
<th>Class</th>
<th>Basic Type</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>int</code></td>
<td>Integer numbers</td>
</tr>
<tr>
<td><code>float</code></td>
<td>Floating-point numbers</td>
</tr>
<tr>
<td><code>complex</code></td>
<td>Complex numbers</td>
</tr>
<tr>
<td><code>str</code></td>
<td>Strings and characters</td>
</tr>
<tr>
<td><code>bytes</code>, <code>bytearray</code></td>
<td>Bytes</td>
</tr>
<tr>
<td><code>bool</code></td>
<td>Boolean values</td>
</tr>
</tbody>
</table>
</div>


### Integers

Integer numbers are whole numbers with no decimal places. They can be positive or negative numbers. For example, 0, 1, 2, 3, -1, -2, and -3 are all integers. In Python, the integer data type is represented by the `int` class.

> Python has no limit to how long an integer value can be. The only constraint is the amount of memory your system has.

When you’re working with long integers, you can use the underscore character to make the literals more readable:
```python
# Example of using underscores in integer literals
population = 1_400_000_000  # Represents 1.4 billion
```

### Floating-point numbers

The float type in Python designates floating-point numbers. To create these types of numbers, you can also use literals, similar to what you use in math. However, in Python, the dot character (`.`) is what you must use to create floating-point literals.

### Strings

In Python, strings are sequences of character data that you can use to represent and store textual data. The string type in Python is called str:
```python
# Example of a string in Python
greeting = "Hello, World!"
print(greeting)  # Output: Hello, World!
```

To build a single-line string literal, you can use double ("") or single quotes ('') and, optionally, a sequence of characters in between them. All the characters between the opening and closing quotes are part of the string:
```python
# Example of single-line string literals
single_quote_string = 'This is a string with single quotes.'
double_quote_string = "This is a string with double quotes."
```

There is yet another way to delimit strings in Python. You can create triple-quoted string literals, which can be delimited using either three single quotes or three double quotes. Triple-quoted strings are commonly used to build multiline string literals. However, you can also use them to create single-line literals:

```python
# Example of triple-quoted string literals
triple_single_quote_string = '''This is a string
that spans multiple lines.'''
triple_double_quote_string = """This is also a string
that spans multiple lines."""
```

### Boolean values

Boolean logic relies on the truth value of expressions and objects. The truth value of an expression or object can take one of two possible values: true or false. In Python, these two values are represented by `True` and `False`, respectively.

### Type function

The `type()` function is used to determine the type of an object. It returns the type of the object passed to it as an argument.

```python
# Example usage of the type() function
print(type(5))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type("Hello, World!"))  # Output: <class 'str'>
```
### Build in functions for type conversion

Python provides several built-in functions for type conversion. Here are some of the most commonly used ones:

- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a floating-point number.
- `str()`: Converts a value to a string.
- `bool()`: Converts a value to a boolean.

```python
# Example usage of type conversion functions
# Convert float to int
print(int(3.14))  # Output: 3

# Convert int to float
print(float(5))  # Output: 5.0

# Convert string to int
print(int("10"))  # Output: 10

# Convert int to string
print(str(5))  # Output: "5"

# Convert float to string
print(str(3.14))  # Output: "3.14"

# Convert string to boolean
print(bool(""))  # Output: False
print(bool("Hello"))  # Output: True
```

> When you use the int() function to convert floating-point numbers, you must be aware that the function just removes the decimal or fractional part.

## Printing to the Console
- [Your Guide to the Python print() Function](https://realpython.com/python-print/)

In Python, you can print output to the console using the built-in `print()` function. The `print()` function takes one or more arguments and displays them as text in the console.

## Variables
- [Variables in Python: Usage and Best Practices](https://realpython.com/python-variables/)

In Python, variables are symbolic names that refer to objects or values stored in your computer’s memory. They allow you to assign descriptive names to data, making it easier to manipulate and reuse values throughout your code. You create a Python variable by assigning a value using the syntax `variable_name = value`.

Overview:
- Variables in Python are **symbolic names pointing to objects or values in memory**.
- You define variables by assigning them a value using the **assignment operator**.
- Python variables are **dynamically typed**, allowing type changes through reassignment.
- Python variable names can include letters, digits, and underscores but can’t start with a digit. You should use **snake case** for multi-word names to improve readability.
- Variables are **case-sensitive**. Lowercase and uppercase letters aren’t treated the same.
- Variables exist in **different scopes** (global, local, non-local, or built-in), which affects how you can access them.
- You can have an **unlimited number of variables** in Python, limited only by computer memory.

> You should always give a variable a descriptive name that clearly explains the variable’s purpose.

## Getting values from users
- [Basic Input and Output in Python](https://realpython.com/python-input-output/)

For a program to be useful, it often needs to communicate with the outside world. In Python, the input() function allows you to capture user input from the keyboard.

Programs often need to obtain data from users, typically through keyboard input. In Python, one way to collect user input from the keyboard is by calling the input() function:
```python
user_input = input("Please enter something: ")
print("You entered:", user_input)
```

The input() function always reads the user’s input as a string. Even if you type characters that resemble numbers, Python will still treat them as a string:
```python
age = input("Please enter your age: ")
print("Your age is:", age)
print("Type of age variable:", type(age))  # Output: <class 'str'>
```

> When you convert user input to a numeric type using functions like int() in a real-world scenario, it’s crucial to handle potential exceptions to prevent your program from crashing due to invalid input.

## Operators and Expressions
- [Operators and Expressions in Python](https://realpython.com/python-operators-expressions)

Python operators enable you to perform computations by combining objects and operators into expressions. Understanding Python operators is essential for manipulating data effectively.

Type of operators in Python:
- **Arithmetic operators** perform mathematical calculations on numeric values.
- **Comparison operators** evaluate relationships between values, returning Boolean results.
- **Boolean operators** create compound logical expressions.
- **Identity operators** determine if two operands refer to the same object.
- **Membership operators** check for the presence of a value in a container.

An **expression** is a simple statement that produces and returns a value. A simple statement is a construct that occupies a single logical line, like an assignment statement.

### Arithmetic Operators and Expressions

Arithmetic operators are those operators that allow you to perform arithmetic operations on numeric values.

<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr>
<th class="text-center">Operator</th>
<th>Type</th>
<th>Operation</th>
<th class="text-center">Sample Expression</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td class="text-center"><code>+</code></td>
<td>Unary</td>
<td>Positive</td>
<td class="text-center"><code>+a</code></td>
<td><code>a</code> without any transformation since this is simply a complement to negation</td>
</tr>
<tr>
<td class="text-center"><code>+</code></td>
<td>Binary</td>
<td>Addition</td>
<td class="text-center"><code>a + b</code></td>
<td>The arithmetic sum of <code>a</code> and <code>b</code></td>
</tr>
<tr>
<td class="text-center"><code>-</code></td>
<td>Unary</td>
<td>Negation</td>
<td class="text-center"><code>-a</code></td>
<td>The value of <code>a</code> but with the opposite sign</td>
</tr>
<tr>
<td class="text-center"><code>-</code></td>
<td>Binary</td>
<td>Subtraction</td>
<td class="text-center"><code>a - b</code></td>
<td><code>b</code> subtracted from <code>a</code></td>
</tr>
<tr>
<td class="text-center"><code>*</code></td>
<td>Binary</td>
<td>Multiplication</td>
<td class="text-center"><code>a * b</code></td>
<td>The product of <code>a</code> and <code>b</code></td>
</tr>
<tr>
<td class="text-center"><code>/</code></td>
<td>Binary</td>
<td>Division</td>
<td class="text-center"><code>a / b</code></td>
<td>The quotient of <code>a</code> divided by <code>b</code>, expressed as a float</td>
</tr>
<tr>
<td class="text-center"><code>%</code></td>
<td>Binary</td>
<td>Modulo</td>
<td class="text-center"><code>a % b</code></td>
<td>The remainder of <code>a</code> divided by <code>b</code></td>
</tr>
<tr>
<td class="text-center"><code>//</code></td>
<td>Binary</td>
<td>Floor division or integer division</td>
<td class="text-center"><code>a // b</code></td>
<td>The quotient of <code>a</code> divided by <code>b</code>, rounded to the next smallest whole number</td>
</tr>
<tr>
<td class="text-center"><code>**</code></td>
<td>Binary</td>
<td>Exponentiation</td>
<td class="text-center"><code>a**b</code></td>
<td><code>a</code> raised to the power of <code>b</code></td>
</tr>
</tbody>
</table>
</div>

### Comparison Operators and Expressions

The Python comparison operators allow you to compare numerical values and any other objects that support them. The table below lists all the currently available comparison operators in Python:

<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr>
<th class="text-center">Operator</th>
<th>Operation</th>
<th class="text-center">Sample Expression</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td class="text-center"><code>==</code></td>
<td>Equal to</td>
<td class="text-center"><code>a == b</code></td>
<td>• <code>True</code> if the value of <code>a</code> is equal to the value of <code>b</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td class="text-center"><code>!=</code></td>
<td>Not equal to</td>
<td class="text-center"><code>a != b</code></td>
<td>• <code>True</code> if <code>a</code> isn’t equal to <code>b</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td class="text-center"><code>&lt;</code></td>
<td>Less than</td>
<td class="text-center"><code>a &lt; b</code></td>
<td>• <code>True</code> if <code>a</code> is less than <code>b</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td class="text-center"><code>&lt;=</code></td>
<td>Less than or equal to</td>
<td class="text-center"><code>a &lt;= b</code></td>
<td>• <code>True</code> if <code>a</code> is less than or equal to <code>b</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td class="text-center"><code>&gt;</code></td>
<td>Greater than</td>
<td class="text-center"><code>a &gt; b</code></td>
<td>• <code>True</code> if <code>a</code> is greater than <code>b</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td class="text-center"><code>&gt;=</code></td>
<td>Greater than or equal to</td>
<td class="text-center"><code>a &gt;= b</code></td>
<td>• <code>True</code> if <code>a</code> is greater than or equal to <code>b</code><br>• <code>False</code> otherwise</td>
</tr>
</tbody>
</table>
</div>


### Boolean Operators and Expressions

Python has three Boolean or logical operators: and, or, and not. They define a set of operations denoted by the generic operators AND, OR, and NOT. With these operators, you can create compound conditions.

<table class="table table-hover">
<thead>
<tr>
<th>Operator</th>
<th>Sample Expression</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>and</code></td>
<td><code>x and y</code></td>
<td>• <code>True</code> if both <code>x</code> and <code>y</code> are <code>True</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td><code>or</code></td>
<td><code>x or y</code></td>
<td>• <code>True</code> if either <code>x</code> or <code>y</code> is <code>True</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td><code>not</code></td>
<td><code>not x</code></td>
<td>• <code>True</code> if <code>x</code> is <code>False</code><br>• <code>False</code> if <code>x</code> is <code>True</code></td>
</tr>
</tbody>
</table>

### Identity Operators and Expressions
- [Python != Is Not is not: Comparing Objects in Python](https://realpython.com/python-is-identity-vs-equality/)

Python provides two operators, is and is not, that allow you to determine whether two operands have the same identity. In other words, they let you check if the operands refer to the same object. Note that identity isn’t the same thing as equality. The latter aims to check whether two operands contain the same data.

<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr>
<th>Operator</th>
<th>Sample Expression</th>
<th>Result</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://docs.python.org/3/reference/expressions.html#is"><code>is</code></a></td>
<td><code>x is y</code></td>
<td>• <code>True</code> if <code>x</code> and <code>y</code> hold a reference to the same in-memory object<br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td><a href="https://docs.python.org/3/reference/expressions.html#is-not"><code>is not</code></a></td>
<td><code>x is not y</code></td>
<td>• <code>True</code> if <code>x</code> points to an object different from the object that <code>y</code> points to<br>• <code>False</code> otherwise</td>
</tr>
</tbody>
</table>
</div>

These two Python operators are keywords instead of odd symbols. This is part of Python’s goal of favoring readability in its syntax.

Here’s an example of two variables, x and y, that refer to objects that are equal but not identical:
```python
x = 1001
y = 1001

print(x == y)      # Output: True (x and y are equal)
print(x is y)     # Output: False (x and y are not identical)
```

In this example, x and y refer to objects whose value is 1001. So, they’re equal. However, they don’t reference the same object. That’s why the is operator returns False. You can check an object’s identity using the built-in `id()` function:

```python
x = 1001
y = 1001
print(id(x))  # Output: e.g., 140123456789456
print(id(y))  # Output: e.g., 140123456789488
```

As you can conclude from the `id()` output, x and y don’t have the same identity. So, they’re different objects, and because of that, the expression x is y returns False. In other words, you get False because you have two different instances of 1001 stored in your computer’s memory.

When you make an assignment like y = x, Python creates a second reference to the same object. Again, you can confirm that with the `id()` function or the is operator:
```python
a = "Hello"
b = a # b now references the same object as a

print(a is b)  # Output: True (a and b are identical)

print(id(a))   # Output: e.g., 140123456789456
print(id(b))   # Output: e.g., 140123456789456
```

### Membership Operators and Expressions

Sometimes you need to determine whether a value is present in a container data type. In other words, you may need to check if a given value is or is not a member of a collection of values.

<div class="table-responsive">
<table class="table table-hover">
<thead>
<tr>
<th class="text-left">Operator</th>
<th>Sample Expression</th>
<th class="text-left">Result</th>
</tr>
</thead>
<tbody>
<tr>
<td class="text-left"><code>in</code></td>
<td><code>value in collection</code></td>
<td class="text-left">• <code>True</code> if <code>value</code> <em>is</em> present in <code>collection</code><br>• <code>False</code> otherwise</td>
</tr>
<tr>
<td class="text-left"><code>not in</code></td>
<td><code>value not in collection</code></td>
<td class="text-left">• <code>True</code> if <code>value</code> <em>is not</em> present in <code>collection</code> of values<br>• <code>False</code> otherwise</td>
</tr>
</tbody>
</table>
</div>

As usual, Python favors readability by using English words as operators instead of potentially confusing symbols or combinations of symbols.

## String formatting
- [Python String Formatting: Available Tools and Their Features](https://realpython.com/python-string-formatting/)
- [String Interpolation in Python: Exploring Available Tools](https://realpython.com/python-string-interpolation/)

String interpolation involves generating strings by inserting other strings or objects into specific places in a base string or template. 

When you do string interpolation, you may need to format the interpolated values to produce a well-formatted final string. To do this, you can use different string interpolation tools that support string formatting. In Python, you have these four tools:
- F-strings
- The str.format() method
- The modulo operator (%)
- Template Strings (T-Strings) - new in Python 3.14!

Python 3.6 added a string interpolation and formatting tool called formatted string literals, or f-strings for short. To create an f-string, you must prefix the string with an f or F and insert replacement fields in the string literal. Each replacement field must contain a variable, object, or expression:
```python
name = "Alice"
age = 30

greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.
```
