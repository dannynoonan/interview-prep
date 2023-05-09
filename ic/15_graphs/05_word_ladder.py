# 05
# Medium

# Word Ladder Problem: You are given 2 words A and B, both of the same length. Your task is to 
# transform one word to another changing only one letter each time. Each intermediate word should 
# be a valid word in the dictionary. Print out the length of the path. 

# (Alternate version: print out the intermediate words)

# A = CAB, B = DOG
# Result: 4 (CAB -> COB -> COG -> DOG)


# -----------------------------------------------------

# Time Complexity:
# * All Words Approach: O(26^N), because in the worst case, you will go through every word of size n.
# * Optimized Approach: O(N * M), where N is the number of words in the dictionary and M is the length of
# the longest word. This time is taken to build the pre-processing map.
# The BFS takes O(N * M) in this case, where N is the number of words in the dictionary and M is the
# length of the longest word. This happens when we go through all the words.

# Space Complexity:
# * All Words Approach: O(26^N), because we store every node in the queue.
# * Optimized Approach: O(N * M), where N is the number of words in the dictionary and M is the length of
# the longest word. This space is taken on the pre-processing map.

from collections import deque

class WordNode(object):
    def __init__(self, word: str):
        self.word = word
        self.wc_list = [None] * len(word)
        for i in range(len(word)):
            self.wc_list[i] = f"{word[:i]}*{word[i+1:]}"
        self.path = []

    def __repr__(self) -> str:
        return self.word

def generate_wc_map(valid_words: list) -> dict:
    dc = {}
    for w in valid_words:
        wn = WordNode(w)
        for wc in wn.wc_list:
            if wc in dc:
                dc[wc].append(wn.word)
            else:
                dc[wc] = [wn.word]
    return dc

def word_ladder_bfs(start_w: str, target_w: str, valid_words: list) -> list:
    wcs_to_words = generate_wc_map(valid_words)
    start_node = WordNode(start_w)
    start_node.path = [start_w]
    q = deque()
    q.appendleft(start_node)
    while q:
        source_node = q.pop()
        if source_node.word == target_w:
            return source_node.path
        for wc in source_node.wc_list:
            for word in wcs_to_words[wc]:
                if word in source_node.path:
                    continue
                word_node = WordNode(word)
                # NOTE: this is where I've made the same mistake a couple times: lists are passed by reference, unless mutated during course of assignment as below
                word_node.path = source_node.path + [word_node.word]
                q.appendleft(word_node)

# -----------------------------------------------------

import pytest

def test_word_ladder():
    valid_words = ['dog', 'dot', 'cog', 'dig', 'fog', 'bog', 'cop', 'cob', 'con', 'did', 'fig', 'pig', 'big', 'can', 'ton', 'top', 'dad', 'dud', 'pin', 'fin', 'bin', 'ban', 'pan', 'tap', 'pad', 'tab', 'cab'] 
    start_word = 'dog'
    target_word = 'cab'
    path = ['dog', 'cog', 'cob', 'cab']
    assert(word_ladder_bfs(start_word, target_word, valid_words) == path)

pytest.main()
