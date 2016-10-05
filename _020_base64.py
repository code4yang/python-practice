import base64


def encode_file(file_name='test.pcm'):
    file = open(file_name, mode='br')
    a = file.read()
    print(a)
    print(base64.encodebytes(a))


if __name__ == '__main__':
    encode_file()
