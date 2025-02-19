# 00_04 Comments

## Comments in Code

As a quick aside from talking about variables, let's talk about comments.

Oftentimes, it's useful for developers to annotate code so that themselves or other devs can better understand what a snippet of code is doing.

Comments do not affect the program in any way, rather they're just for developers' quality-of-life.

## Single-Line Comments

We can make single-line comments with the `#` symbol. Everything that follows this character on the same line will be considered a comment:

```python3
# Let console know we're underway.
print("Program starting...")
```

## Multi-Line Comments

Python also supports multi-line comments. We can use the triple quotes `'''` or `"""` to signify the start and end of a multi-line comment.

Here is an example of a dev leaving a comment for other developers to see:

```python3
"""
We'll declare a few sample users for our program to use here.

NOTE: These users should not be modified, or the tests will fail:
"""
username_1 = "jdoe43"
username_2 = "thelegend27"
```

_Fun Fact_: These are actually just multi-line strings, but since they're not assigned to a variable, they functionally don't do anything. Thus, they are used as comments in Python.

## Commenting-Out Code

A common developer practice is to use comments to "deactivate" code that we don't want to be executed, but that we might use later.

Instead of deleting it, we turn it into a comment so that we can uncomment it later.

Consider the following example:

```python3
username1 = "jdoe43"
password1 = "password1"

# This test case is giving us issues, commenting out until resolved.
# username2 = "thelegend27"
# password2 = "thepassword27"
```

Instead of deleting the problematic test case, we can simply comment it out for now, so when the test case is resolved, it can simply be uncommented.

# Exercises

Try out `exercise_b.py` to get used to commenting-out code!
