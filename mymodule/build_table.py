from random import shuffle, seed

def build_table(time_seed):
    seed(time_seed)
    charactors = [chr(i) for i in range(48, 48+10)]
    charactors += [chr(i) for i in range(97, 97+26)]
    shuffle(charactors)
    table = [charactors[i:i+6] for i in range(0, 36, 6)]
    return table
