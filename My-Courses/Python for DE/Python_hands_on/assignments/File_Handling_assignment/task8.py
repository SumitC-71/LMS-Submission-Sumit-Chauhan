'''
Task 8: Word Count
    1. Create a file named paragraph.txt and add a paragraph of your choice.
    2. Write a Python program to:
        ○ Count the total number of words in the file.
        ○ Count the occurrences of a specific word entered by the user
'''

filename='paragraph.txt'

# writing a random paragraph
with open(filename,'w') as wf:
    wf.write(
        "She never liked cleaning the sink.\n"
        "It was beyond her comprehension how it got so dirty so quickly.\n"
        "It seemed that she was forced to clean it every other day.\n"
        "Even when she was extra careful to keep things clean and orderly, it still ended up looking like a mess in a couple of days.\n"
        "What she didn't know was there was a tiny creature living in it that didn't like things neat.\n"
    )

word_dic={}
with open(filename,'r') as rf:
    total_words=0
    for row in rf:
        # spliting row by spaces to create word list
        word_list = row.split(' ')
        # filtering empty strings
        word_list = list(filter(lambda string: string != '',word_list))

        # counting total words
        total_words += len(word_list)

        # counting frequencies
        for word in word_list:
            word_dic[word] = word_dic.get(word, 0) + 1
            # print(type(word))

    print(total_words)
    for word,occurence in word_dic.items():
        print(f'{word}: {occurence}')
