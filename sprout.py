# Based on https://github.com/MJL85/seedpart

# WARNING:
#   Do not use this on real seed phrases!
#   This is a hobby project and proof-of-concept 

from wordlist import bip39 as bip39
import random


def getrandomphrase():
    # Remember the random phrase is Shard 1!
    # This is *NOT* BIP39 compliant/valid!
    i = 0
    d = []
    random_phrase = []
    while i < 24:
        n = random.randint(0, 2047)
        if n in d:
            i -= 1
        else:
            d.append(n)
        i += 1
    for n in d:
        random_phrase.append(bip39[n])
    return random_phrase


def getwordindexes(wordlist):
    word_index = []
    for word in wordlist:
        word_index.append(bip39.index(word))
    return word_index


def getwords(indexlist):
    word_list = []
    for word in indexlist:
        word_list.append(bip39[word])
    return word_list


def straightXOR(index_list1, index_list2):
    new_index = []
    w = 0
    while w < 24:
        x = index_list1[w] ^ index_list2[w]
        new_index.append(x)
        w += 1
    word_list = getwords(new_index)
    return word_list


def reverseXOR(index_list1, index_list2):
    new_index = []
    w = 0
    while w < 24:
        y = index_list1[w] ^ index_list2[23 - w]
        new_index.append(y)
        w += 1
    word_list = getwords(new_index)
    return word_list


def split_seed(seed):
    seed_index = getwordindexes(seed)

    # set first shard
    shard1_words = getrandomphrase()

    # Get indexes of first shard
    shard1_index = getwordindexes(shard1_words)

    # set second shard
    shard2_words = straightXOR(seed_index, shard1_index)
    shard2_index = getwordindexes(shard2_words)

    # set third shard
    shard3_words = reverseXOR(shard1_index, shard2_index)
    shard3_index = getwordindexes(shard3_words)  # not needed, but it's there!

    # Put it all together
    split_seed = [shard1_words, shard2_words, shard3_words]
    return split_seed


def recover_seed(s1, s2, w):
    if w == "1 & 2":
        shard1_index = getwordindexes(s1)
        shard2_index = getwordindexes(s2)
    if w == "1 & 3":
        # XOR each number from both shards to generate a third shard. For both shards start with the first word.
        # Reverse the list generated from the previous step.
        shard1_index = getwordindexes(s1)
        shard3_index = getwordindexes(s2)
        shard2 = straightXOR(shard1_index, shard3_index)
        shard2.reverse()  # Because it's backward
        shard2_index = getwordindexes(shard2)

    if w == "2 & 3":
        shard2_index = getwordindexes(s1)
        shard3_index = getwordindexes(s2)

        shard1 = reverseXOR(shard3_index, shard2_index)
        shard1_index = getwordindexes(shard1)

    # Final Step
    seed_phrase = straightXOR(shard1_index, shard2_index)
    return seed_phrase
