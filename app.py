from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

try:
    client = MongoClient(config["MONGODB_URL"])
    db = client["dictionary_lookup_cli"]
    dictionary_collection = db["dictionary"]
except Exception as e:
    print(f"\nError connecting to database: {e}")
    exit(1)

class Dictionary:
    def __init__(self, word = None, add_word = None, meaning = None):
        self.word = word
        self.add_word = add_word
        self.meaning = meaning
        self.data = None
    
    def search_word(self):
        if not self.word:
            print("\nPlease enter word, Try again")
            return
        self.data = dictionary_collection.find_one({"word": self.word})
        if not self.data:
            print("\nWord is not found in dictionary, Try another word.")
            return
        
        print(f"\n{"*"*30} Word {"*"*30}")
        print(f"Word: {self.data["word"]}")
        print(f"Meaning: {self.data["meaning"]}")

    def new_word(self):
        if not self.add_word or not self.meaning:
            print("\nPlease enter both word and meaning to proceed. Try again.")
            return
        
        self.data = dictionary_collection.insert_one({"word": self.add_word, "meaning": self.meaning})
        if not self.data:
            print("\nFailed to add word to the dictionary. Try again.")
        else:
            print("\nWord added successfully")

def main():
    while True:
        print(f"\n{"*"*30} Dictionary Lookup {"*"*30}")
        print("1. Search Word in Dictionary.")
        print("2. Add New Word in Dictionary.")
        print("0. Exit App.")
        choice = input("\nEnter your choice: ")

        match choice:
            case "1":
                word = input("\nEnter word: ")
                dictionary = Dictionary(word = word.strip().lower())
                dictionary.search_word()
            case "2":
                add_word = input("\nAdded new word in dictionary: ")
                meaning = input("Enter word meaning: ")
                dictionary = Dictionary(add_word = add_word.strip().lower(), meaning = meaning.strip())
                dictionary.new_word()
            case "0":
                break
            case _:
                print("\nInvalid choice, Try again")

if __name__ == "__main__":
    main()