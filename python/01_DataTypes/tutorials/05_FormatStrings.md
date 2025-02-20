# 01_04 Format Strings

## The Old Way

Before we dive into the concept of _format strings_, let's take a look at a quick code example:

```python3
# Create some info for a tweet.
tweet_body = "Just setting up my twitter!"
tweet_author = "@jack"
tweet_likes = 24

# Print the details of the tweet.
print("User " + tweet_author + " tweeted '" + tweet_body + "', which got " + str(tweet_likes) + " likes")
```

When we run this code, we get:

```
User @jack tweeted 'Just setting up my twitter!', which got 24 likes
```

This works, but notice how we had to:

1. Use multiple `+` operators to concatenate strings
2. Cast `tweet_likes` from an `int` to a `str`
3. Manually add spaces and punctuation to make the sentence more readable

This approach gets messy fast, especially as we add more variables or longer strings.

Let's explore a better way: _format strings_.

## What are Format Strings?

Format strings provide a cleaner, more readable way to combine variables into a string.

They let us embed expressions directly into a _template_, handling type casting automatically in most cases.

Python offers a few ways to do this, which we'll cover here:

## Method 1: The `.format()` Method

The built-in `.format()` function lets us define placeholders in a string using curly braces `{}`, and then fill them in with values after.

Here's how we can rewrite our tweet example:

```python3
# Create some info for a tweet.
tweet_body = "Just setting up my twitter!"
tweet_author = "@jack"
tweet_likes = 24

# Use .format() to print the details.
print("User {} tweeted '{}', which got {} likes".format(tweet_author, tweet_body, tweet_likes))
```

Which yields the same output:

```
User @jack tweeted 'Just setting up my twitter!', which got 24 likes
```

Breaking down what's happening here:

- The `{}` placeholders act as slots to insert values
- The `.format()` method fills these slots with the arguments in the order they are provided
    - So in this case, `tweet_author` goes into the first `{}` placeholder, since it was provided first, and so on
- Python automatically converts `tweet_likes` (an `int`) to a string for us, so we don't have to call the `str()` casting method

---

You can also name the placeholders for clarity:

```python3
print("User {author} tweeted '{body}', which got {likes} likes".format(
    author=tweet_author, 
    body=tweet_body, 
    likes=tweet_likes
))
```

The named version produces the same output, but may make the code more readable, especially with many variables.

## Method 2: F-Strings

_f-strings_ are the preferred method in newer versions of Python. They were added in Python 3.6 (we're using 3.12).

The `.format()` method from before can still be used, but f-strings are more preferable now.

With f-strings, you can prefix the string with an `f` and put variables or values directly inside the curly braces.

So an f-string is simply a string with a `f` in front of it:

- `f""` or `f''` - Remember double quotes and single quotes in Python are functionaly identical

Here's the tweet example using an f-string instead of `.format`:

```python3
# Create some info for a tweet.
tweet_body = "Just setting up my twitter!"
tweet_author = "@jack"
tweet_likes = 24

# Use an f-string to print the details.
print(f"User {tweet_author} tweeted '{tweet_body}', which got {tweet_likes} likes")
```

and we get the same output:

```
User @jack tweeted 'Just setting up my twitter!', which got 24 likes
```

This method is concise, intuitive, and more flexible!

We can even add some in-line logic like arithmetic:

```python3
print(f"User {tweet_author} tweeted '{tweet_body}', which got {tweet_likes * 2} likes after doubling")
```

```
User @jack tweeted 'Just setting up my twitter!', which got 48 likes after doubling
```

## Getting Fancier with F-Strings

f-strings can do more than just plug in values--they can format them in specific ways as well!

For instance, let's say we're printing a monetary value:

```python3
order_total = 17.40

print(f"Your order total is ${order_total}")
```

```
Your order total is $17.4
```

Hmmm.. that doesn't look quite right. Of course it's correct, but it cut off the trailing zero of our float. Dollar values are not typically presented this way.

We can use a special feature of f-strings to format floats like so:

```python3
order_total = 17.40

print(f"Your order total is ${order_total:.2f}")
```

```
Your order total is $17.40
```

That looks better. The `:` operator here tells the f-string to look for some formatting instructions. And `.2f` tells it that we should always print 2 decimal places of a `float`.

There are plenty more things we can do to format values based on our requirements with f-strings and the `:` operator. But we'll leave those as an exercise to the reader if they wish to explore this concept more.

## Exercises

Check out `exercise_d.py` to get some reps with format strings!
