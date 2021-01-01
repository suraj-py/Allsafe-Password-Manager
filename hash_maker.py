import bcrypt

# hashing plaintext pasword
def hash_password(plaintext):
    encode = plaintext.encode('utf-8')
    pwhash = bcrypt.hashpw(encode, bcrypt.gensalt())
    hashed = pwhash.decode('utf-8')
    return hashed

# checking plaintext password with hashed password
def get_hash_password(plaintext, hash_password):
    encode = plaintext.encode('utf-8')
    decode = hash_password.encode('utf-8')
    check = bcrypt.checkpw(encode, decode)
    return check

# converting tuple to string
def convertTuple(tup):
    str = ''.join(tup)
    return str
