# 01_03 Arithmetic

## Basic Arithmetic

Python supports the basic mathematical operators for numerical values:

| Operation | Operator | Description |
| --- | --- | --- |
| Addition | `+` | Basic addition |
| Subtraction | `-` | Basic subtraction |
| Multiplication | `*` | Basic multiplication |
| Division | `/` | Basic division |

We can use these in our programs just as we would expect:

```python3
# Basic addition.
x = 5 + 4 # 9

# Using multiple operators.
y = x * 2 + 4 # 22

# Python will use PEMDAS order-of-operations.
z = y + 2 * 4 # 30

# Python will also respect parentheses.
w = (z + x) * -1 # -39
```

Try using some of these operators in the REPL!

## Additional Arithmetic Operators

Python also gives us a few additional operators for our convenience:

| Operation | Operator | Description |
| --- | --- | --- |
| Integer (aka 'Floor') Division | `//` | Perform division and round result (always down) to the nearest integer |
| Exponentiation | `**` | `a ** b` Raise `a` to the `b` power |
| Modulus | `%` | Perform division, and use the remainder as the result |

Try some of these out in the REPL:

```python3
x = 14 // 5 # Divide 14 by 5 and round result down.

y = 2 ** 4 # Raise 2 to the 4th power.

z = 13 % 2 # Divide 13 by 2 and give just the remainder.
```

If you're having trouble with the modulus operator, it sometimes helps to imagine it as long division, taking the remainder:

![Long Div](../../../imgs/00_03_longdiv.png)

## Using Arithmetic on Other Data Types

Other data types than integers support arithmetic operations!

Joining two strings together, also referred to as _concatenation_, involves using the `+` operator:

Try this out in the REPL:

```python3
first_name = "James"
last_name = "Bond"

# Create the full name, adding a space in between.
full_name = first_name + " " + last_name
print(full_name)
```

In this case, we concatentated 3 strings together: The first name, a space, and the last name, to form a single string, which is stored in the `full_name` variable.

Let's look at the symbol table, just to keep the idea fresh:

| Symbol | Data Type | Value |
| --- | --- | --- |
| first_name | `str` | `"James"` |
| last_name | `str` | `"Bond"` |
| full_name | `str` | `"James Bond"` |

We can also use the multiply `*` operator on a `str` and an `int` to repeat the string multiple times:

```python3
sound_effect = "pow"

# Throw some punches!
print(sound_effect * 3) # powpowpow
```

We can also apply what we learned about concatenation to add some extra pop to these punches:

```python3
sound_effect = "pow"

# Throw some punches!
print(sound_effect * 3 + "!") # powpowpow!
```

Remember order of operations, we multiply the string `"pow"` by `3` to get `"powpowpow"`, then add the string `"!"` to the end via concatenation to get the final result.

## Exercises

Try `exercise_b.py` to practice using arithmetic operations.

Remember the REPL and drawing out the Symbol Table as you go are great tools to help you if you get stuck.
