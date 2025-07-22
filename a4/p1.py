import pymongo
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Create a document
def create_document(document):
    result = collection.insert_one(document)
    print(f"Document inserted with _id: {result.inserted_id}")

# Read documents
def read_documents(query={}):
    documents = collection.find(query)
    for doc in documents:
        print(doc)

# Update a document
def update_document(query, new_values):
    result = collection.update_one(query, {'$set': new_values})
    print(f"Documents matched: {result.matched_count}, Documents modified: {result.modified_count}")

# Delete a document
def delete_document(query):
    result = collection.delete_one(query)
    print(f"Documents deleted: {result.deleted_count}")

# Example usage
if __name__ == "__main__":
    # Create a document
    document = {"name": "John", "age": 30, "city": "New York"}
    create_document(document)

    # Read documents
    print("Reading documents:")
    read_documents()

    # Update a document
    query = {"name": "John"}
    new_values = {"age": 31}
    update_document(query, new_values)

    # Read documents again to see the update
    print("Reading documents after update:")
    read_documents()

    # Delete a document
    delete_document(query)

    # Read documents again to see the deletion
    print("Reading documents after deletion:")
    read_documents()
