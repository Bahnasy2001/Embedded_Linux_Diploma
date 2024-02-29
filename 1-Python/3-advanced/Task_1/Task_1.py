import firelink

print("Choose from the following options:")
print("1-Facebook Page\n2-Linkedin Page\n3-Twitter Page")
index = int(input("Choose with index:"))

firelink.firelink(index)


