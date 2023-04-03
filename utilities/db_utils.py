import pymongo
from urllib.parse import quote
# from bson import ObjectId

# Credentials
password = "veHt1JK5"
encoded_password = quote(password)
user_name = 'qa_agency'
db_name = "trado_qa"

# Function to create MongoDB connection
def create_mongo_connection():
    # Connect to MongoDB using the given credentials and return the database object
    client = pymongo.MongoClient(
        f"mongodb+srv://{user_name}:{encoded_password}@cluster0.qnr3p.mongodb.net/{db_name}?retryWrites=true&w=majority")
    db = client[db_name]
    return db

# Function to test the MongoDB connection
def test_connection(db):
    try:
        db.command("ping")
        print("Connected to MongoDB.")
    except Exception as e:
        print("Error connecting to MongoDB:", e)

# Function to get a list of collection names in the given database
def get_collections(db):
    collections = db.list_collection_names()
    return collections

# Function to display collection names in the given database
def display_collections(db):
    collections = db.list_collection_names()
    print(f'Collections in {db_name}: {collections}')
    return collections

# Function to display document count and an example document for each collection in the given database
def display_samples(db):
    collections = get_collections(db)
    for i in collections:
        sample_collection = db[i]
        document_count = sample_collection.count_documents({})
        print(f"There are {document_count} documents in the {i} collection.")
        print(f'Example data set: {sample_collection.find_one()}')

# Function to display all documents in a given collection
def display_all_documents_in_a_collection(db, collection_name):
    collection = db[collection_name]
    documents = collection.find()
    for document in documents:
        print(document)

def get_random_product(db):
    product_collecton = db["products"]
    all_products = product_collecton.find()
    return all_products[0]

def get_login_code(db, phone):
    user_collection = db["users"]
    user = user_collection.find_one({"phone": phone})
    return user.get("loginCode")

def is_user_in_db(db, phone):
    user_collection = db["users"]
    user = user_collection.find_one({"phone": phone})
    if user:
        return True
    else:
        return False

def get_user_details(db, phone):
    user_collection = db["users"]
    user = user_collection.find_one({"phone": phone})
    if user:
        return user
    else:
        return None

def get_user_first_name(db, phone):
    user = get_user_details(db, phone)
    return user.get("firstName")

def get_user_last_name(db, phone):
    user = get_user_details(db, phone)
    return user.get("lastName")

def get_user_city(db, phone):
    user = get_user_details(db, phone)
    address = user.get("address")
    city = address.get("city")
    return city

def get_user_home_number(db, phone):
    user = get_user_details(db, phone)
    address = user.get("address")
    building = address.get("building")
    return building


    # db is the connection object to mongo
def is_product_in_db(db, barcode):
    product_collection = db["products"]
    product = product_collection.find_one({"barcode": barcode})
    if product:
        return True
    else:
        return False



def count_users_by_phone_number(db, phone):
    users_count = db.users.count_documents({"phone": phone})
    return users_count

# Function to get the value of a specific key in a document identified by its ID in a given collection
# def get_specific_key_value(db, collection_name, document_id, key):
#     collection = db[collection_name]
#     document = collection.find_one({'_id': ObjectId(document_id)})
#     if document:
#         value = document.get(key)
#         return value
#     else:
#         return None

# The function we used
def get_specific_document(db, collection_name, key, value):
    collection = db[collection_name]
    document = collection.find_one({key: value})
    if document:
        return document
    else:
        return None

# Function to count the documents with a specific key-value pair in a given collection
def count_key_value(db, collection_name, key, value):
    collection = db[collection_name]
    count = collection.count_documents({key: value})
    return count

# Function to get the distinct values of a specific key in a given collection
def get_distinct_key_values(db, collection_name, key):
    collection = db[collection_name]
    distinct_values = collection.distinct(key)
    return distinct_values

# Function to test the stock status of products in the 'products' collection
def test_product_stock(db):
    products = db['products']
    out_of_stock_products = products.count_documents({"productStock": 0})
    print(f"There are {out_of_stock_products} out-of-stock products.")

# Function to test the order status in the 'orders' collection
def test_orders(db):
    orders = db['orders']
    pending_orders = orders.count_documents({"status": "ready"})
    print(f"There are {pending_orders} ready orders.")

# Main function
def main():
    db = create_mongo_connection(user_name, encoded_password, db_name)
    test_connection(db)
    display_collections(db)

    # Main menu
    while True:
        print("\n--- Main Menu ---")
        print("1. Display sample documents")
        print("2. Display all documents in a collection")
        print("3. Get specific key-value")
        print("4. Count key-value pairs")
        print("5. Get distinct key values")
        print("6. Test product stock")
        print("7. Test order status")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_samples(db)
        elif choice == "2":
            collection_name = input("Enter collection name: ")
            display_all_documents_in_a_collection(db, collection_name)
        elif choice == "3":
            collection_name = input("Enter collection name: ")
            document_id = input("Enter document ID: ")
            key = input("Enter key: ")
            value = get_specific_key_value(db, collection_name, document_id, key)
            print(f"The {key} for document with ID '{document_id}' is: {value}")
        elif choice == "4":
            collection_name = input("Enter collection name: ")
            key = input("Enter key: ")
            value = input("Enter value: ")
            count = count_key_value(db, collection_name, key, value)
            print(f"There are {count} documents with '{key}': '{value}'.")
        elif choice == "5":
            collection_name = input("Enter collection name: ")
            key = input("Enter key: ")
            distinct_values = get_distinct_key_values(db, collection_name, key)
            print(f"The distinct {key} values in {collection_name} are: {distinct_values}")
        elif choice == "6":
            test_product_stock(db)
        elif choice == "7":
            test_orders(db)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()