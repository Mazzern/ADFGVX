import math
import re
from datetime import datetime
from mymodule import *

def main(cipher_data, key, time_seed):

    table = build_table(time_seed)
    key_rank, key_len = make_key(key)

    cipher_data_len = len(cipher_data)

    r = 1
    p = 0
    if cipher_data_len % key_len == 0:
        decrypt_table = [['' for i in range(key_len)] for j in range(cipher_data_len // key_len)]
        while r <= key_len:
            y = key_rank.index(r)
            for x in range(cipher_data_len // key_len):
                decrypt_table[x][y] = cipher_data[p+x]
            p += cipher_data_len // key_len
            r += 1
    else:
        decrypt_table = [['' for i in range(key_len)] for j in range(cipher_data_len // key_len + 1)]
        while r <= key_len:
            y = key_rank.index(r)
            if y <= cipher_data_len % key_len - 1:
                for x in range(cipher_data_len // key_len + 1):
                    decrypt_table[x][y] = cipher_data[p+x]
                p += cipher_data_len // key_len + 1
            else:
                for x in range(cipher_data_len // key_len):
                    decrypt_table[x][y] = cipher_data[p+x]
                p += cipher_data_len // key_len
            r += 1

    decrypt_list = []
    for i in decrypt_table:
        decrypt_list.extend(i)

    ADFGVX = ('A','D','F','G','V','X')
    raw_data = ''
    for i in range(cipher_data_len):
        if i % 2 == 0:
            x = ADFGVX.index(decrypt_list[i])
            continue
        y = ADFGVX.index(decrypt_list[i])
        raw_data += table[x][y]

    return raw_data

if __name__ == '__main__':
    encrypt_data = str(input('暗号文を入力: '))
    key = str(input('鍵を入力: '))
    time_stamp = math.floor(datetime.strptime(input('タイムスタンプを入力: '), '%Y-%m-%d %H:%M:%S').timestamp())

    key = re.sub('[ -/:-@[-`]', '', key)
    key = key.lower()

    decrypt_data = main(encrypt_data, key, time_stamp)
    print(decrypt_data)
