def square(num):
    return num*num

print(square(2))

word = input("Enter string:")
if is_palindrome(word):
    print(f'"{word}"is a palindrome.')
else:
    print("word is not palindrome")
