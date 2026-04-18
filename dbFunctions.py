import supabase
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

# good practice? in my code... no way
class DB:
    def __init__(self):
        self.SUPABASE_URL = os.getenv("SUPABASE_URL")
        self.SUPABASE_KEY = os.getenv("SUPABASE_KEY")
        self.connection = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def check_cache(self, word):
        response = (
            self.connection.table("words")
            .select("*")
            .eq("word",word)
            .execute()
        )
        return response.data
    

    def insert_to_db(self, word, transcript):
        response = (
            self.connection.table("words")
            .insert({"word": word, "transcription": transcript})
            .execute()
        )
        return response
    
    # only really exists for unit testing
    def pull_cache(self):
        response = (
            self.connection.table("words")
            .select("*")
            .range(0,10)
            .execute()
        )
        return response.data
    