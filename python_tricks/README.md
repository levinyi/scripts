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
*   Everything in Python is an object, including functions. You can assign them to variables, store them in data structures, and pass or return them to and from other functions (first-class functions.)
*   First-class functions allow you to abstract away and pass around behavior in your programs.
*   Functions can be nested and they can capture and carry some of the parent function’s state with them. Functions that do this are called closures.
*   Objects can be made callable. In many cases this allows you to treat them like functions.

############ 10/12/2020 

### 3.2 Lambdas Are Sinngle-Expression Functions
The lambda keyword in Python provides a shortcut for declaring small anonymous functions. Lambda functions behave just like regular functions declared with the def keyword. They can be used whenever function objects are required.

For example, this is how you'd define a simple lambda function carrying out an addition:
```
>>> add = lambda x, y : x + y
>>> add(5,3)
8
```
You could declare the same add function with the def keyword, but it would be slightly more verbose:
```
>>> def add(x, y):
...     return x + y
...
>>> add(5,3)
8
```

Now you might be wondering, "Why the big fuss about lambdas? If they're just a slightly more concise version of declaring functions with def, what's the big deal?"

Take a look at the following example and keep the words function expression in your head while you do that:
```
>>> (lambda x, y: x + y)(5, 3)
8
```
Okay, what happened here? I just used lambda to define an "add" function inline and then immediately called it with the arguments 5 and 3.

Conceptually, the lambda expression lambda x, y: x + y is the same as declaring a function with def, but just written inline. THe key difference here is that I didn't have to bind the function object to a name before U used it. I simply stated the expression I wanted to compute as part of a lambda, and then immediately evaluated it by calling the lambda expression like a regular function.

Before you move on, you might want to play with the previous code example a little to really let the meaning of it sink in. I still remember this taking me awhile to wrap my head around. So don't worry spending a few minutes in an interpreter session on this. I'll be worth it.

There's another syntactic difference between lambdas and regular function definitions. Lambda functions are restricted to a single expression. This means a lambda function can't use statements or annotations --not even a return statement.

How do you return values from lambdas then? Executing a lambda function evaluates its expression and then automatically returns the expression's result, so there's always an implicit return statement. That's why some people refer to lambdas as single expression functions.

### Lambdas You Can Use

When should you use lambda functions in your code? Technically, any time you're expected to supply a function object you can use a lambda expression. And because lambdas can be anonymous, you don't even need to assign them to a name first.

This can provide a handy and "unbureaucratic" shortcut to defining a function in Python. My most frequent use case for lambdas is writing short and concise key funcs for sorting iterables by an alternate key:
```
>>> tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
>>> sorted(tuples, key=lambda x: x[1])
[(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
```
In the above example, we’re sorting a list of tuples by the second value in each tuple. In this case, the lambda function provides a quick way to modify the sort order. Here’s another sorting example you can play with:

```
>>> sorted(range(-5,6), key=lambda x: x*x)
[0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]
```

Both examples I showed you have more concise implementations in Python using the built-in operator.itemgetter() and abs() functions. But I hope you can see how using a lambda gives you much more flexibility. Want to sort a sequence by some arbitrary computed key? No problem. Now you know how to do it.

Here's another interesting thing about  lambdas: Just like regular nested functions, lambdas also work as lexical closures.

What's a lexical closure? It's just a fancy name for a function that remembers the values from the enclosing lexical scope even when the program flow is no longer in that scope. Here's a (fairly academic) example to illustrate the idea:
```
>>> def make_adder(n):
...     return lambda x: x + n
...
>>> plus_3 = make_adder(3)
>>> plus_3
<function make_adder.<locals>.<lambda> at 0x7f1f9042b820>
>>> plus_5 = make_adder(5)
>>> plus_3(4)
7
>>> plus_5(4)
9
```
In the above example, the x + n lambda can still access the value of n even though it was defined in the make_adder function (the enclosing scope).

Sometimes, using a lambda function instead of a nested function declared with the def keyword can express the programmer's intent more clearly. But to be honest, this isn't a common occurrence -- at least not in the kind of code that I like to write. So let's talk a little more about that.

### But Maybe You Shouldn't...

On the one hand, I'm hoping this chapter got interested in exploring Python's lambda functions. On the other hand, I feel like it's time to put up another caveat: Lambda functions should be used sparingly and with extraordinary care.

