from flask import Flask, render_template, request
import text2emotion as te

app = Flask(__name__)


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

            return render_template('app.html', sum=mood)

        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
