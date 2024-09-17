from server import global_setup, record_registration, create_response, update_db
from client import create_registration, create_request, derive_token
from database import credential_db
import utils
from iris_recognition import extract_iris_code

def main():
    # Step 1: Server global setup
    pp, mk = global_setup(2048)
    print("Global setup complete. Public Parameters and Master Key initialized.")

    # Step 2: Client registration
    client_iris_code = extract_iris_code()
    Reg = create_registration(client_iris_code)
    registration_status = record_registration(Reg, credential_db)

    if registration_status == 1:
        print("Registration successful!")
    else:
        print("Client already registered.")

    # Step 3: Client authentication request
    LS, Req = create_request(client_iris_code)

    # Step 4: Server responds to the request
    Res, KIDC = create_response(credential_db, Req)
    if Res['status'] == 'success':
        print("Authentication successful! Session key:", KIDC.hex())
    else:
        print("Authentication failed.")

    # Step 5: Client derives the session key
    session_key = derive_token(LS, Res, KIDC)
    if session_key:
        print("Session key derived by the client:", session_key.hex())
    else:
        print("Session key derivation failed.")

    # Step 6: Server database update
    pp_new, credential_db_new, new_mk = update_db(credential_db, mk)
    print("Database and master key updated.")

if __name__ == '__main__':
    main()
