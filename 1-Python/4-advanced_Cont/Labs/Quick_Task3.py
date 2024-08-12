color = ['Red','Green','White','Black','Pink','Yellow']
with open('demofile2.txt','a') as myfile:
    myfile.write(" ".join(color))


content = open('demofile2.txt')
print(content.read())
