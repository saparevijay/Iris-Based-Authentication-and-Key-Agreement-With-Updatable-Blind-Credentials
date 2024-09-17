# In-memory database for storing registered clients
credential_db = []

# Function to add data to the database
def add_to_db(iris_code):
    credential_db.append(iris_code)

# Function to check if a client exists in the database
def is_registered(iris_code):
    return iris_code in credential_db
