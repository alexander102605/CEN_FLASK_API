import json
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from supabase import create_client
load_dotenv()
app = Flask(__name__)

#Connect to Supabase DB
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#DB functions

def read_words():
    return supabase.rpc('ReadWordDB').execute()

def read_IPA():
    return supabase.rpc('ReadIPA').execute()

def insert_to_db(scraped_word):
    supabase.rpc("Insert_word", {"scraped_word":scraped_word}).execute()

#scrape function
def webScrape(lang, result):
    pass

#dummy data
sampleData = {"language": "en", "transcription": "hə'loʊ"}

#api route
@app.route('/api', methods=['GET'])
def get_data():
    lang = request.args.get('lang','en')
    transcript = request.args.get("word", "placeholder")
    scraped_data = webScrape(lang, transcript)
    insert_to_db(sampleData)
    return jsonify(sampleData) #REPLACE WITH REAL DATA