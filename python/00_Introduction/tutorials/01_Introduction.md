# 00_01 Introduction

## A. Welcome

Welcome to this Python "zero-to-hero" course geared towards JQR developers.

This course is designed to bring programmers with zero Python experience or even programming experience to the point where they can feel that Python is a useful tool in their developer toolbag.

These tutorials will reward those that code alongside it, and take their time with the concepts.

If you spot errors such as typos, broken test cases, or have questions about things things related to the course, feel free to reach me here:

`rosinskymike@gmail.com`

## B. A Quick Scenario

You're sitting at your desk on your first day in a developer role.

A superior walks over to your desk with pace:

"Hey dev, we need xyz application that can do xyz by xyz this week, can you handle that for us?"

Being the good dev that you are you answer: "Of course sir, no problem".

Only problem now is, you actually have to write the thing. The requirements are vague, and there are a million ways to come at this problem.

Time to reach into our developer toolbox and see which tool we have that can solve this problem.

"Java, hmmm not sure they have a JVM machine... C, maybe too slow to develop for this time constraint... ah here we are, Python. Verbose, versatile, a real swiss-army knife of the development world. Perfect."

## Python in our Toolbox

Python is a powerhouse of a tool that every developer should feel comfortable enough to call upon in a pinch.

Let's take a look at some of the things Python does well, that we may feel inclined to pick it when faced with a new challenge:

- Readability:
    - One of Python's biggest appeals is the readability of its syntax. It's easy to read, employs a clean structure without the boilerplate a lot of languages contend with, and is a great choice for writing maintainable code
- Versatility:
    - From web development, data analytics, machine learning, automation, Python can do all of these things well
- Developer Ecosystem and Toolchain:
    - Python has an extensive community of developers that can contribute packages through Python's package manager: `pip`
- Cross-platform:
    - Works out-of-the-box for nearly all systems. Just grab the code from one system and drop it in another one, and it should just work. Most system-specific implementation details are abstracted away

Of course, we also have to go over things that Python lacks, so when these requirements are presented we may steer clear of Python:

- Execution Speed:
    - Python is an interpreted language, compared to a compiled language like C or Rust
    - This means that the Python interpreter has to handle language processing at execution-time, rather than only having to read machine-code like compiled languages
    - Optimizations over time have made Python faster, but for realtime systems a compiled language may be a better choice
- Memory Consumption:
    - Due to Python's dynamic nature, memory usage can be high
    - This can invalidate Python's viability on systems where memory is critical, such as embedded systems
- Dependency Management:
    - Especially for large projects, managing dependencies can become complex (See "dependency hell")
    - Tools like `pip` and `virtualenv` can help alleviate these issues, but as a codebase grows to the hundreds or thousands of source code files, Python's weaknesses can begin to show

## Conclusion

With the boring introduction to the language out of the way, we can dive into setting up our environment for writing our first Python programs.
