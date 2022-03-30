f1 = open("Readme.txt", "r")
vowels = "aeiouAEIOU"
msg = ""
for i in f1.readlines():
    for j in i:
        if j in vowels:
            msg += j

print(msg)