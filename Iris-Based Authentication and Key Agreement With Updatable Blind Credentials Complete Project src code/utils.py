import os

# Generate a session key
def generate_session_key():
    return os.urandom(16)  # Generates a 128-bit session key
