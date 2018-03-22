def make_key(raw_key):
    key_uniq = []
    for i in raw_key:
        if i not in key_uniq:
            key_uniq.append(i)

    key_uniq_sorted = sorted(key_uniq)
    key_len = len(key_uniq)
    key_rank = [0 for i in range(key_len)]

    r = 1
    for i in key_uniq_sorted:
        point = key_uniq.index(i)
        key_rank[point] = r
        r += 1

    return key_rank, key_len
