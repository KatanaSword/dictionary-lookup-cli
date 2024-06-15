from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = MongoClient(os.getenv("MONGODB_URL"))
    db = client["dictionary_lookup_cli"]
    collection = db["dictionary"]
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

def main():
    while True:
        print(f"\n{"*"*"30"} Dictionary Lookup {"*"*"30"}")
        print("1. Search Word in Dictionary.")
        print("2. Add New Word in Dictionary.")
        print("0. Exit App.")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                word = input("Enter word: ")
                search_word(word)
            case "2":
                add_word = input("Added new word in dictionary: ")
                meaning = input("Enter word meaning: ")
                new_word(add_word, meaning)
            case "0":
                break
            case _:
                print("Invalid Entry, Try again")

if __name__ == "__main__":
    main()