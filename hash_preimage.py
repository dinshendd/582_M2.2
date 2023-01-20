import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return
    #nonce = b'\x00'

    # generate 64 bits randomly
    nonce = os.urandom(64)
    bits_to_match = ''
    string_len = len(target_string)


    # If input string is empty, generate random bytes
    if string_len == 0:
        return nonce

    while bits_to_match != target_string:

        nonce = os.urandom(64)
        bits = "{0:08b}".format(int(hashlib.sha256(nonce).hexdigest(), 16))
        bits_to_match = bits[-string_len:]


    return( nonce )
