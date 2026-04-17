import json
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from supabase import create_client
from IPA_Scraper import returnIPA
load_dotenv()
app = Flask(__name__)

#Connect to Supabase DB
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#DB functions

def check_cache(word):
    response = (
        supabase.table("words")
        .select("*")
        .eq("word",word)
        .execute()
    )

    return response.data

def insert_to_db(word, transcript):
    response = (
        supabase.table("words")
        .insert({"word": word, "transcription": transcript})
        .execute()
    )
    return response


# print(check_cache("test"))

#dummy data
sampleData = {"language": "en", "transcription": "hə'loʊ"}

# api route
@app.route('/', methods=['GET'])
def get_data():
    # return "hello world"
    lang = request.args.get('lang','en')
    word = request.args.get('word', 'placeholder')
    res = returnIPA(lang, word)

    if (not check_cache(word)):
        insert_to_db(res[0], res[1])

    return jsonify(res[0], res[1]) #REPLACE WITH REAL DATA