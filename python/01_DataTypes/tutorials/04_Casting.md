# 01_04 Casting

## A Simple Example

In this example, we've got some information about a user and want to print it nicely to the console:

```python3
# Some sample info about a user account.
username = "johndoe"
account_age_days = 24

# Print the info.
print(username + "'s account is " + account_age_days + " days old")
```

When we run this either in the REPL or from a source file, we might expect the following to be printed:

```
johndoe's account is 24 days old
```

But let's see what happens in practice:

```python3
>>> username = "johndoe"
>>> account_age_days = 24
>>> print(username + "'s account is " + account_age_days + " days old")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Hmm, what did we do wrong here?

Looking at the error message, it mentions that we can only concatenate a `str` to a `str`.

And this makes sense! We saw this in the last tutorial on using arithmetic operations on strings. When we use the `+` operator on 2 strings, it concatenates them together to form a single, combined string.

But here, we're trying to concatenate an `int`, in this case `24`, with a `str`, and Python tells us that it can't do this.

So how can we fix this? Enter a new concept called _casting_.

## What is Casting?

Casting is simply _changing_ a variable from one data type to another. That's all there is to it.

In our above example, in order to successfully perform concatenation, we have to change our `account_age_days` variable, which is an `int`, to a `str` so that it can be combined with the string in our print statement.

The way we do that, is simply by using the data type name, in this case `str`, as a function on our data.

Take a look at this in practice:

```python3
account_age_days = 24

# Create a new variable, which is our account_age_days casted to a str.
account_age_str = str(account_age_days)
```

In this snippet, we invoked the `str` function by saying `str(account_age_days)`, which produces a string version of our `account_age_days` variable, and we save it in a _new_ variable called `account_age_str`.

Let's look at the symbol table to ensure we understand what's happening behind the scenes:

| Symbol | Data Type | Value |
| --- | --- | --- |
| account_age_days | `int` | `24` |
| account_age_str | `str` | `"24"` |

## Fixing the Code

So let's put casting into practice by fixing our code snippet from earlier:

```python3
# Some sample info about a user account.
username = "johndoe"
account_age_days = 24

# Print the info. Make sure we cast!
print(username + "'s account is " + str(account_age_days) + " days old")
```

And now we get the output we expect:

```python3
>>> print(username + "'s account is " + str(account_age_days) + " days old")
johndoe's account is 24 days old
```

Python is now able to perform concatenation using the `+` operator, since both sides of the operator are `str` now!

## Extrapolating

Casting can be used to convert variables of any kind to any kind, as long as Python has a built-in knowledge of how to convert it.

Let's take a look at a few examples. We'll put the symbol table after each one.

### Cast int to float

```python3
# Cast an integer to a float.
my_int = 24
my_float = float(my_int)
```

| Symbol | Data Type | Value |
| --- | --- | --- |
| my_int | `int` | `24` |
| my_float | `float` | `24.0` |

### Cast float to int

```python3
# Cast a float to an integer. This always rounds the decimal down.
my_float = 24.9
my_int = int(my_float)
```

| Symbol | Data Type | Value |
| --- | --- | --- |
| my_float | `float` | `24.9` |
| my_int | `int` | `24` |

See how `24.9` was rounded down to `24`, instead of up to `25`? It simply shaves the decimals off, instead of rounding to the nearest whole number.

This behavior is defined in the internals of Python.

### Casting str to int

```python3
my_str = "245"
my_int = int(my_str)
```

| Symbol | Data Type | Value |
| --- | --- | --- |
| my_str | `str` | `"245"` |
| my_int | `int` | `245` |

Converting a `str` to an `int` is not guaranteed to succeed!

Try running the following in the REPL:

```python3
my_str = "245a"
my_int = int(my_str)
```

What happens? Is this what you'd expect?

### Casting to the Same Variable

In the previous examples, we created a new variable with the casted result. But we can also perform casting by modifying the existing variable:

```python3
my_var = 24
my_var = float(my_var)
```

In this case, we save the casted result to the same variable, effectively overwriting the entry in the symbol table.

Let's take a look at the symbol table as we go.

The first line is executed, and we save it to the table:

| Symbol | Data Type | Value |
| --- | --- | --- |
| my_var | `int` | `24` |

Then, when we perform the cast, it sees `my_var` already exists in the table, so it overwrites the entry:

| Symbol | Data Type | Value |
| --- | --- | --- |
| my_var | `float` | `24.0` |

So we've effectively performed a cast in-place.

There's no right or wrong way to perform casting. This tutorial aims to show a few different ways you might approach a problem that requires it.

## Exercises

Try out `exercise_c.py` to get some practice in using casting.
