import os
import argparse

startup = "import numpy as np\nMEMORY_LENGTH = 30000\nmemory = np.zeros((MEMORY_LENGTH), dtype=int)\nindex = 0\n"

def parse_args():
    parser = argparse.ArgumentParser(description='Compile BrainF*ck to Python.')
    parser.add_argument('in_file', nargs='?', default="in.txt")
    parser.add_argument('out_file', nargs='?', default="out.py")
    parser.add_argument('-r', action='store_true')

    args = parser.parse_args()

    compile(args.in_file, args.out_file)

    if args.r:
        run(args.out_file)

def compile(in_filepath, out_filepath):
    file_in = open(in_filepath, "r")

    file_out = open(out_filepath, "w")
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

def run(filepath):
    print(f"Executing {filepath}...")
    os.system(f"python {filepath}")

if __name__ == "__main__":
    parse_args()
