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

The actual symbol table under the hood is a bit complex, but let's make a simplified version for ourselves that we can use when debugging a program:

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
>>> print(y)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'y' is not defined
```

In this case, we expectedly get an error. Python sees the symbol `y` and consults the Symbol Table.

Of course, `y` is not in the Symbol Table! So it throws the error we see above.

We're going to be seeing a lot of the Symbol Table used in future tutorials, as a way to describe the behavior of the program as it exeuctes.

## Conclusion

In this tutorial, we've become introduced to the Symbol Table, a concept we're going to see frequently as the tutorials continue.

I encourage both new and experienced programmers to make a symbol table like this for yourself on some scratch paper when writing or reading code!

Take your program line-by-line updating the symbol table as you go. It can be surprising useful when fixing issues in your programs.
