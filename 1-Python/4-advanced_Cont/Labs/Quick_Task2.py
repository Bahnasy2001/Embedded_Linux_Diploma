#python Style
f = open("demofile2.txt","r")
st = f.read()
print(len(st.split()))

#C style
def word_count(fname):
    with open(fname) as f:
        return (f.read().split())
    
print("Number of Words: ",len(word_count("demofile2.txt")))