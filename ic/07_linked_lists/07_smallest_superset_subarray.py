# 07 
# Hard

# Smallest Subarray Covering All Values: 
# Let's say you are given a large text document Doc. You are also given a set S of words. 
# You want to find the smallest substring of Doc that contains all the words in S. For example:

# S: ["and", "of", "one"]

# Doc: "a set of words that is complete in itself, typically containing a subject and predicate,
# conveying a statement, question, exclamation, or command, and consisting of a main clause and
# sometimes one or more subordinate clauses"

# Solution: "of a main clause and sometimes one" 

# Note that the order in which the words appear doesn't matter. 
# Also, the length of the substring is in terms of number of characters.


# -----------------------------------------------------

# Time Complexity: O(Doc.charCount)
# We iterate through the entire doc, and we do O(1) work at each step.
# Space Complexity: O(Doc.charCount)
# In the worst case, the result might contain the entire Doc.

class Node(object):
    def __init__(self, word: str):
        self.word = word
        self.start_i = None
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"{self.word}:{self.start_i}"

class LinkedList(object):
    def __init__(self):
        self.earliest = None
        self.latest = None

    def __repr__(self):
        out = ""
        n = self.earliest
        while n:
            out = "{out}{n}"
            if n.next:
                out = "{out}->"
        return out

    def add_latest(self, node: Node) -> None:
        if not self.latest:
            self.latest = node
            self.earliest = node
        else:
            self.latest.next = node
            node.prev = self.latest
            self.latest = node

    def move_to_latest(self, node: Node) -> None:
        if node == self.latest:
            return
        if node == self.earliest:
            self.earliest = self.earliest.next
            self.earliest.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.add_latest(node)

class LinkedHashMap(object):
    def __init__(self, words: list):
        self.words = words
        self.word_ll = LinkedList()
        self.word_map = {}
        self.shortest_span = None
        self.earliest_start_i = None
        self.latest_end_i = None

    def calc_span(self) -> tuple[int, int, int]:
        if len(self.word_map) < len(self.words):
            print(f"Only {len(self.word_map)} words have been seen.  Shortest span cannot be calculated until all words have been seen")
            return
        earliest_word = self.word_ll.earliest.word
        earliest_node = self.word_map[earliest_word]
        latest_word = self.word_ll.latest.word
        latest_node = self.word_map[latest_word] 
        latest_end_i = latest_node.start_i + len(latest_word)
        span = latest_end_i - earliest_node.start_i
        return span, earliest_node.start_i, latest_end_i

    def process_word(self, word: str, word_i: int) -> None:
        if word not in self.words:
            return
        if word in self.word_map:
            word_node = self.word_map[word]
            word_node.start_i = word_i
            self.word_ll.move_to_latest(word_node)
        else:
            word_node = Node(word)
            word_node.start_i = word_i
            self.word_ll.add_latest(word_node)
            self.word_map[word] = word_node
        span = self.calc_span()
        if span and (not self.shortest_span or span[0] < self.shortest_span):
            self.shortest_span = span[0]
            self.earliest_start_i = span[1]
            self.latest_end_i = span[2]

def smallest_superset_subarray(text_blob: str, target_words: list) -> str:
    lhm = LinkedHashMap(target_words)
    text_blob_words = text_blob.split(' ')
    word_i = 0
    for w in text_blob_words:
        lhm.process_word(w, word_i)
        word_i += len(w) + 1
    if not lhm.shortest_span:
        raise Exception(f"Unable to generate smallest_superset_subarray, shortest_span was not set")
    return text_blob[lhm.earliest_start_i:lhm.latest_end_i]
    

# -----------------------------------------------------

import pytest

def test_smallest_superset():
    text_blob = """a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, question, exclamation, or command, and consisting of a main clause and sometimes one or more subordinate clauses"""
    target_words = ["and", "of", "one"]
    assert(smallest_superset_subarray(text_blob, target_words) == "of a main clause and sometimes one")

    text_blob2 = "one of the car and bike and one of those"
    assert(smallest_superset_subarray(text_blob2, target_words) == "and one of")

pytest.main()
