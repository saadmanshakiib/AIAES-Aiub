str = input("Enter String : ")
print("Total Characters : ", len(str))
v = "AEIOUaeiou"
c = 0
for ch in str:
    if ch in v:
        c += 1

print("Number of Vowels : ", c)
print("Uppercase : ", str.upper())
print("Reverse : ", str[:-1])