I know I've written my fair share of code using lambdas that looked "cool" but were actually a liability for me and my coworkers. if you're tempted to use a lambda, spend a few seconds (or minutes) to think if it is really the cleanest and most maintainable way to achieve the desired result.

For example, doing something like this to save two lines of code is just silly. Sure, technically it works and it's a nice enough "trick". But it's also going to confuse the next gal or guy that has to ship a bugfix under a tight deadline:
```
# Harmful:
>>> class Car:
...     rev = lambda self: print("Wroom!")
...     crash = lambda self: print('Boom!')
...
>>> my_car = Car()
>>> my_car.crash()
Boom!
```
I have similar feelings about complicated map() or filter() constructs using lambdas. Usually it's much cleaner to go with a list comprehension or generator expression:
```
# Harmful:
>>> list(filter(lambda x:x %2 == 0, range(16)))
[0, 2, 4, 6, 8, 10, 12, 14]

# Better:
>>> [x for x in range(16) if x % 2 ==0]
[0, 2, 4, 6, 8, 10, 12, 14]
```

If you find yourself doing anything remotely complex with lambda expressions, consider defining a standalone function with a proper name instead.

Saving a few keystrokes won't matter in the long run, but your colleagues (and your future self) will appreaciate clean and readable code more than terse wizardry.

### Key Takeaway
*  Lambda functions are single-expression functions that are not necessarily bound to a name (anonymous).
*  Lambda functions can't use regular Python statements and always include an implicit return statement.
*  Always ask yourself: Would using a regular (named) function or a list comprehension offer more clarity?


# 3.3 The Power of Decorators
At their core, Python's decorators allow you to extend and modify the behavior of a callable(functions, methods, and classes) without permanently modifying the callable itself.

Any sufficiently generic functionality you can tack on to an existing class or function's behavior makes a great use case for decoration. This includes the following:
* logging
* enforcing access control and authentication
* instrumentation and timing functions
* rate-limiting
* caching and mor

Now, why should you master the use of decorators in Python? After  all, what I just mentioned  sounded quite abstract, and it might be difficult to see how decorators can benefit you in your day-to-day work as a Python developer. Let my try to bring some clarity to this question by giving you a somewhat real-world example:

Imagine you've got 30 functions with business logic in your reportgeneration program. One rainy Monday morning your boss walks up to your desk and says: "Happy Monday! Remember those TPS reports? I need you to add input/output logging to each step in the report generator. XYZ Corp needs it for auditing purposes. Oh, and I told them we can ship this by Wednesday."

Depending on whether or not you've got a solid grasp on Python's decorators, this request will either send your blood pressure spiking or leave you relatively calm.

Without decorators you might be spending the next three days scrambling to modify each of those 30 functions and clutter them up with manual logging calls. Fun times, right?

If you do know your decorators however, you'll calmly smile at your boss and say: "Don't worry Jim, I'll get it done by 2pm today."

Right after that you'll type the code for a generic @audit_log decorator (that's only about 10 lines long) and quickly paste it in front of each function definition. Then you'll commit your code and grab another cup of coffee...

I'm dramatizing here, but only a little. Decorators can be that powerful. I'd go as far as to say that understanding decorators is a milestone for any serious Python programmer. They require a solid grasp of several advanced concepts in the language, including the properties of first-class functions.

### I believe that the payoff for understanding how decorators work in Python can be enormous.

Sure, decorators are relatively complicated to wrap your head around for the first time, but they're a hightly useful feature that you'll often encounter in third-party frameworks and the Python standard library. Explaining decorators is also a make or break moment for any good Python tutorial. I'll do my best here to introduce you to them step by step.

Before you dive in however, now would be an excellent moment to refresh your memory on the properties of first-class functions in Python. There's a chapter on them in this book, and I would encourage you to take a few minutes to review it. The most important "first-class functions" takeaways for understanding decorators are:
* Functions are objects- they can be assigned to variables and passed to and returned from other functions
* Functions can be defined inside other functions -- and a child function can capture the parent function's local state (lexical closures)

Alright, are you ready to do this? Let's get started.

### Python Decorator Basics
Now, what are decorators really? They "decorate" or "wrap" another function and let you execute code before and after the wrapped function runs.

Decorators allow you to define reusable building blocks that can change or extend the behavior of other functions. And, they let you do that without permanently modifying the wrapped function itself. The function's behavior changes only when it's decorated.

What might the implementation of a simple decorator look like? In basic terms, a decorator is a callable that takes a callable as input and returns another callable.

