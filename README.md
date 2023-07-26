# AMM
AMM is short for ascci--. Ascii-- is not that crazy as Brainfuck or other "ESO langs" but i would still say that it is an esoteric programing language. Ascii-- is made by me.

## Ouptut in ascii--
To output sometihng in "AMM" you write "80" which represents "P" in ASCII followed by text you want to output.

    80 Hello, World!
## Variables
Variables in "AMM" are written like this:

    86 AMM 61 ascii--
"86" is "V" in ASCII and is short for variable. "AMM" represents the name of variable. "61" represents addition sign "=" in ASCII. "ascii--" is name of the variable.
To print a variable alone or inside text you type "80" followed by name of the variable inside "<>"

    80 This is <AMM>.
This code prints:

    This is ascii--.
## Repeat
To write repeat block in "AMM" you write "82" followed by number of times you want to repeat the code block. "82" represents "R" in ASCII.

    82 5 
    80 "Hello, World!"
    33
Code above prints "Hello, World!" 5 times.

"33" is "!" in ASCII and represents end of the repeat block.

## Ending program
To end program in "AMM" you just write "0" which represents "NULL" in ASCII and after that you get message:

    Program ended with status code '0'

You can end program inside of repeat block.
## Math
"AMM" uses "Python's eval() function for math". To get result of mathematical expression in "AMM" you type "77" which represents "M" in ASCII followed by mathematical expresion

    77 5 + 3

This will print:

    8
If you mess something up you will get this message:

    Invalid mathematical expression!
## For loop
For loop in "AMM" is declared by number "70" which represents "F" in ASCII. After that you write variable that you want to use in loop (this variable can not be used anywhere else) followe bz "91" which represents "[" in ASCII and "in" in other languages like Python and Javascript. After that you type range throgh which you want to loop:

    70 i 91 0..5
After that you type functions you want to be executed and type "33" to indicate end of for block.

    70 i 91 0..5
    80 i: <i>
    33
This prints the following:

    i: 0
    i: 1
    i: 2
    i: 3
    i: 4