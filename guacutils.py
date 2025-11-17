def encode(*args):
    return ",".join(f"{len(a)}.{a}" for a in args) + ";"

def decode(msg: str):
    decode_str = msg[:-1]
    decode_list = decode_str.split(",")
    result = []

    for i in decode_list:
        split = i.split(".")
        result.append(split[1][:int(split[0])])
    
    return result