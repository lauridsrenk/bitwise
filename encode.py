def encode(string):
    return "".join([chr(ord(char) ^ 0b10010) for char in string])
    
if __name__ == "__main__":
    print("Hallo Welt", encode("Hallo Welt"))
    print(encode("Hallo Welt"), encode(encode("Hallo Welt")))