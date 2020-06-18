# Cipher by Andrew Li
# Creates a cipher (public and private key pair)
import secrets

# you can change the number of rounds the cipher goes
ROUNDS = 8

def decode(final_hash):
    hash_len = len(final_hash)

    first_half = int(final_hash[:(hash_len+1)//2], 16)
    second_half = int(final_hash[(hash_len+1)//2:], 16)

    # decrypt
    for _ in range(ROUNDS):

        second_half = first_half ^ second_half
        # switch
        first_half, second_half = second_half, first_half

    original_hex = str(hex(second_half)).lstrip("0x") + str(hex(first_half)).lstrip("0x")

    return original_hex

def to_string(hex):
    # turns hex into string
    return bytes.fromhex(hex).decode("ASCII")

def main():
    msg = "Hello World!"
    pub_key = pvt_key = ""
    empty = "\0"

    # msg to hex and pad it out to make even

    # msg to hex
    pub_key = msg.encode('utf-8').hex()
    msg_len = len(pub_key)


    if msg_len % 2 != 0:
        pub_key += empty.encode('utf-8').hex()

    # random number
    # pvt_key = secrets.token_hex(16)

    # divides into 2 halves
    first_half = int(pub_key[:(msg_len+1)//2], 16)
    second_half = int(pub_key[(msg_len+1)//2:], 16)

    # encrypt
    for _ in range(ROUNDS):

        second_half = first_half ^ second_half
        first_half, second_half = second_half, first_half

    # concat at the end
    final_hash = str(hex(second_half)).lstrip("0x") + str(hex(first_half)).lstrip("0x")

    # debug
    print(final_hash)

    # print
    # print(f"The public key is: {pub_key} ")
    # print(f"The private key is: {pvt_key} ")

    # decode
    original_hex = decode(final_hash)

    print(to_string(original_hex))


if __name__ == "__main__":
    main()
