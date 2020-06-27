
#Import Files
from flask import Flask, redirect, render_template, request, url_for

import os
import sys
import helpers
from analyzer import Analyzer
import nltk
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")

    if screen_name == None:
        return redirect(url_for("index"))

    # get screen_name's tweets


    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)

    tweets = helpers.get_user_timeline(screen_name,100)


    if tweets == None:
        return redirect(url_for("index"))

    red_score = 0.0
    yellow_score = 0.0
    green_score = 0.0

    for t in tweets:
        fscore = analyzer.analyze(t)        #Analyze every tweet and score it

        if fscore > 0:
            green_score+=1.0
        elif fscore < 0 :
            red_score+=1.0
        else:
            yellow_score+=1.0


    # TODO

    # generate chart
    chart = helpers.chart(green_score,red_score, yellow_score)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)


"""
Consumer Key (API Key)	qvEyC4gardegk4R511NtX8iDT
Consumer Secret (API Secret)	Hjiiu1ZfuAGoPr4gVVkGyFXVKRbRjO991SwHS0zIidfAiilf55


export API_KEY=qvEyC4gardegk4R511NtX8iDT
export API_SECRET=Hjiiu1ZfuAGoPr4gVVkGyFXVKRbRjO991SwHS0zIidfAiilf55
"""