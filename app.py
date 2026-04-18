import json
import os
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from supabase import create_client
from IPA_Scraper import returnIPA
load_dotenv()
app = Flask(__name__)
from dbFunctions import DB

allowed_origins = [
    "http://localhost:5173",
    "https://cen4010-finalproject.onrender.com"
]

CORS(app, resources={r"/*": {"origins": allowed_origins}})
conn = DB()

# print(conn.check_cache(word="test"))


#dummy data
sampleData = {"language": "en", "transcription": "hə'loʊ"}

# api route
@app.route('/', methods=['GET'])
def get_data():
    lang = request.args.get('lang','en')
    word = request.args.get('word', 'placeholder')
    
    # sneaky caching system, def not optimal but it works
    if (not conn.check_cache(word)):
        res = returnIPA(lang, word)
        conn.insert_to_db(res[0], res[1])
        return jsonify(res[0],res[1])
    else:
        temp = conn.check_cache(word)
        return jsonify(temp[0]["word"], temp[0]["transcription"])