'''str1 = input("Enter a string:")
print(str1[::-1])'''




'''# Get input from the user
sentence = input("Input: ")

# Split the sentence into words, reverse the list, and join them back into a sentence
output = ' '.join(sentence.split()[::-1])

# Print the output
print("Output:", output)'''





sentence = input("Enter:")
list1= sentence.split()
for i in list1[::-1]:
    print(i, end= " ")
