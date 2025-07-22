from pymongo import MongoClient, errors

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Function to insert data with exception handling
def insert_data(document):
    try:
        result = collection.insert_one(document)
        print(f"Document inserted with _id: {result.inserted_id}")
    except errors.DuplicateKeyError:
        print("Error: Duplicate key error. The document already exists.")
    except errors.WriteError as e:
        print(f"Write error: {e}")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

# Example usage
document = {"_id": 1, "name": "John", "age": 30, "city": "New York"}
insert_data(document)

# Trying to insert a duplicate document to trigger an error
duplicate_document = {"_id": 1, "name": "Jane", "age": 25, "city": "Los Angeles"}
insert_data(duplicate_document)
