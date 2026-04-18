import json
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from supabase import create_client
from IPA_Scraper import returnIPA
load_dotenv()
app = Flask(__name__)
from dbFunctions import DB


conn = DB()

# print(conn.check_cache(word="test"))

# assert len(conn.check_cache("test")) > 0
# assert type(returnIPA("en","word")) is list

#dummy data
sampleData = {"language": "en", "transcription": "hə'loʊ"}

# api route
@app.route('/', methods=['GET'])
def get_data():
    # return "hello world"
    lang = request.args.get('lang','en')
    word = request.args.get('word', 'placeholder')
    
    if (not conn.check_cache(word)):
        res = returnIPA(lang, word)
        conn.insert_to_db(res[0], res[1])
        return jsonify(res[0],res[1])
    else:
        temp = conn.check_cache(word)
        return jsonify(temp[0]["word"], temp[0]["transcription"])