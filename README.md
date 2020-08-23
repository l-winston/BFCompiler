# BFCompiler
A compiler for the notorious esoteric programming language, [BrainF*ck](https://en.wikipedia.org/wiki/Brainfuck) 



## Example

`in.txt`

```brainfuck
+++++ +++++             (initialize counter (cell #0) to 10)
[                       (use loop to set the next four cells to 70/100/30/10)
    > +++++ ++          (    add  7 to cell #1)
    > +++++ +++++       (    add 10 to cell #2 )
    > +++               (    add  3 to cell #3)
    > +                 (    add  1 to cell #4)
    <<<< -              (    decrement counter (cell #0))
]                   
> ++ .                  (print 'H')
> + .                   (print 'e')
+++++ ++ .              (print 'l')
.                       (print 'l')
+++ .                   (print 'o')
> ++ .                  (print ' ')
<< +++++ +++++ +++++ .  (print 'W')
> .                     (print 'o')
+++ .                   (print 'r')
----- - .               (print 'l')
----- --- .             (print 'd')
> + .                   (print bang)
> .                     (print '\n')
```

`out.py`

```python
import numpy as np
MEMORY_LENGTH = 30000
memory = np.zeros((MEMORY_LENGTH), dtype=np.int8)
index = 0
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
while(memory[index]):
	index+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	index+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	index+=1
	memory[index]+=1
	memory[index]+=1
	memory[index]+=1
	index+=1
	memory[index]+=1
	index-=1
	index-=1
	index-=1
	index-=1
	memory[index]-=1
index+=1
memory[index]+=1
memory[index]+=1
print(chr(memory[index]), end="")
index+=1
memory[index]+=1
print(chr(memory[index]), end="")
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
print(chr(memory[index]), end="")
print(chr(memory[index]), end="")
memory[index]+=1
memory[index]+=1
memory[index]+=1
print(chr(memory[index]), end="")
index+=1
memory[index]+=1
memory[index]+=1
print(chr(memory[index]), end="")
index-=1
index-=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
memory[index]+=1
print(chr(memory[index]), end="")
index+=1
print(chr(memory[index]), end="")
memory[index]+=1
memory[index]+=1
memory[index]+=1
print(chr(memory[index]), end="")
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
print(chr(memory[index]), end="")
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
memory[index]-=1
print(chr(memory[index]), end="")
index+=1
memory[index]+=1
print(chr(memory[index]), end="")
index+=1
print(chr(memory[index]), end="")
```


Here is a table of each of the valid characters in BrainF*ck and their corresponding meanings. 

| Character        | Meaning           |
| ------------- |---------------|
| > | increment the data pointer (to point to the next cell to the right).|
| < | decrement the data pointer (to point to the next cell to the left). |
| + | increment (increase by one) the byte at the data pointer. |
| - | decrement (decrease by one) the byte at the data pointer. |
| . | output the byte at the data pointer. |
| , | accept one byte of input, storing its value in the byte at the data pointer. |
| [ | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command. |
| ] | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command. |

