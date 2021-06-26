from flask import Flask, render_template, request
import text2emotion as te
from profanity_filter import ProfanityFilter
from PyDictionary import PyDictionary

app = Flask(__name__)


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

    string = ''

    for word in wordDict:
        w = str(wordDict[word])
        temp = word + " " + w.replace("{", "").replace("}", "").replace("[", "").replace("]", "")
        string = string + '\n' + temp + '\n'

    return string


def getMood(text):
    emotion = te.get_emotion(text)

    highScore = 0
    mood = ''

    for e in emotion:
        score = emotion[e]
        if score > highScore:
            highScore = score
            mood = e

    return mood


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':

        operation = request.form['text']

        print(operation)

        if operation != '':

            mood = getMood(operation)

            censor = profanity(operation)

            print(censor)

            string = "Your words give off this mood: " + mood + '\n' + "Your words may or may not contain offensive language. If the former. Below is/are the meaning of these words " + str(censor)

            return render_template('app.html', sum=string)

        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
