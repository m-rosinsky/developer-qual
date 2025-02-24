# 02_03 If Else Statements

In the last tutorial, we introduced the `if` keyword and explored how to use it in its most basic form.

In this tutorial, we’ll expand on that by introducing two more keywords: `elif` and `else`.

## The `else` Keyword

Let's revisit the basic syntax of an `if` block:

```python3
if <condition>:
    <code>
```

Here, the `<code>` block only executes when the `<condition>` evaluates to `True`.

We can use the `else` keyword to add a block of code that runs when the condition evaluates to `False`. Here’s how it looks:

```python3
if <condition>:
    <code a>
else:
    <code b>
```

A few key points to note:

1. The `:` appears again after the `else` keyword, indicating the start of a new code block
2. Unlike the `if` clause, the `else` clause doesn’t require a condition
    - That’s because else acts as a catch-all: if the `<condition>` is `False`, `<code b>` runs no matter what.

Let's take a look at an example:

```python3
# Targets we hit on the range.
targets_hit = 31

# Let the user know if they qualified or not.
if targets_hit >= 23:
    print("You've qualified!")
else:
    print("Unqualified shooter. Demotion imminent")
```

It may help to visualize these examples with a flowchart:

| ![If Else](../../../imgs/02_03_IfElse1.png) |
| :--: |
| _If-Else Flowchart_ |

## The `elif` Keyword

We can also add additional branches and conditions to our `if` statements.

Imagine we want to go beyond just telling a shooter whether they qualified or not. Instead, we can tell them their specific qualification level based on their score.

The `elif` keyword lets us add additional conditions like this:

```python3
targets_hit = 31

# Tell the shooter their level of qual.
if targets_hit >= 36:
    print("Expert")
elif targets_hit >= 30:
    print("Sharpshooter")
elif targets_hit >= 23:
    print("Marksman")
else:
    print("Unqualified")

# Call up the next shooter.
print("Next shooter up!")
```
```
Sharpshooter
Next shooter up!
```

Let's walk through this example.

1. The first condition, `targets_hit >= 36`, evaluates to `False` because 31 is less than 36.

2. The next condition, `targets_hit >= 30`, evaluates to `True` since 31 >= 30. So `Sharpshooter` is printed.

3. Once a condition is satisfied, the entire `if`-`elif`-`else` block stops-—no further conditions are checked, and the `else` block is skipped.

Notice that `print("Next shooter up!")` isn’t indented. This means it’s outside the if block and runs regardless of which condition is met.

This behavior is called _mutual exclusion_: only one block within the `if`, `elif`, or `else` structure can execute. Once Python finds a `True` condition, it skips the rest of the block and moves on.

Here's the flowchart for this example:

| ![If Else](../../../imgs/02_03_IfElse2.png) |
| :--: |
| _If-Else Flowchart 2_ |

This one’s a bit more complex! Try picking a number for targets_hit and tracing it through the flowchart yourself.

The diagram shows that only one print statement can run. If all if and elif conditions are False, the else block serves as the catch-all.

## Conclusion

In this tutorial, we expanded upon the `if` statements that we covered previously, and introduced the keywords `elif` and `else`, to form more cohesive decision making in our programs.

Try out `exercise_c.py` for practice using `if`-`elif`-`else` blocks!
