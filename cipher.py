# Cipher by Andrew Li
# Creates a cipher (public and private key pair)



def main():
    msg = "Hello World!"
    pub_key = pvt_key = ""

    # msg to binary and pad it out to 256 bit chunks
    check_size = 32
    msg_len = len(msg)
    # msg = [map(bin, bytearray(msg))]

    # encrypt


    # debug
    print(bytearray(msg, 'utf-8'))

    # print
    # print(f"The public key is: {pub_key} ")
    # print(f"The private key is: {pvt_key} ")


if __name__ == "__main__":
    main()
