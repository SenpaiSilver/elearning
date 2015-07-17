Variables & types
============

Each language provides a way to store data in memory.

## Strings

### What?

Strings are basically an array for characters. Instead of storing one character in a variable you can store several.

### How?

In Python you can define strings with quotes (`"`), simple quotes (`'`) or triple quotes (`"""`).

	my_quotes = "Quotes are used"
	my_simple_quote = 'Simple quotes were used'
	my_triple_quotes = """And this is triple quotes"""

It is possible to append strings, concatenate or even format them:

	my_format = "Hello {}".format("World")
	my_other_format = "Between %d and %d" % (3, 4)
	my_final_string = my_format + "\n" + my_other_format

The first way used to format a string is an unusual way to do it, it's easier to do it the second way since it works just like `printf()` in `C`.

Here is the corresponding characters to their types:

Character | Type
----------|--------
%d        | Integer
%f        | Float
%s        | String

The list is longer and there a modifiers to.

### When?

Quotes and simple quotes can be used however you want, usually you'll use simple quotes when you don't want to have to escape quotes. The other way around is possible too.

Triple quotes can be used for multiline strings (refer yourself to `vars.py`).

You can't use strings to do math operations:

	fifty_five = "5" + "5" # Will be "55" as a string

Is it also possible to convert an integer to a string with the `str()` function.

## Integers

### What?

Integers are numbers, you can do math with them and they don't behave the same way as string do.

### How?

Assigning and doing math with numbers is as easy as writing it on paper:

	five = 5
	ten = 5 + five
	zero = five - 5

In case you want to convert a string to a number you can use the `int()` function.

You can consult the online manual about all the operators: https://docs.python.org/3.4/library/operator.html

### When?

Integer are best suited for math. There is not much to say about it.

## Notes

Strings and integers are objects. The main difference is that you can call method for strings on constants while you can't on integers.

You can go deeper by looking up floating point numbers.
