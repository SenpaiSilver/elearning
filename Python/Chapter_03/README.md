Logic flow
============

## Defining and calling functions

Defining functions enables you to write clean code. Writing clean code is the key to having control about your program.

	def my_function():
		# Statements

This is the basic code to define a function. You can `return` an object to return a result or return nothing:

	def return_something(arg):
		return (arg)

	def return nothing():
		return

Returning nothing is also the best way to end a function earlier when necessary.

## Defining function arguments

Since functions need to do something it is a good idea to pass arguments to it. There are a few types of arguments you can pass on:

1. Classic arguments;
2. `*args` or argument list;
3. `**kwargs` or keyword argument.

You can specify any numbers of arguments you want but are limited to one `*args` and one `**kwarg` since they are respectivly a `list` and a `dictionnary`.

You can view their usage in `logic.py` script.

## Conditions

When you control the flow of your program you might want to change its behaviour. While working with condition indentation is important and must not differ, for example: this course uses `\t` or `tabs` to indent code.

A scope is defined depending on how it is indented.

### `if`

The `if` keyword will execute any code within its scope when it's `True`:

	if (1 == 1):
		print("It's True")

Using multiple `if`s is possible when you want to check multiple statements without skipping every possibility.

### `elif`

Whenever you want to test multiple possibilities until you find the one you were looking for you can use `elif` after an `if`. `elif` stands for `else if`.

	if (i < 0):
		print("i is less than 0")
	elif (i > 0):
		print("i is greater than 0")

If `i` is less than `0` the program will execute the condition's scope and skip the `elif` and `else` if present.

### `else`

When every logic test fail you can use else:

	if (i < 0):
		print("i is less than 0")
	elif (i > 0):
		print("i is greater than 0")
	else:
	 print("i is 0")

`else` doesn't need a parameter since it's the default action.

## Loops

Loops are conditions that will repeat until they become `False`.

### `while`

As a simple loop, `while` wil repeat its scope while it's `True`.

	while (True):
		print("INFINITE LOOP!!!")

It is now possible to make an infinite loops!

More seriously, it can be used as such:

	i = 0
	while (i <= 64):
		print(i)
		i += 1

This snippet will print from `0` to `64` numbers.

### `for`

When it comes to loops, `for` is much more used since it can interate on objects directly.

	for i in range(64):
		print(i)

This code will print from `0` to `64`. What is actually happening is that `range()` is returning a `list` of numbers.

## Defining program flow

In `C/C++` you have a `main()` function that acts as an entry point to your program. While Python doesn't need such entry point you can still create one with conditions like following:

	if (__name__ == "__main__"):
		# Your statements

When the script is executed the variable `__name__` is set to `__main__`. When it's imported as a module it isn't and will not execute that code.

It's also a good way to handling programs that can be used as modules too.

## Notes

When using `*args` or `**kwargs` you can call the argument however you want, `**my_args` will still be a `**kwargs`.

You can also create `lambda` expressions that behave like functions:

	add_one = lambda x: x + 1
	print(add_one(1)) # Will print 2
	print(add_one(2)) # Will print 3

