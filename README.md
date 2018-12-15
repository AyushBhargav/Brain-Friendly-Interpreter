# BrainFriendly-Interpreter

Family friendly version of BF interpreter. Literally a turing machine. Written in Python. Language is simple to learn, concise, efficient and not useful.

## Friendly Challenge
Try to generate a fibonacci series with the this language.

## Language Semantics
Consider you have an infinitely long magnetic tape and you are standing exactly in middle. You can walk in two direction. Let's say if you move towards left. you move in negative direction otherwise you will move in positive direction. You start from 0. Each position is called a cell. For a given instruction, 
* You can take single(ASCII) character input from keyboard and store it at cell you are standing on. 
* You can show the character (value stored on which cell you are standing) on screen.
* You can incre/decrement the value for current cell.
* You can move to cell left to your current cell.
* You can move to cell right to your current cell.
* You can initiate a loop for a current cell.
* You can end a loop for a given cell.

| Symbol | Action |
| ------ | ------ |
| > | increment the data pointer (to point to the next cell to the right). |
| < | decrement the data pointer (to point to the next cell to the left). |
| + | increment value by one. |
| - | decrement value by one. |
| . | output value on screen. |
| , | take one byte from keyboard. |
| \[ | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching \] command. |
| \] | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching \[ command. | 

## Sample Addition Program
```
,>,[<+>-]<.
```
### Have fun!
