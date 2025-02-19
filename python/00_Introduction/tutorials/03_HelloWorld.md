# 00_03 Hello World

## Writing Our First Program

Now that we've got all the boring installation out of the way, let's actually write some code.

Of course, we're required to begin with the proverbial 'Hello, World' program.

To print text to the console output, we'll need to leverage the `print` function in Python.

`print` is a <u><i>built-in</i></u> function, meaning it is given to us natively by the Python interpreter. We'll see a few more of these built-in functions as we continue through the course.

## Functions

If you're confused by what I mean when i say <u><i>function</i></u>, don't worry about it too much yet.

Functions (both built-in and user-defined) will be explaining in detail in later chapters.

## The Main Function

You may be familiar from your experience in other programming languages with a concept known as the _main function_, to mark the entry point of the program.

Python does provide a mechanism to use a main function, but it is optional, so to make our first program as simple as possible, we'll avoid it for now.

Python will simply execute our program from top to bottom, executing each line as it reads them.

## Using the `print` Function

So with that out of the way, here's how we can use the `print` function:

```python
print("Hello, World")
```

When we save this code to a `.py` file, such as `hello_world.py`, and run it using the terminal command:

```bash
% python3 hello_world.py 
Hello, World
```

We see our first program has run successfully!

If something went wrong, go back to the 02_Setup tutorial and ensure you've verified everything in the checklist.

I urge users of this course to code alongside these tutorials, so try this out if you want!

Either make your own py file (probably outside of this repo), or you can leverage an online Python interpreter such as <b>onlinegdb</b>.

Online interpreters are great for writing quick ad-hoc code.

## Syntax

If you're new to Python, you may be asking things like:

- "What's up with the parentheses?"
- "Why is Hello, World in quotes?"

If you're coding alongside me and have these questions, try it out without the quotes and see what happens!

The concepts covered in these questions are a bit too advanced for our first actual lesson, but they will be covered in-depth in future tutorials.

Just hang on to those questions for now, but don't be afraid to experiment on your own.

## Conclusion

Now that we've written our first program, go ahead and tackle exercise_a in the exercise folder of this section.

Remember, you can run the test cases with the `run_tests.sh` script in the root folder of this section.

## Exercises

Try out `exercise_a.py` in the `exercises` subdirectory, and run the `run_tests.sh` script to verify your code is working correctly.
