import json
from difflib import get_close_matches

with open("data.json") as file:
    data = json.load(file)
# print(data['Ram'])

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        a = input(f"Did you mean {get_close_matches(word,data.keys())[0]},Y if yes , N if no:")
        if a=='Y' or a=='y':
            return data[get_close_matches(word,data.keys())[0]]
        elif a=='N' or a=='n':
            return f"{word} doesn't exist"
    else:
        return f"{word} doesn't exist, please double check it."

# print(get_close_matches("rainn",data.keys(),n=1))

word = input("Enter word: ")
output = translate(word)
# print(item for  item in output)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)