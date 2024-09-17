# Create the registration request for the client with the iris code
def create_registration(iris_code):
    Reg = {'iris_code': iris_code}
    return Reg

# Create an authentication request for the client
def create_request(iris_code):
    LS = {'iris_code': iris_code}
    Req = {'iris_code': iris_code}
    return LS, Req

# Derive the session key from the server's response
def derive_token(LS, Res, KIDC):
    if Res['status'] == 'success':
        return KIDC  # Return session key
    else:
        return None  # Authentication failed
