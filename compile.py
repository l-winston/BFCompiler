import os

startup = "import numpy as np\nMEMORY_LENGTH = 30000\nmemory = np.zeros((MEMORY_LENGTH), dtype=int)\nindex = 0\n"

def main():
    file_in = open("in.txt", "r")

    file_out = open("out.py", "w")
    file_out.truncate(0)
    file_out.write(startup)

    tabs = 0
    for line_num, line in enumerate(file_in):
        for i in range(len(line)):
            c = line[i]

            prefix = tabs * "\t"

            if c == ">":
                file_out.write(prefix + "index+=1\n")
            elif c == "<":
                file_out.write(prefix + "index-=1\n")
            elif c == "+":
                file_out.write(prefix + "memory[index]+=1\n")
            elif c == "-":
                file_out.write(prefix + "memory[index]-=1\n")
            elif c == ".":
                file_out.write(prefix + 'print(chr(memory[index]), end="")\n')
            elif c == ",":
                file_out.write(prefix + "memory[index]=int(input())\n")
            elif c == "[":
                file_out.write(prefix + "while(memory[index]):\n")
                tabs += 1
            elif c == "]":
                tabs -= 1

    file_out.close()
    print("Executing out.py...")
    os.system("python out.py")


if __name__ == "__main__":
    main()
