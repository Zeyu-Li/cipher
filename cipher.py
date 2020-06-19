# Feistel Cipher by Andrew Li
# Creates a cipher based on the Feistel cipher (public and private key pair)
import secrets
import math


def code(final_hash, key, rounds):
    # both encodes and decodes
    hash_len = len(final_hash)

    first_half = int(final_hash[:-int(hash_len/2)], 16)
    second_half = int(final_hash[-int(hash_len/2):], 16)

    # decrypt
    for _ in range(rounds):

        second_half, key = hash_function(second_half, key)
        first_half = first_half ^ second_half

        # switch
        first_half, second_half = second_half, first_half

    first_part = str(hex(second_half)).lstrip("0x") 
    second_part = str(hex(first_half)).lstrip("0x")

    # sometimes 0 is omitted so watch out
    # there may be more bugs here relating to this :(
    while len(first_part) != int(hash_len/2):
        first_part += "0"

    while len(second_part) != int(hash_len/2):
        second_part = "0" + second_part

    return first_part + second_part, key

def hash_function(hash, key):
    # takes a hex and transforms it
    # If you want to change the hash function, you can do it here

    # hash = hash ^ key

    return hash, key

def to_string(some_hex):
    # turns hex into string

    return bytes.fromhex(some_hex).decode("utf-8")

def main():
    # predefined static message
    msg = "Hello World"

    # you can change the number of rounds the cipher goes
    ROUNDS = 10
    # uncomment if you want message to be inputted
    # msg = str(input("Secret message: "))
    pub_key = pvt_key = ""

    # random number
    pvt_key = int(secrets.token_hex(8).encode('utf-8').hex(), 16)

    # msg to hex
    pub_key = msg.encode('utf-8').hex()

    final_hash, new_key = code(pub_key, pvt_key, ROUNDS)

    # debug
    # print(final_hash)

    # print
    # print(f"The public key is: {pub_key} ")
    # print(f"The private key is: {pvt_key} ")

    # decode
    original_hex, original_key = code(final_hash, new_key, ROUNDS)

    print(f"The secret message was: {to_string(original_hex)}")


if __name__ == "__main__":
    main()
