def to_base5(n: int):
    s = ""
    while n:
        s = str(n % 5) + s
        n //= 5
    return s.zfill(3)


def from_base5(n: str):
    i = 0
    for x in enumerate(n):
        i += int(x[1]) * (5 ** (len(n) - x[0] - 1))
    return i


space_dict = {
    0: " ",
    1: "\u2001",
    2: "\u2003",
    3: "\u2007",
    4: "\u205f",
    # 5: "\u3000",  Bro is too fat
}


def encode_into_message(message: list[str], secret: list[str]):
    secret = [chr(len(secret))] + secret
    secret_encode = [to_base5(ord(x)) for x in secret]
    secret_encode = [int(y) for x in secret for y in to_base5(ord(x))]
    secret_index = 0
    for x in range(0, len(message)):
        if message[x] == " ":
            t = secret_encode[secret_index % len(secret_encode)]
            message[x] = space_dict[t]
            secret_index += 1


def decode_secret(message: list[str]) -> list[str]:
    secret = list()
    for x in range(0, len(message)):
        for dic in space_dict.items():
            if dic[1] == message[x]:
                secret.append(dic[0])
    group = [secret[i : i + 3] for i in range(0, len(secret), 3)]
    grouped = ["".join(map(str, x)) for x in group]
    unbase5 = [chr(from_base5(x)) for x in grouped]
    length = ord(unbase5[0]) + 1
    return unbase5[1:length]


with open("story.txt", "r") as f:
    file_data = f.read()

message = list(file_data)
secret = list("Hi, nice to meet you.")

encode_into_message(message, secret)
secret_decoded = decode_secret(message)
print("".join(secret_decoded))


with open("story.marked", "w") as f:
    f.writelines(message)
