sentence = input("Please enter a sentence:")
letters_count = {}
for i in sentence:
  counts = sentence.count(i)
  letters_count[i] = counts
print(letters_count)

