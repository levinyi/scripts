xxx



chapter: Effective Functions

python's functions are first-class objects. you can assign them to variables, store them in data structures, pass them as arguments to other functions, and even return them as values from other functions.

Grokking these concepts intuitively will make understanding advanced features in Python like lambdas and decorators much easier. It also puts you on a path towards functional programming techniques.

Wrapping your head around the concepts we'll be discussing here might take a little longer than you'd expect. Don't worry--that's completely normal. I've been there. You might feel like you're banging your head against the wall, and then suddenly things will "click" and fall into place when you're ready.

Throughout this chapter I'll be using this yell function for demonstration purposes. It's a simple toy example with easily recognizable output:
```
def yell(text):
	return text.upper() + '!'

>>> yell('hello')
'HELLO!'
```
Functions Are Objects

Functions Can Be Stored in Data Structures
Since functions are first-class citizens, you can store them in data structures, just like you can with other objects. For example, you can add functions to a list:
```
funcs = [bark, str.lower, str.capialize]
>>> funcs
[<function yell at 0x7fce419d2430>, <method 'lower' of 'str' objects>, <method 'capitalize' of 'str' objects>]

>>> for f in funcs:
...     print(f, f('hey there'))
...
<function yell at 0x7fce419d2430> HEY THERE!
<method 'lower' of 'str' objects> hey there
<method 'capitalize' of 'str' objects> Hey there
```
You can even call a function object stored in the list without first assigning it to a variable. You can do the lookup and then immediately call the resulting "disembodied" function object within a single expression:
```
>>> funcs[0]('heyho')
'HEYHO!'
```
Functions Can Be Passed to Other Functions
Because functions are objects, you cann pass them as arguments to other functions. Here's a greet function that formats a greeting string using the function object passed to it and then prints it:
```
>>> def greet(func):
...     greeting = func('Hi, I am a Python program')
...     print(greeting)
```
You can influence the resulting greeting by passinng in different functions. Here's what happens if you pass the bark function to greet:
```
>>> greet(bark)
HI, I AM A PYTHON PROGRAM!
```
Of course, you could also define a new function to generate a different flavor of greeting. For example, the following whisper function might work better if you don't want your Python programs to sound like Optimus Prime:
```
>>> def whisper(text):
...     return text.lower() + '...'
...
>>> greet(whisper)
hi, i am a python program...
```
The ability to pass function objects as arguments to other functions is powerful. It allows you to abstract away and pass around behavior in your programs. In this example, the greet function stays the same but you can influence its output by passing in different greeting behaviors.

Functions that can accept other functions as arguments are also called higher-order functions. They are a necessity for the functional programming style.

The classical example for higher-order functions in Python is the built-in map function. It takes a function object and an iterable, and then calls the function on each element in the iterable, yielding the results as it goes along.

Here's how you might format a sequence of greetings all at once by mapping the bark function to them:
```
>>> list(map(bark, ['hello', 'hey', 'hi']))
['HELLO!', 'HEY!', 'HI!']
```
As you saw, map went through the entire list and applied the bark function to each element. As a result, we now have a new list object with modified greeting strings.

Functions Can Be Nested
Perhaps surprisingly, Python allows functions to be defined inside other functions. These are often called nested functions or inner functions. Here's a example:
```
>>> def speak(text):
...     def whisper(t):
...             return t.lower() + '...'
...     return whisper(text)
...
>>> speak('Hello, World')
'hello, world...'
```
Now, what’s going on here? Every time you call speak, it defines a new inner function whisper and then calls it immediately after. My brain’s starting to itch just a little here but, all in all, that’s still relatively straightforward stuff.

Here’s the kicker though—whisper does not exist outside speak:
```
>>> whisper('Yo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'whisper' is not defined

>>> speak.whisper
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'function' object has no attribute 'whisper'
```
But what if you really wanted to access that nested whisper function from outside speak? Well, functions are objects—you can return the inner function to the caller of the parent function.

