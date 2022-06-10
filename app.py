from flask import Flask, request, jsonify
from flask_cors import CORS
import sys

app = Flask(__name__)

tweets = [ 
    "Sick of having to go to 2 different huts to buy pizza & sunglasses.", 
    "Waabalubbadubbdub", "This is the most annoying part of the assignment",
    "I hate applying concepts from my English high school experiences",
    "Meh, directing my dislike for creating content towards creating content seems to be working",
    "I hope I am doing this first step correctly...",
    "MMMMM pretty sure six isn't enough tweets yet, well here's seven then!",
    "Thankful for machines and how I hopefully won't have to re-type this nonsense a million times!!!",
    "You know, I'm sure I could have just done shorter quotes...",
    "True!"
]

@app.get('/api/tweets')
def tweets_get():
    args = request.args
    
    #tweetId
    tweet_Id = args.get('tweetId')
    if tweet_Id == None:
        return jsonify(tweets), 200
    else:
        return jsonify(tweets[tweet_Id]), 200


if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print("Missing required argument: testing|production")
    exit()

if mode == "testing":
    CORS(app)
    app.run(debug=True)
elif mode == "production":
    import bjoern
    bjoern.run(app, "0.0.0.0", 5000)
else:
    print("Invalid mode, must be one of: testing|production")
    exit()