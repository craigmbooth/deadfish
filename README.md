An implementation of Deadfish~
==============================

# Overview

Deadfish is a joke programming language.  According to the [esoteric programming language wiki](http://www.esolangs.org), a joke programming language is one that

>is not of any interest except for potential humor value. Generally speaking, it is completely unusable for programming even in theory

One such joke language is Deadfish, which got its name from

>Deadfish was originally going to be called fishheads as programming in this language is like eating raw fish heads. However, due to the limiting features of the language, programming in this language became like eating (and having to smell) dead, rotting fish heads, an experience not often generally considered pleasurable.

Nevertheless, the wiki page for Deadfish contains implementations in 65 different languages including C, C#, C++, Chicken, Clever, COBOL, and Commodore 64 BASIC to name just the C's.

Deadfish has been extended to [Deadfish~](http://esolangs.org/wiki/Deadfish~), which is a super-set of the original Deadfish language.  For what is probably a good reason,  Deadfish~ remained unimplemented... until today.

# Deadfish Language Features

A Deadfish program has a single integer accumulator variable, which is initialized to zero.  The programming language defines only four operations

|cmd| description                                                                               |
|:-:|:------------------------------------------------------------------------------------------|
| i | This increments the accumulator                                                           |
| d | This decrements the accumulator                                                           |
| s | Squares the value in the accumulator                                                      |
| o | Outputs the accumulator                                                                   |

If the accumulator becomes -1 or 256, it is reset to zero.

# Deadfish~ Language Features

Deadfish~ is a super-set of the Deadfish programming language.  Programs have the same single integer accumulator variable as for Deadfish, which is initialized to zero, and has the same behavior around values -1 and 256.  The language is defined via the page on esolangs.org, which contains the following table of supported commands

|cmd| description                                                                               |
|:-:|:------------------------------------------------------------------------------------------|
| i | This increments the accumulator                                                           |
| d | This decrements the accumulator                                                           |
| c | Makes the accumulator a character                                                         |
| o | Outputs the accumulator                                                                   |
| s | Squares the value in the accumulator                                                      |
| {}| Instructions inside the curly braces loop for zero to ten times with an increment of one  |
| ()| If the accumulator is not zero then execute the statement inside once                     |
| h | Halt                                                                                      |
| w | Hello, World! greeting is displayed                                                       |

A couple of these commands are a bit ambiguous, so I decided that for this implementation

   * ``c``, outputs the accumulator as an ascii character, leaving the value in the accumulator unchanged
   * ``{}``, statements inside of the braces are repeated ten times.

The code performs no error checking, and invalid commands or incorrectly nested braces are skipped silently, just like the original author of Deadfish would have wanted.

#Usage

The source code is entirely contained in ``deadfish.py``.  Evaluate Deadfish strings with the ``deadfish.deadfish`` method.

```python
>>> import deadfish
>>> deadfish.deadfish("iisiiiis{ic}{ic}icicicicicic")
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

There is also a CLI for Deadfish~, which can be accessed with ``deadfish.deadfish_cli()``

```
>>> deadfish.deadfish_cli()
>>iiio
3
>>h
```

# Examples

From ``deadfish_cli()``:

```
>>iisiiiisiiiiiiiiciiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiciii{c}dddddddddcdddddddciiiiiiiiiicdddddddc
Horrrrrrrrrrible
>>o
101
>>w
Hello, World!
```

This example shows the standard queries from the top of the Deadfish wiki page, demonstrating that arithmetic works just as one would 'expect' in Deadfish
```
>>iisssoiissiso
0289
```
