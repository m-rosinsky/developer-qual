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

## Example

Let's look at an example:

```python3
count = 5

# Count down to zero.
while count >= 0:
    print(count)
    
    # Decrement count.
    count -= 1

print("Liftoff! 🚀")
```
```
5
4
3
2
1
0
Liftoff! 🚀
```

Let's break down what's happening here, using the symbol table to assist us:

1. Declare the variable `count` and assign it the value `5`

| Symbol | Data Type | Value |
| --- | --- | --- |
| count | `int` | `5` |

2. Evaluate the condition: `count >= 0`
3. Since `5 >= 0` is `True`, the code block is executed.
    - Print the `count` variable (`5`)
    - Then, it decrements `count` using `count -= 1`.
    - This is a new operator, which is shorthand for writing `count = count - 1`, meaning "subtract 1 from `count` and reassign the result back to `count`"

| Symbol | Data Type | Value |
| --- | --- | --- |
| count | `int` | `4` |

4. The loop checks the condition again: `4 >= 0`, which is still `True`, so the code block runs again!

    - Print `4`
    - Decrement `count` to `3`

5. This process repeats, updating `count` each time (`3`, `2`, `1`, `0`), printing each value along the way.

6. After printing `0`, `count` is decremented to `-1`:

| Symbol | Data Type | Value |
| --- | --- | --- |
| count | `int` | `-1` |

9. Now when the condition is evaluated, it evaluates to `False`
10. Now we _don't_ execute the code block, and we move on in the program.
11. We print the final statement, `"Liftoff! 🚀"`, and the program terminates.

## Infinite Loops

A `while` loop will continue to run as long as its condition is `True`. So what if the condition _never_ becomes `False`?

Here's a simple example. (_Note: If you run this in a terminal, press Ctrl+C to stop it!_)

```python3
count = 10

while count >= 0:
    print(count)

print("Liftoff! 🚀")
```

```
10
10
10
10
10
...
```

Here, we forgot the very important step of decrementing the `count` variable!

Since `count` stays at `10`, the condition `count >= 0` remains `True` forever!

This creates an infinite loop--the program keeps printing `10` until we force it to stop.

If you're debugging a program in the future and the program never terminates an infinite loop is a common culprit!

## The `break` and `continue` Keywords

Python gives us 2 additional keywords to give us a bit more control over loops that we write: `break` and `continue`.

### `break`

`break` is a way to tell the `while` loop to exit right then and there, even if the condition is still `True`! It doesn't evaluate the condition again, and anything left in the code block is also skipped over. It simply moves on to whatever code comes after the while loop.

```python3
secret_number = 6
my_guess = 0

# Guess all the numbers from 0-10, and break early when we find the secret number.
while my_guess <= 10:
    # Print the number we're guessing.
    print(f"Guess: {my_guess}")

    # Check if we reached the secret number.
    if my_guess == secret_number:
        print(f"Got the secret number: {my_guess}")
        
        # Stop the loop!
        break

    # Increment the guess.
    my_guess += 1
```

```
Guess: 0
Guess: 1
Guess: 2
Guess: 3
Guess: 4
Guess: 5
Guess: 6
Got the secret number: 6
```

We combine a few ideas we've discussed in this example:

- A `while` loop
- An `if` statement, _nested_ inside the `while` loop
    - We can tell the `if` statement is inside the while loop because it's indented!
    - We can also tell the code that's inside the `if` statement, since it's indented twice
- f-strings to print the guess
- The `break` keyword to exit out of the loop early

We can see how the `break` keyword works here. Even though our count hadn't yet reached `10`, which would signify the condition returning `False`, we exited early because we encountered the `break` keyword inside of the `if` statement.

_Note_: The `break` keyword _must_ occur inside of a loop! If it's on it's own, we get this error

```python3
break
```

```
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 1
SyntaxError: 'break' outside loop
```

### `continue`
