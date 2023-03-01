#Imported the string module to map alphabets and numbers using the zip function.
import string 

letters = string.ascii_letters
numbers = range(1, 53)
mapping = dict(zip(letters, numbers))


#Appended the difference. 
charaters = []

#Accessing the text file and slicing every string into two.
with open("read.txt", "r") as file:
    for f in file:
        first = f[:len(f)//2]
        second = f[len(f)//2:]
        difference = set(first) & set(second)
        charaters.append(difference)

#Looping over charaters and dictionary then adding the values of dictionary if they are same as elements of characters.  
total = 0
for x in charaters:
    for y in mapping:
        if list(x) == list(y):
            total += mapping[y]

print(total)






    
