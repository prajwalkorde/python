from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['employee']
collection = db['empinfo']

# Function to add documents
def add_documents():
    documents = [
        {"name": "John", "age": 30, "position": "Manager"},
        {"name": "Jane", "age": 25, "position": "Developer"},
        {"name": "Mike", "age": 35, "position": "Analyst"},
        {"name": "Sara", "age": 28, "position": "Designer"},
        {"name": "Tom", "age": 40, "position": "Director"}
    ]
    result = collection.insert_many(documents)
    print(f"Documents inserted with _ids: {result.inserted_ids}")

# Function to read documents
def read_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)

# Function to update a document
def update_document(query, new_values):
    result = collection.update_one(query, {'$set': new_values})
    print(f"Documents matched: {result.matched_count}, Documents modified: {result.modified_count}")

# Function to delete a document
def delete_document(query):
    result = collection.delete_one(query)
    print(f"Documents deleted: {result.deleted_count}")

# Example usage
if __name__ == "__main__":
    # Add documents to the collection
    add_documents()

    # Read documents from the collection
    print("Reading documents:")
    read_documents()

    # Update a document in the collection
    query = {"name": "John"}
    new_values = {"age": 31}
    update_document(query, new_values)

    # Read documents again to see the update
    print("Reading documents after update:")
    read_documents()

    # Delete a document from the collection
    delete_document(query)

    # Read documents again to see the deletion
    print("Reading documents after deletion:")
    read_documents()
