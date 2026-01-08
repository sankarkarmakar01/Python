f = open("file1.txt", "w")
lines = ['line1\n','line2\n','line3']
f.writelines(lines)
f.close()

with open("file1.txt") as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break

