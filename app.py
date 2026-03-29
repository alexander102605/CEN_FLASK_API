import json
from flask import Flask, jsonify, request

app = Flask(__name__)

sampleData = {"language": "en", "transcription": "hə'loʊ"}

def webScrape(lang, result):
    pass


@app.route('/api', methods=['GET'])
def get_data():
    lang = request.args.get('lang', 'en')
    transcript = request.args.get("word", "placeholder")
    result = webScrape(lang, transcript)

    return jsonify(sampleData)