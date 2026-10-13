import numbers

num = []
for i in range(5):
    number = int(input("Enter 5 numbers : "))
    num.append(number)

print(num)

print("Largest Number : ", max(num))
print("Smallest Number : ", min(num))

print("Sum : ", sum(num))
print("Average : ", sum(num)/len(num))

