from flask import Flask, render_template, request
app = Flask(__name__)

target = "１０年は待つには長い時間だ。"

answer_gt = "Ten years is a long time to wait."
answer_ai = "Ten years is too long to wait."


@app.route("/")
def input_translation():
    return render_template('translate.html', target=target)


@app.route("/choose", methods=['POST'])
def choose_answer():
    answer_user = request.form['answer']
    answers = {"user": answer_user, "gt": answer_gt, "ai": answer_ai}
    return render_template('choose.html', answers=answers)


@app.route("/result", methods=['POST'])
def show_result():
    return render_template('result.html')
