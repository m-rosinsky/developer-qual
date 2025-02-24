# 02_02 If Statements

After brushing up on the `bool` data type and comparison operators in the previous chapter, we’re ready to dive into the most quintessential piece of control flow in Python: the `if` statement.

## What is Control Flow?

Control flow is simply how we instruct our program to make decisions.

Think of it like a fork in the road: our program chooses which path to take based on a condition.

There are Several types of control flow, but in this tutorial, we’ll cover the most basic one: the `if` statement.

## The `if` Keyword

In the last chapter, we introduced the keywords `True` and `False`.

Now, we’ll introduce another keyword: `if`.

Python recognizes this word as the start of an `if` statement.

In its simplest form, an `if` statement looks like this:

```python3
if <condition>:
    <code>
```

To make this more concrete, here’s an example:

```python3
max_users = 100
num_users = 100

if num_users >= max_users:
    print("User table is full!")
```

This example might make it easier to see what’s happening. 

Let’s break it down step by step.

## The Condition

After the `if` keyword comes the condition-—a statement that evaluates to either `True` or `False`.

In other words, a condition is an expression that produces a boolean value!

That’s why we often use comparison operators (like `>=`, `<`, or `==`) in conditions.

From the last chapter, we know these operators always return a boolean.

In our example, the condition is:

```python3
num_users >= max_users
```

This asks:

_Is the number of users greater than or equal to the maximum number of users?_

If so, it evaluates to `True`; otherwise, it’s `False`.

Here, since 100 >= 100, the condition is `True`.

## The Code Block

To mark the end of the condition and the start of a code block, we use the `:` symbol. You’ll see this symbol pop up in other parts of Python too.

The `:` tells Python that an indented block of code is coming next. For example:

```python3
if num_users >= max_users:
    print("User table is full!")
```

The indentation isn’t just for looks—-it’s critical!

It shows that the print statement belongs inside the if block.

This means the indented code only runs if the condition evaluates to `True`. If the condition is `False`, Python skips over the entire indented block.

In our example, since 100 >= 100 is `True`, the message "User table is full!" will print.

## Going Deeper

Let’s try another example:

```python3
house_price_yesterday = 250000
house_price_today = 235000

# Let the user know we’re checking.
print("Checking if price went down...")

# Check if the price went down.
if house_price_today < house_price_yesterday:
    print(f"House prices fell by {house_price_yesterday - house_price_today} dollars")

print("Done checking!")
```

Here, we check if today’s house price is lower than yesterday’s and use an f-string (see 01_05) to display the difference.

Notice there are two print statements after the `if` line:

1. The first one is indented, so it only runs if the condition (house_price_today < house_price_yesterday) is `True`.

2. The second one isn’t indented, so it runs no matter what, since it’s outside the if block.

In this case, 235000 < 250000 is `True`, so the output would be:

```
Checking if price went down...
House prices fell by 15000 dollars
Done checking!
```

The REPL can be tricky for experimenting with indentation, so you might find it easier to try this in a code file. Play around with it-—what surprises you, and what clicks?

## Conclusion

In this chapter, we brought comparison operators and boolean logic to life with our first taste of control flow: the if statement.

Check out exercise_b.py in this section to practice writing a few if statements of your own!
