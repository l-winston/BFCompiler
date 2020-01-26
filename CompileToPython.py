import os

startup = """import numpy as np\nMEMORY_LENGTH = 30000\nmemory = np.zeros((MEMORY_LENGTH), dtype=np.int8)\nindex = 0\n"""


def main():
    filein = open("input.txt", "r")


    f = open("compiled.py", "w")
    f.truncate(0)
    f.write(startup)

    tabs = 0;
    for line_num, line in enumerate(filein):
        print(str(line_num+1))
        for i in range(len(line)):
            c = line[i]

            prefix = tabs * "\t"

            if c == '>':
                f.write(prefix + "index+=1\n")
            elif c == '<':
                f.write(prefix + "index-=1\n")
            elif c == "+":
                f.write(prefix + "memory[index]+=1\n")
            elif c == "-":
                f.write(prefix + "memory[index]-=1\n")
            elif c == ".":
                f.write(prefix + "print(memory[index])\n")
            elif c == ",":
                f.write(prefix + "memory[index]=int(input())\n")
            elif c == "[":
                f.write(prefix + "while(memory[index]):\n")
                tabs += 1
            elif c == "]":
                tabs -= 1

    #f.write("print(memory)\n")

    f.close()

    os.system("python compiled.py")


if __name__ == "__main__":
    main()
