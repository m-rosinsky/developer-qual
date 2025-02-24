# 02_02 If Statements

After brushing up on the `bool` data type and comparison operators in the previous chapter, we're ready to dive into the most quintessential piece of control flow in Python, the `if` statement.

## What is Control Flow?

Control Flow is simply how we instruct our program to make decisions.

Kind of like a fork in the road, where our program chooses which side of the fork to go down based on a _condition_.

There are a few different types of Control Flow, and we'll cover the most basic one in this tutorial:

## The `if` Keyword

In the last chapter, we introduced the keywords `True` and `False`.

Here, we introduce another keyword: `if`.

Python recognizes this word as the start of an `if` statement.

An `if` statement, in its most basic form, is formatted like so:

```python3
if <condition>:
    <code>
```

Before we pull this apart, here is an example to make it a bit more tangible:

```python3
max_users = 100
num_users = 100

if num_users >= max_users:
    print("User table is full!")
```

Maybe this example makes it a bit more intuitive to understand what's going on here. But let's break it down:

Of course, we have the `if` keyword. Nothing too crazy there.

## The Condition

Following the `if` keyword, we have our _condition_. A condition is simply something that evaluates to `True` or `False`.

In other words, a condition is an expression that results in a boolean!

Therefore, we typically use our comparison operators in the condition, so we know from the last chapter that comparison operators produce a boolean value!

In the example, we see the condition:

```python3
num_users >= max_users
```

So we're saying, _is the number of users greater than or equal to the maximum number of users?_ Which of course evaluates to `True`, if it is, or `False` otherwise.

## The Code Block

We see that the `print` statement on the line following the condition is indented:

```python3
if num_users >= max_users:
    print("User table is full!")
```

The indentation here is not just for show! The indentation signfies that the line is _inside_ the `if` code block!

This means that this `print` statement will _only_ be execute when the condition in the `if` statement evaluates to `True`.

Otherwise, if the condition is `False`, all the indented code following it will be skipped over completely!

So in our example, our condition is `True`, since `100 >= 100` evaluates to `True`!

So the code inside the `if` block is printed.

## Going Deeper

Let's take a look at another example:

```python3
house_price_yesterday = 250000
house_price_today = 235000

# Let the user know we're checking.
print("Checking if price went down...)

# Check if the price went down.
if house_price_today < house_price_yesterday:
    print(f"House prices fell by {house_price_yesterday - house_price_today} dollars")

print("Done checking!)
```

In this example, we check if today's house price is lower than that of yesterday, and use an f-string (see 01_05) to print out how much.

Another interesting thing to note is that we have 2 `print` statements after the line with the `if` keyword.

One of the `print` statements is indented, and the other one is not.

This means that _only_ the first `print` statement will be executed depending on the conditional!

The second `print` statement, in that it is _not_ indented, will be executed regardless, since it doesn't belong to the `if` block!

The REPL is a bit tricky to play around with indentation so an actual code file may be better here, but play around with it!

What things surprise you, and what makes sense?

## Conclusion

In this chapter, we brought the concept of comparison operators and boolean logic to life via our first bit of control flow, the `if` statement.

Check out `exercise_b.py` in this section to get used to writing a few `if` statements of your own!
