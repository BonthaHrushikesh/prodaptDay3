add = lambda x, y: x + y
result = add(5, 3)
print(result)                                   

find_largest_word=lambda sentence: max(sentence.split(), key=len)
sentence = input("Enter a sentence: ")  
largest_word = find_largest_word(sentence)
print("The largest word is:", largest_word)


text = input("Enter a string: ")
result = find_longest_word(text)
print("The longest word is:", result)

sentence = input("Enter a sentence: ")
#start time
import time
start_time = time.perf_counter()

#end time
end_time = time.perf_counter()