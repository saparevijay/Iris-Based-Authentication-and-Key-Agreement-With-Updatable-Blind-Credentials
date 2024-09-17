import os
from Crypto.PublicKey import RSA

# Global Setup for the server
def global_setup(security_parameter):
    pp = {'security_param': security_parameter}
    mk = RSA.generate(2048)
    return pp, mk

# Recording the client registration request
def record_registration(Reg, credential_db):
    if Reg['iris_code'] in credential_db:
        return 0  # Already registered
    else:
        credential_db.append(Reg['iris_code'])
        return 1  # Successfully registered

# Creating server response after receiving a client request
def create_response(credential_db, Req):
    if Req['iris_code'] in credential_db:
        KIDC = os.urandom(16)  # 128-bit session key
        Res = {'status': 'success'}
    else:
        Res = {'status': 'failure'}
        KIDC = None
    return Res, KIDC

# Updating the server database and possibly master key
def update_db(credential_db, mk):
    new_mk = RSA.generate(2048)
    pp_new = {'security_param': 2048}
    return pp_new, credential_db, new_mk
