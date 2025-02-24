# 02_01 Boolean Logic

When we initially talked about various data types in the 01_01 tutorial, we mentioned the Boolean data type, which we said can contain a True or False value.

This tutorial aims to dive deeper into the `bool` data type in Python, which will set the stage for talking about a core-concept of any programming language: _Control Flow_.

## First Principles

At its core, all a `bool` is, is a variable that holds a `True` or `False` value. We can assign these variables a value and print them just like we've done in previous chapters:

Fire up the REPL and try this out:

```python3
>>> b = True
>>> print(b)
True
>>> type(b)
<class 'bool'>
```

| Symbol | Data Type | Value |
| --- | --- | --- |
| b | `bool` | `True` |

This code snippet also provides our first exposure to _keywords_ in Python.

We've already seen _built-in functions_ such as `print` and `type`, and now we get introduced to the keywords `True` and `False`.

Keywords are reserved, special words that the Python interpreter recognizes.

Just like the built-in functions, keywords are case-sensitive, so `True` is a keyword, but `true` is not.

We'll be introduced to more keywords in future tutorials, especially the ones in this section on control flow.

## Comparison Operators

Comparison operators are a category of operators the _compare_ two values, and the result is either `True` or `False`

Let's take a look at the comparison operators:

| Operation | Operator | Example | Description |
| --- | --- | --- | --- |
| Equals | `==` | `a == b` | `True` if `a` is equal in value to `b` |
| Not Equals | `!=` | `a != b` | `True` if `a` is _not_ equal in value to `b` |
| Greater Than | `>` | `a > b` | `True` if `a` is greater in value to `b` |
| Less Than | `<` | `a < b` | `True` if `a` is less in value to `b` |
| Greater Than or Equal To | `>=` | `a >= b` | `True` if `a` is greater than or equal in value to `b` |
| Less Than or Equal To | `<= ` | `a <= b` | `True` if `a` is less than or equal in value to `b` |

It intuitively makes sense that these operators would result in a boolean value by just reading them out loud:

Take this code snippet for example:

```python3
a = 4
b = 2

print(a == b)
```
```
False
```

We assign values to the variables `a` and `b`, and then print the result of comparing them using the equality operator: `==`.

If `a` and `b` were the same value, it would print `True`, but in this case they're different, so `False` was printed.

The most important thing to take away from this is simply:

_The result of any comparison operation is a boolean value_.

## Comparison Examples

Play around with a few comparison operators in the REPL.

It's fairly intuitive what the result will be when used on `int` or `float` data:

```python3
>>> x = 10
>>> y = 5
>>> x == y
False
>>> x != y
True
>>> x > y
True
>>> x < y
False
>>> x >= y
True
>>> x <= y
False
```

None of these should be too surprising.

## Order of Operations

It's a good time to rehash the concept of Order of Operations here.

In tutorial 01_03, we talked about arithmetic operators using PEMDAS, so in this example:

```python3
print(2 + 4 * 3)
```

The value `14` would be printed since it performs the `*` operation first.

Python has a hard-coded internal table of what's referred to as _operator precedence_, which is a fancy way of saying order of operations.

It's clear that `*` has higher precedence than `+`, since it gets executed first here.

But the precedence table also extends to more operators than just arithmetic; it also extends to operators like the comparison operators!

So let's look at a code snippet:

```python3
4 + 5 == 9
```

Should we expect this to print `True` or `False`? Well that depends on order of operations.

If the `==` operation is executed first, the statement would be `False`, and then you'd have to evaluate the following:

```python3
4 + False
```

Which wouldn't make much sense.

Comparison operators are actually _all_ lower in precendence than arithmetic operators.

So in this case, it would execute the `+` operation first, which leaves:

```python3
9 == 9
```

Which evaluates to `True`. Try it out!

For your further reading, try Googling something like "Python order of operations table" and seeing what comes up.

Most operators in the table we haven't covered yet, but we will eventually.

You'll see that arithmetic operators are grouped close together, higher than the comparison operators.

## Conclusion

In this tutorial we introduced boolean data types and comparison operators.

Try out `exercise_a.py` in this section for some practice, then move onto the following tutorials to delve into control flow!
