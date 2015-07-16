Hello World!
============

In this chapter we will cover how to get started in Python. This course will focus on Python 3.

## Setting up Python 3

Depending on your operating system you will need to download an installer, the source code or a precompiled version. This chapter covers installing Python 3 on Windows and Debian (Ubuntu and Mint).

[Debian 8](http://www.debian.org/) was used to write this course but any other GNU/Linux OS can be used too. It is expected that you can learn how to use the terminal and that you have `root` access.

### Windows

The official web site provides an installer for Windows that can be found here: https://www.python.org/download/releases/3.0/

In case `python` or `python3` can't be launched from the command line you will need to add its folder to the `%PATH%` environnement variable in Windows. This won't be covered here and we will assume that you know how to launch Python script from the command line.

### Debian

For Debian, and Debian based distros such as Ubuntu, you can install Python 3 with the `apt-get` command line:

	$ sudo apt-get install python3

You can also append the command with other packets such as text editors that will be covered in the next section.

The usage of the command line won't be taught in this course and we will assume that all the files created can be executed as if `chmod +x` was used on them.

## Editor

### Windows

The most populare text editor a the time of printing is currently [Notepad++](https://notepad-plus-plus.org/), but you can use just about anything.

### Debian

Depending on how you use Debian you will have more choices. For console usage I recommend `vim`, but since it can be a bit hard to leard how to use you may want to use another editor.

For a graphical usage you can use `gedit`, `leafpad`, or `geany`.

To install an editor, just use `apt-get`:

	$ sudo apt-get install vim gedit leafpad geany

Remove the editors you won't use. This course will not focus on the usage of the editor and it you choose to use `vim` you will have to learn by yourself how to use it.

## Program entry point

All language provide an entry point for the program to start. In Python the entry point is the start of the file. Python also provides an interpreter so you can type in and try out expression on the go.

## Printing to STDOUT

Printing to `STDOUT` (Standard Output) is simply printing text on the terminal. To do so the `print()` function is used and takes a `String` as the first argument.

	print("Hello World!")

Printing text to `STDOUT` can be consuming, so try printing as much text as once instead of printing each character one by one.

It is also possible to print directly numbers with and without `quotes`:

	print(5)
	print("5")

The `print()` function can also take some special arguments called `keyword arguments` such as `file=` wich requires a `file` object. Printing to `STDOUT` can be achieve also by printing the following code:

	import sys

	print("Hello World!", file=sys.stdout)

The default behaviour of `print()` is to print the first argument followed by a newline (`\n`), in case you want to control that it is possible to use the argument `end=` which requires a `String`:

	print("Hello", end=" ") # Print "Hello" and end it with a space
	print("World", end="!") # Print "World" and end it with a !
	print("")               # Just print a newline

You will notice that you needed to import a module. Modules will be covered in a later chapter.

### Why?

It is necessary in modern computing to print the output somewhere that can be read by a human being. The best way and most economic is to print the output to a screen directly.

`STDOUT` being the *standard output* is the default output for `print()`

## Printing to STDERR and why

As seen previously we will need to import a module to achieve this since `print()` can write to different ouput like if they were files (see end note about files) with the `file=` argument.

	import sys

	print("Fatal Error", file=sys.stderr)

If you're running on GNU/Linux you can verify that it prints on `STDERR` by redirecting `STDOUT` to `/dev/null`.

### Why?

Some programs will output processed data to `STDOUT` and it will output logging (info, warnings and errors) to `STDERR` so that the main output is not affected or can be processed indenpendtly.

For example `curl` uses `STDERR` to inform about the status of the connection and will only print to `STDOUT` the body's response.

## Notes

On Linux and UNIX systems everything is a file, even the physical hardware is represented as a file. To print to a file you will need to get a file descriptor with is, to the program, a handle to access, read and/or write a file.
For Python an object is returned instead of the bare file descriptor.
`sys.stdout` is `STDOUT`'s object and `sys.stderr` is `STDERR`'s object.
