def count_vowels(text):
    vowels="aeiou"
    count=0
    for ch in text.lower():
        if  ch in vowels:
            count+=1            
    return count

#user input
text=input("enter string:")

result=count_vowels(text)
print("number of vowels:", result)
