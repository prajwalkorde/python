from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['employee']
collection = db['empinfo']

# Function to add documents
def add_documents():
    documents = [
        {"name": "John", "age": 30, "position": "Manager", "salary": 50000},
        {"name": "Jane", "age": 25, "position": "Developer", "salary": 60000},
        {"name": "Mike", "age": 35, "position": "Analyst", "salary": 55000},
        {"name": "Sara", "age": 28, "position": "Designer", "salary": 52000},
        {"name": "Tom", "age": 40, "position": "Director", "salary": 70000}
    ]
    result = collection.insert_many(documents)
    print(f"Documents inserted with _ids: {result.inserted_ids}")

# Aggregation pipeline to calculate the average salary
pipeline = [
    {
        '$group': {
            '_id': None,
            'average_salary': {'$avg': '$salary'}
        }
    }
]

# Execute the aggregation pipeline
def calculate_average_salary():
    result = list(collection.aggregate(pipeline))
    if result:
        average_salary = result[0]['average_salary']
        print(f"The average salary of employees is: {average_salary}")
    else:
        print("No data found.")

# Example usage
if __name__ == "__main__":
    # Add documents to the collection
    add_documents()

    # Calculate the average salary
    calculate_average_salary()