The following function has that property and could be considered the simplest decorator you could possibly write:
```
def null_decorator(func):
    return func
```

As you can see, null_decorator is a callable (it's a function), it takes another callable as its input, and it returns the same input callable without modifying it.

Let's use it to decorate (or wrap) another function:
```
def greet():
    return "Hello"

greet = null_decorator(greet)

>>> greet()
'Hello'
```

In this example, I've defined a greet function and then immediately decorated it by running it through the null_decorator function. I know this doesn't look very useful yet. I mean, we specifically designed the null decorator to be useless, right? But in a moment this example will clarify how Python's special-case decorator syntax works.

Instead of explicitly calling null_decorator on greet and then reassigning the greet variable, you can use Python's @syntax for decorating a function more conveniently:
```
@null_decorator
def greet():
    return "Hello"

>>> greet()
'Hello'
```

Putting an @null_decorator line in front of the function definition is the same as defining the function first and then running through the decorator. Using the @syntax is just syntactic sugar and a shortcut for this commonly used pattern.

Note that using the @ syntax decorates the function immediately at definition time. This makes it difficult to access the undecorated original without brittle hacks. Therefore you might choose to decorate some functions manually in order to retain the ability to call the undecorated function as well.

### Decorators Can Modify Behavior
Now that you're a little more familiar with the decorator syntax, let's write another decorator that actually does something and modifies the behavior of the decorated function.

Here's a slightly more complex decorator which converts the result of the decorated function to uppercase letters:
```
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
```

Instead of simply returning the input function like the null decorator did, this uppercase decorator defines a new function on the fly(a closure) and uses it to wrap the input function in order to modify its behavior at call time.

The wrapper closure has access to the undecorated input function and it is free to execute additional code before and after calling the input function. (Technically, it doesn't even need to call the input function at all.)

Note how, up until now, the decorated function has never been executed. Actually calling the input function at this point wouldn't make any sense -- you'll want the decorator to be able to modify the behavior of its input function when it eventually gets called.

You might want to let that sink in for a minute or two. I know how complicated this stuff can seem, but we'll get it sorted out together, I promise.

Time to see the uppercase decorator in action. What happens if you decorate the original greet function with it?
```
@uppercase
def greet():
    return 'Hello!'

>>>greet()
'HELLO!'
```
I hope this was the result you expected. Let's take a closer look at what just happened here. Unlike null_decorator, our uppercase decorator returns a different function object when it decorates a function:
```
>>> greet
<function uppercase.<locals>.wrapper at 0x7f76a753d4c0>
>>> null_decorator(greet)
<function uppercase.<locals>.wrapper at 0x7f76a753d4c0>
>>> uppercase(greet)
<function uppercase.<locals>.wrapper at 0x7f76a753d5e0>
```

And as you saw earlier, it needs to do that in order to modify the behavior of the decorated function when it finally gets called. The uppercase decorator is a function itself. And the only way to influence the "future behavior" of an input function it decorates is to replace (or wrap) the input function with a closure.

That's why uppercase defines and returns another function (the closure) that can then be called at a later time, run the original input function, and modify its result.

Decorators modify the behavior of a callable through a wrapper closure so you don't have to permanently modify the original. The original callable isn't permanently modified -- its behavior changes only when decorated.

This let's you tack on reusable building blocks, like logging and other instrumenttation, to existing functions and classes. It makes decorators such a powerful feature in Python that it's frequently used in the standard library and in third-party packages.

### A Quick Intermission
By the way, if you feel like you need a quick coffee break or a walk around the block at this point -- that's totally normal. In my opinion closures and decorators are some of the most difficult concepts to understand in Python.

Please, take your time and don't worry about figuring this out immediately. Playing through the code examples in an interpreter session one by one often helps make things sink in.

I know you can do it!

### Applying Multiple Decorators to a Function
Perhaps not surprisingly, you can apply more than one decorator to a function. This accumulates their effects and it's what makes decorators so helpful as resuable building blocks.

Here's an example. The following two decorators wrap the output string of the decorated function in HTML tags. By looking at how the tags are nested, you can see which order Python uses to apply multiple decorators:
```
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper
```
Now let's take these two decorators and apply them to our greet function at the same time. You can use the regular @ syntax for that and just "stack" multiple decorators on top of a single function:
```
>>> greet()
'<em><strong>Hello!</strong></strong>'
```

This clearly shows in what order the decorators were applied: from bottom to top. First, the input function was wrapped by the @emphasis decorator, and then the resulting (decorated) function got wrapped again by the @strong decorator.

To help me remember this bottom to top order, I like to call this behavior decorator stacking. You start building the stack at the bottom and then keep adding new blocks on top to work your way upwards.

If you break down the above example and avoid the @ syntax to apply the decorators, the chain of decorator function calls looks like this:
```
decorated_greet = strong(emphasis(greet))
```

Again you can see that the emphasis decorator is applied first and then the resulting wrapped function is wrapped again by the strong decorator.

This also means that deep levels of decorator stacking will evenutally have an effect on performance because they keep adding nested function calls. In practice, this usually won't be a problem, but it's something to keep in mind if you're working on performance-intensive code that frequently uses decoration.

### Decorating Functions That Accept Arguments
All examples so far only decorated a simple nullary greet function that didn't take any arguments whatsoever. Up until now, the decorators you saw here didn't have to deal with forwarding arguments to the input function.

If you try to apply one of these decorators to a function that takes argumetns, it will not work correctly. How do you decorate a function that takes arbitrary arguments?
```
def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
There are two notable things going on with this decorator:
**  It uses the * and ** operators in the wrapper closure definition to collect all positional and keyword arguments and stores them in variables (args and kwargs).
*** The  wrapper closure then forwards the collected arguments to the original input function using the * and ** "argument unpacking" operators.
It's a bit unfortunate that the meaning of the star and double-star operators is overloaded and changes depending on the context they're used in, but I hope you get the idea.

Let's expand the technique laid out by the proxy decorator into a more useful practical example. Here's a trace decorator that logs function arguments and results during execution time:
```
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: CALLING {func.__name__}() '
            f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
            f'returned {original_result!r}')
        return original_result
    return wrapper
```
Decorating a function with trace and then calling it will print the arguments passed to the decorated function and its return value. This is still somewhat of a "toy" example -- but in a pinch it makes a great debugging aid:
```
@trace
def say(name, line):
    return f'{name}: {line}'
>>> say('Jane', 'Hello, World')
TRACE: CALLING say() with ('Jane', 'Hello, World'), {}
TRACE: say() returned 'Jane: Hello, World'
'Jane: Hello, World'
```
Speaking of debugging, there are some things you should keep in mind when debugging decorators:
### How to Write "Debuggable" Decorators
When you use a decorator, really what you're doing is replacing one function with another. One downside of this process is that it "hides" some of the metadata attached to the original (undecorated) function.

For example, the original function name, its docstring, and parameter list are hidden by the wrapper closure:
```
def greet():
    """Return a friendly greeting."""
    return 'Hello!'

decorated_greet = uppercase(greet)
```
If you try to access any of that function metadata, you’ll see the wrapper closure’s metadata instead:
```
>>> greet.__name__
'greet'
>>> greet.__doc__
'Return a friendly greeting.'
>>> decorated_greet.__name__
'wrapper'
>>> decorated_greet.__doc__
None
```
This makes debugging and working with the Python interpreter awkward and challenging. Thankfully there’s a quick fix for this: the functools.wraps decorator included in Python’s standard library. You can use functools.wraps in your own decorators to copy over the lost metadata from the undecorated function to the decorator closure.
Here’s an example:
```
import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper
```
Applying functools.wraps to the wrapper closure returned by the decorator carries over the docstring and other metadata of the input function:
```
@uppercase
def greet():
"""Return a friendly greeting."""
return 'Hello!'
>>> greet.__name__
'greet'
>>> greet.__doc__
'Return a friendly greeting.'
```
As a best practice, I’d recommend that you use functools.wraps in all of the decorators you write yourself. It doesn’t take much time and
it will save you (and others) debugging headaches down the road. Oh, and congratulations—you’ve made it all the way to the end of
this complicated chapter and learned a whole lot about decorators in Python. Great job!

Key Takeaways
• Decorators define reusable building blocks you can apply to a callable to modify its behavior without permanently modifying
the callable itself.
• The @ syntax is just a shorthand for calling the decorator on an input function. Multiple decorators on a single function are
applied bottom to top (decorator stacking).
• As a debugging best practice, use the functools.wraps helper in your own decorators to carry over metadata from the undecorated callable to the decorated one.
• Just like any other tool in the software development toolbox, decorators are not a cure-all and they should not be overused. It’s important to balance the need to “get stuff done” with the goal of “not getting tangled up in a horrible, unmaintainable mess of a code base.”


