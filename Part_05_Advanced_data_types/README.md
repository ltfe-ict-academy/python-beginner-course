## Advanced Data Types

## Lists
- [Python's list Data Type: A Deep Dive With Examples](https://realpython.com/python-list/)

The list class is a fundamental built-in data type in Python. It has an impressive and useful set of features, allowing you to efficiently organize and manipulate heterogeneous data.

Some of the more relevant characteristics of list objects include being:
- **Ordered**: They contain elements or items that are sequentially arranged according to their specific insertion order.
- ***Zero-based**: They allow you to access their elements by indices that start from zero.
- **Mutable**: They support in-place mutations or changes to their contained elements.
- **Heterogeneous**: They can store objects of different types.
- **Growable and dynamic**: They can grow or shrink dynamically, which means that they support the addition, insertion, and removal of elements.
- **Nestable**: They can contain other lists, so you can have lists of lists.
- **Iterable**: They support iteration, so you can traverse them using a loop or comprehension while you perform operations on each of their elements.
- **Sliceable**: They support slicing operations, meaning that you can extract a series of elements from them.
- **Combinable**: They support concatenation operations, so you can combine two or more lists using the concatenation operators.
- **Copyable**: They allow you to make copies of their content using various techniques.

## Tuples
- [Python's tuple Data Type: A Deep Dive With Examples](https://realpython.com/python-tuple/)

In Python, a tuple is a built-in data type that allows you to create immutable sequences of values. The values or items in a tuple can be of any type. This makes tuples pretty useful in those situations where you need to store heterogeneous data, like that in a database record, for example.

Some of the most relevant characteristics of tuple objects include the following:
- **Ordered**: They contain elements that are sequentially arranged according to their specific insertion order.
- **Lightweight**: They consume relatively small amounts of memory compared to other sequences like lists.
- **Indexable through a zero-based index**: They allow you to access their elements by integer indices that start from zero.
- **Immutable**: They don’t support in-place mutations or changes to their contained elements. They don’t support growing or shrinking operations.
- **Heterogeneous**: They can store objects of different data types and domains, including mutable objects.
- **Nestable**: They can contain other tuples, so you can have tuples of tuples.
- **Iterable**: They support iteration, so you can traverse them using a loop or comprehension while you perform operations with each of their elements.
- **Sliceable**: They support slicing operations, meaning that you can extract a series of elements from a tuple.
- **Combinable**: They support concatenation operations, so you can combine two or more tuples using the concatenation operators, which creates a new tuple.
- **Hashable**: They can work as keys in dictionaries when all the tuple items are immutable.

## Sets
- [Sets in Python](https://realpython.com/python-sets/)

Python provides a built-in set data type. It differs from other built-in data types in that it’s an unordered collection of unique elements. It also supports operations that differ from those of other data types.

In this definition, the qualifiers mean the following:
- **Mutable**: You can add or remove elements from an existing set.
- **Unordered**: A set doesn’t maintain any particular order of its elements.
- **Unique elements**: Duplicate elements aren’t allowed.
- **Hashable elements**: Each element must have a hash value that stays the same for its entire lifetime.

## Dictionaries
- [Dictionaries in Python](https://realpython.com/python-dicts/)

Python dictionaries are a powerful built-in data type that allows you to store key-value pairs for efficient data retrieval and manipulation. Learning about them is essential for developers who want to process data efficiently.

Python’s dictionaries have the following characteristics:
- **Mutable**: The dictionary values can be updated in place.
- **Dynamic**: Dictionaries can grow and shrink as needed.
- **Efficient**: They’re implemented as hash tables, which allows for fast key lookup.
- **Ordered**: Starting with Python 3.7, dictionaries keep their items in the same order they were inserted.

The keys of a dictionary have a couple of restrictions. They need to be:
- **Hashable**: This means that you can’t use unhashable objects like lists as dictionary keys.
- **Unique**: This means that your dictionaries won’t have duplicate keys.

## Strings Advanced
- [Strings and Character Data in Python](https://realpython.com/python-strings/)

Python strings are a sequence of characters used for handling textual data. You can create strings in Python using quotation marks or the str() function, which converts objects into strings. Strings in Python are immutable, meaning once you define a string, you can’t change it.

## Iterators and Iterables
- [Iterators and Iterables in Python: Run Efficient Iterations](https://realpython.com/python-iterators-iterables/#understanding-some-constraints-of-python-iterators)

Understanding iterators and iterables in Python is crucial for running efficient iterations. Iterators control loops, allowing you to traverse arbitrary data containers one item at a time. Iterables, on the other hand, provide the data that you want to iterate over. 

In Python, an iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets.

## For loops
- [Python for Loops: The Pythonic Way](https://realpython.com/python-for-loop/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-while-loop)

Python’s for loop allows you to iterate over the items in a collection, such as lists, tuples, strings, and dictionaries. The for loop syntax declares a loop variable that takes each item from the collection in each iteration. This loop is ideal for repeatedly executing a block of code on each item in the collection. You can also tweak for loops further with features like break, continue, and else.

In Python, for loops are compound statements with a header and a code block that runs a predefined number of times. The basic syntax of a for loop is shown below:
```python
for loop_variable in collection:
    # code block to be executed
```

- Range Function

## Data Manipulation Examples

- Copying Data Structures (Deep vs Shallow)
- Sorting Data Structures
- Append vs. Concatenate
- Flattening Nested Structures
- Enumerate Function
- del Statement
- len Function
- Comprehensions

### Mutability vs Immutability
- [Python's Mutable vs Immutable Types: What's the Difference?](https://realpython.com/python-mutable-vs-immutable-types/#mutability-vs-immutability)

Python’s mutable objects, such as lists and dictionaries, allow you to change their value or data directly without affecting their identity. In contrast, immutable objects, like tuples and strings, don’t allow in-place modifications. Instead, you’ll need to create new objects of the same type with different values.
- **Immutable Types**: int, float, bool, str, tuple, bytes
- **Mutable Types**: list, dict, set
