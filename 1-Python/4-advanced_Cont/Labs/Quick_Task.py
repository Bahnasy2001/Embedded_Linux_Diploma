#python style
f = open("demofile2.txt","r")
lst = f.readlines()
print(len(lst))

#C style
def file_lengthy(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
                pass
    return i + 1
print("Number of lines in the file: ",file_lengthy("demofile2.txt"))