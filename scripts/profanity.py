from profanity_filter import ProfanityFilter
from PyDictionary import PyDictionary

original = "that's bullshit shit"

def profanity(text):
    dictionary = PyDictionary()

    pf = ProfanityFilter()

    censored = pf.censor(text)

    print(censored)

    oArr = text.split(" ")

    cArr = censored.split(" ")

    censoredList = []

    for i in range(0, len(cArr)):
        if '*' in cArr[i]:
            if oArr[i] not in censoredList:
                censoredList.append(oArr[i])

    if len(censoredList) == 0:
        return "no foul language detected."

    wordDict = {}

    for c in censoredList:
        word = dictionary.meaning(c)
        wordDict[c] = word

    print(len(censoredList))

    string = ''

    for word in wordDict:
        w = str(wordDict[word])
        temp = word + " " + w.replace("{", "").replace("}", "").replace("[", "").replace("]", "")
        string = string + '\n' + '<p>' + temp + '</p>' + '\n'

    return string.replace('\n', '<br>')

print(profanity(original))
