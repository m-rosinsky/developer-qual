# 01_02 The Symbol Table

## What is the Symbol Table?

Take a look at this code snippet:

```python3
x = 5

print(x)
```

On line 1, we store the value `5` in the variable `x`.

On line 3, we ask Python to recall the value of `x` from before, and print it to the console.

So how does Python store this variable?

The answer is the Symbol Table!

The actual symbol table under the hood is a bit complex, but let's make a simplified version for ourselves that we can use when debugging a program.

It will have 3 columns like so:

| Symbol | Data Type | Value |
| --- | --- | --- |
| | |


When we encounter the line:

```python3
x = 5
```

We can add it to our table:

| Symbol | Data Type | Value |
| --- | --- | --- |
| x | `int` | 5 |

Now when Python sees the line:

```python3
print(x)
```

It sees the symbol `x`, and consults the Symbol Table to see what it's value is. In this case, it finds the entry for `x` from earlier, sees the value `5`, and prints it for us.

Let's see what happens when we execute this line after it.

```python3
print(y)
```

Try it out in the REPL:

```python3
>>> x = 5
>>> print(x)
5
>>> print(y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
>>> 
```

In this case, we expectedly get an error. Python sees the symbol `y` and consults the Symbol Table.

Of course, `y` is not in the Symbol Table! So it throws the error we see above.

We're going to be seeing a lot of the Symbol Table used in future tutorials, as a way to describe the behavior of the program as it exeuctes.

## Modifying Variables

After variables are declared, we can modify them to hold other values, or even values of other data types:

```python3
x = 5
y = x # Create a new variable y and set it equal to the value of x.

# Modify x.
x = 22

# Print.
print(x) # 22
print(y) # 5
```

Let's take a look at what's happening in the table as we go:

First, we declare `x` and add it to the Symbol Table:

```python3
x = 5
```

| Symbol | Data Type | Value |
| --- | --- | --- |
| x | `int` | 5 | 


Then we declare `y`. We'll look up in the Symbol Table the value of `x` and set `y` equal to that value:

```python3
y = x
```

| Symbol | Data Type | Value |
| --- | --- | --- |
| x | `int` | 5 |
| y | `int` | 5 |

Notice here that in our Symbol Table, `y` is a _copy_ of `x`. So later when we modify `x`:

```python3
x = 22
```

Python will consult the Symbol Table and see that `x` already exists, so instead of creating a new entry, it will simply overwrite it:

| Symbol | Data Type | Value |
| --- | --- | --- |
| x | `int` | 22 |
| y | `int` | 5 |

And `y` is not affected. So when we run our `print` statements:

```python3
print(x)
print(y)
```

we see exactly what we'd expect from our symbol table:

```
22
5
```

Try this small program out in the REPL!

```python3
>>> x = 5
>>> y = x
>>> x = 22
>>> print(x)
22
>>> print(y)
5
```

Pretty intuitive for these more trivial examples, but as we add layers of complexity to our programs later on, these first-principles of the Symbol Table will be a very useful tool!

## Conclusion

In this tutorial, we've become introduced to the Symbol Table, a concept we're going to see frequently as the tutorials continue.

I encourage both new and experienced programmers to make a symbol table like this for yourself on some scratch paper when writing or reading code!

Take your program line-by-line updating the symbol table as you go. It can be surprising useful when fixing issues in your programs.

# Exercises

Complete `exercise_a.py` in the exercises directory.

Validate the test cases pass by using the `run_tests.sh` script.
