import math
import re
from time import time
from datetime import datetime
from mymodule import *

def main(raw_data, key):

    time_seed = math.floor(time())
    table = build_table(time_seed)
    key_rank, key_len = make_key(key)

    ADFGVX = ('A','D','F','G','V','X')
    subst_data = []
    for i in raw_data:
        for x in range(6):
            for y in range(6):
                if table[x][y] == i:
                    subst_data.append(ADFGVX[x])
                    subst_data.append(ADFGVX[y])

    if len(subst_data) % key_len != 0:
        subst_data += ['' for i in range(key_len - (len(subst_data) % key_len))]

    subst_data2x = [subst_data[i:i+key_len] for i in range(0,len(subst_data),key_len)]

    cipher_data = ''
    r = 1
    while r <= key_len:
        y = key_rank.index(r)
        for x in range(len(subst_data2x)):
            cipher_data += subst_data2x[x][y]
        r += 1

    return cipher_data, time_seed

if __name__ == '__main__':
    message = str(input('メッセージを入力: '))
    key = str(input('鍵を入力: '))

    message = re.sub('[ -/:-@[-`]', '', message)
    key = re.sub('[ -/:-@[-`]', '', key)

    message = message.lower()
    key = key.lower()

    encrypt_data, time_stamp = main(message, key)
    print(datetime.fromtimestamp(time_stamp))
    print(encrypt_data)
