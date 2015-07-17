#! /usr/bin/env python3

def my_func():
	print("my_function")

def my_func_arg(arg):
	print("Argument: {} ({})".format(arg, type(arg)))

def my_func_arglist(*args):
	for i in args:
		print(i)

def my_func_kwarg(**kwargs):
	for key, val in kwargs.items():
		print("{} => {}".format(key, val))

def return_pow_of_two(nb):
	return (nb ** 2)

def unused_function(first, second, third):
	return (first + second - third)

if (__name__ == '__main__'):
	my_func()
	my_func_arg("My argument is a string.")
	my_func_arg(1337)
	my_func_arglist("Hello", "World", "!")
	my_func_kwarg(msg1="Hello", msg2="World")
	print(return_pow_of_two(8))
else:
	print("This module has been imported.")
