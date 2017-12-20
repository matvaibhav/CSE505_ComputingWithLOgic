import os
import sys

if (len(sys.argv) < 2):
    print(
        "Arguments expected: Path to test data, path to output")
    exit(0)

rootdir = sys.argv[1]
outdir = sys.argv[2]
for root, dirs, files in os.walk(rootdir):
    for file in files:
        op = open(outdir+"\\"+str(file + ".lp"), "w")

        file_object = open(os.path.join(root, file), "r")

        line = file_object.readline()
        firstLine = line.split(" ")
        op.write("#const num_work = " + firstLine[0] + ".\n")
        op.write("#const num_shifts = " + firstLine[1] + ".\n")
        op.write("#const min_num_shifts = " + firstLine[2].split("\n")[0] + ".\n")
        linecount = 1
        line = file_object.readline()
        while (line):
            splitLine = line.split(" ")
            count = int(splitLine[1])
            i = 2
            values = ""
            j = 0
            while (j < count):
                if (j + 1 == count):
                    values += splitLine[i]
                else:
                    values += splitLine[i] + ";"
                i += 1
                j += 1
            op.write("shift(" + str(linecount) + ", " + values + ").\n")
            linecount += 1
            line = file_object.readline()

op.close()

