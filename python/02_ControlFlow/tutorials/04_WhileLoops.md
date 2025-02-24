# 02_04 While Loops

_Loops_ are another form of control flow that we can utilize in our Python programs.

There are a few types of loops offered to us in Python, and we'll look at the most basic one in this tutorial, the `while` loop.

## How Does the `while` Loop Work?

Let's take a look at the syntax of a `while` loop:

```python3
while <condition>:
    <code>
```

This might look familiar--it's nearly identical to the `if` statement syntax we covered in previous chapters, except the `if` keyword is swapped for `while`.

The `while` loop operates in a way that's similar to an `if` statement, but with a key twist!

Here's how it works: We evaluate the `<condition>`. If it's `True`, the `<code>` block runs in its entirety. So far, that's just like an `if` statement.

The difference is that after the `<code>` block executes, the `<condition>` is checked again. If it's still `True`, the block runs again!

The process repeats (potentially infinitely) until the `<condition>` evaluates to `False`.

At that point, the loop stops, and the program moves on to whatever comes next.
