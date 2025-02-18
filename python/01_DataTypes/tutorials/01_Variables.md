# 01_01 Variables

## Data Types in Python

The heart of programming is reading and writing data from memory.

In Python, as in other programming languages, we can use a concept known as _variables_ to store data in our program's memory.

Variables we store are assoicated with a _data type_. Here are some basic data types that Python provides for us:

| Data Type | Descriptive Name | Description | Examples |
| --- | --- | --- | --- |
| `int` | Integer | Whole numbers, positive or negative | `24`, `0`, `-132` |
| `str` | String | A string of characters, representing literal text. Strings in Python can be represented with either double quotes or single quotes | `"Hello, World"`, `""` (empty string), `'spam and eggs'` |
| `float` | Float | A floating-point number, meaning a number with a decimal point | `3.1415`, `0.0`, `-12.352` |
| `bool` | Boolean | A true or false value | `True`, `False` |

There are more native data types in Python not listed here, but we'll cover them later.

## Variables and the REPL

We can declare a variable with a given value using the below syntax:

```python
<name> = <value>
```

For example:

```python
x = 12
my_name = "John Doe"
```

Notice how we declared the variables (an `int` and a `str`) without explicitly stating the data type?

This is due to a feature of Python called _type inference_.

The Python interpreter is smart enough to know the data type of our variable based on its value.

We can verify this by using another Python _built-in_ function, `type`.

To demonstrate this, let's get familiar with another helpful Python tool, the _REPL_. The _REPL_ allows us to execute Python statements line-by-line.

We can start the Python REPL by simply typing the `python3` command in a terminal:

```bash
$ python3
Python 3.12.0 (default, Aug  9 2024, 14:24:13) 
[Clang 16.0.0 (clang-1600.0.26.3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Now let's declare a variable in the REPL:

```python3
>>> x = 5
>>>
```

And we can verify that `x` is indeed an integer by calling the `type` function on `x`:

```python3
>>> type(x)
<class 'int'>
```

We'll talk about classes in a later section, but we can see how the Python interpreter knew `x` was an `int` just from its value, without us explicitly saying that `x` is an integer.

## Printing Variables

We can print the value of variables by just using the `print` function that we did in the first section:

```python
x = 5
print(x)
```

Try this out in the REPL, or in your own `.py` file.

Notice that `x` in this case does _not_ have quotes around it! Try this snippet for yourself and you'll see the difference:

```python
x = 5
print(x)
print("x")
```

## Conclusion

That's going to conclude this tutorial! We covered:

- Different data types in Python
- Declaring variables
- Printing variables
- The `type` function
- The Python REPL

Continue to the next tutorial to learn an extremely important concept, the Symbol Table.
