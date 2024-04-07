# https://www.acmicpc.net/problem/1786

import sys

def calculate_list_len_prefix_equals_suffix(word: str):
    ps_equals = [0]
    for i in range(1, len(word)):
        cand = ps_equals[i-1]
        while cand > 0 and word[cand] != word[i]:
            cand = ps_equals[cand-1]
        ps_equals.append(cand+1 if word[cand] == word[i] else cand)
    return ps_equals

def kmp(sentence: str, word: str):
    occurence_idx = []
    ps_equals = calculate_list_len_prefix_equals_suffix(word)
    m = 0
    s = 0

    max_m = len(sentence) - len(word) + 1

    while m < max_m:
        while s < len(word) and m < max_m:
            if sentence[m+s] != word[s]:
                if s == 0:
                    m = m+1
                else:
                    m = m+s-ps_equals[s-1]
                    s = ps_equals[s-1]
            else:
                s += 1
        if s == len(word):
            occurence_idx.append(m)
            m = m+s-ps_equals[s-1]
            s = ps_equals[s-1]
    
    return occurence_idx

def main():
    input_ = sys.stdin.readline

    sentence = input_()[:-1]
    word = input_()[:-1]

    occurences = kmp(sentence, word)
    print(len(occurences))
    print(str.join(' ', map(lambda x: str(x+1), occurences)))

main()
