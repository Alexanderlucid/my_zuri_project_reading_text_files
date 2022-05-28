def read_file_content():
    # [assignment] Add your code here 
    with open(r'story.txt','r') as file:
        text = file.read()
        

        print(text)
    # return "Hello World"


def count_words():
    wordsCount = {}
    with open(r'story.txt','r') as file:
        text = file.read()
    
    for punc in ",.?":
        text = text.replace(punc, " ")

    text = text.lower()

    text =text.split()

    for word in text:

        wordsCount[word] = wordsCount.get(word, 0) + 1

    print(wordsCount)
    # return {"as": 10, "would": 20}


read_file_content()
count_words()