For example, here’s a function defining two inner functions. Depending on the argument passed to top-level function, it selects and returns one of the inner functions to the caller:
```
>>> def get_speak_func(volume):
...     def whisper(text):
...             return text.lower() + '...'
...     def yell(text):
...             return text.upper() + '!'
...     if volume >0.5:
...             return yell
...     else:
...             return whisper
```
Notice how get_speak_func doesn’t actually call any of its inner functions—it simply selects the appropriate inner function based on the volume argument and then returns the function object:
```
>>> get_speak_func(0.3)
<function get_speak_func.<locals>.whisper at 0x7fa7f9603940>
>>> get_speak_func(0.7)
<function get_speak_func.<locals>.yell at 0x7fa7f8615dc0>
```
Of course, you could then go on and call the returned function, either directly or by assigning it to a variable name first:
```
>>> speak_func = get_speak_func(0.7)
>>> speak_func('Hello')
'HELLO!'
```
Let that sink in for a second here… This means not only can functions accept behaviors through arguments but they can also return behaviors. How cool is that?

You know what, things are starting to get a little loopy here. I’m going to take a quick coffee break before I continue writing (and I suggest you do the same).
################################################################################################

Functions Can Capture Local State
You just saw how functions can contain inner functions, annd that it's even possible to return these (otherwise hidden) inner functions from the parent function.

Best put on your seat belt now because it's going to get a little crazier still--we're about to enter even deeper functional programming territory.(You had that coffee break, right?)

Not only can functions return other functions, these inner functions can also capture and carry some of the parent function's state with them. Well, what does that mean?

I'm going to slightly rewrite the previous get_speak_func example to illustrate this. The new version takes a "volume" and a "text" argument right away to make the returned function immediately callable:
```
>>> def get_speak_func(text, volume):
...     def whisper():
...             return text.lower() + '...'
...     def yell():
...             return text.upper() + '!'
...     if volume > 0.5:
...             return yell
...     else:
...             return whisper
...
>>> get_speak_func('Hello, World', 0.7)()
'HELLO, WORLD!'
```

Take a good look at the inner functions whisper and yell now. Notice how they no longer have a text parameter? But somehow they can still access the text parameter defined in the parent function. In fact, they seem to capture and "remember" the value of that argument.

Functions that do this are called lexical closures (or just closures, for short). A closure remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.

In practical terms, this means not only can functions return behaviors but they can also pre-configure those behaviors. Here's another barebones exapmle to illustrate this idea:
```
>>> def make_adder(n):
...     def add(x):
...             return x + n
...     return add
...
>>> plus_3 = make_adder(3)
>>> plus_5 = make_adder(5)
>>> plus_3
<function make_adder.<locals>.add at 0x7fa7f8615dc0>
>>> plus_3(4)
7
>>> plus_5(4)
9
```
In this example, make_adder serves as a factory to create and configure "adder" functions. Notice how the "adder" functions can still access the n argument of the make_adder function (the enclosing scope).


### Objects Can Behave Like Functions
While all functions are objects in Python, the reverse isn't true. Objects aren't functions. But they can be made callable, which allows you to treat them like functions in many cases.

If an object is callable it means you can use the round parentheses function call syntax on it and even pass in function call arguments. This is all powered by the __call__ dunder method. Here's an example of class defining a callable object:
```
>>> class Adder:
...     def __init__(self, n):
...             self.n = n
...     def __call__(self, x):
...             return self.n + x
...
>>> plus_3 = Adder(3)
>>> plus_3(4)
7
```
Behind the scenes, “calling” an object instance as a function attempts to execute the object’s __call__ method.

Of course, not all objects will be callable. That’s why there’s a built-in callable function to check whether an object appears to be callable or not:
```
>>> callable(plus_3)
True
>>> callable(yell)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yell' is not defined
>>> callable('hello')
False
```

### Key Takeaways
• Everything in Python is an object, including functions. You can assign them to variables, store them in data structures, and pass or return them to and from other functions (first-class functions.)
• First-class functions allow you to abstract away and pass around behavior in your programs.
• Functions can be nested and they can capture and carry some of the parent function’s state with them. Functions that do this are called closures.
• Objects can be made callable. In many cases this allows you to treat them like functions.

############ 10/12/2020 Levin du
