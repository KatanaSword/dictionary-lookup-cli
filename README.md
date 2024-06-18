# Dictionary Lookup CLI

A command-line interface (CLI) application that allows users to search for words and add new words to a MongoDB-based dictionary.

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/KatanaSword/dictionary-lookup-cli.git
   cd dictionary-lookup-cli
   ```

2. **Create a virtual environment and activate it:**

   ```sh
   python -m venv .venv
   .\.venv\Scripts\activate  # On Mac use `source .venv/bin/activate`
   ```

3. **Install the dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your environment variables:**
   Create a `.env` file in the project root directory and add your [MongoDB](https://www.mongodb.com/cloud/atlas/register) connection string:
   ```
   MONGODB_URL=your_mongodb_connection_string_here
   ```

## Usage

Run the Dictionary Lookup CLI:

```sh
python app.py
```

Follow the on-screen menu to search for a word or add a new word to the dictionary:

1. Search Word in Dictionary
2. Add New Word to Dictionary
3. Exit App

## Environment Variables

MONGODB_URL: Your [MongoDB](https://www.mongodb.com/cloud/atlas/register) connection string for accessing the dictionary collection.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
