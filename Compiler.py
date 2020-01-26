import numpy as np

MEMORY_LENGTH = 30000
memory = np.zeros((MEMORY_LENGTH), dtype=np.int8)

def evaluate(str, index):

    for i in range(len(str)):
        c = str[i]
        if c == '>':
            index += 1
        elif c == '<':
            index -= 1
        elif c == "+":
            memory[index] +=1
        elif c == "-":
            memory[index] -= 1
        elif c == ".":
            print(memory[index], end=" ")
        elif c == ""



def main():
    str = input("Enter Command:\n")

    evaluate(str, index=0)


if __name__ == "__main__":
    main()
