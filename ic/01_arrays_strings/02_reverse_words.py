# 02
# Easy

# Given a sentence, reverse the words of the sentence. 

# For example, "i live in a house" becomes "house a in live i".


# -----------------------------------------------------

# Time Complexity: O(n)
# Space Complexity: O(n)

def reverse_words(sent: str) -> str:
    words = sent.split()
    rev_words = [None] * len(words)
    for i in range(len(words)):
        rev_words[len(words) - 1 - i] = words[i]
    return ' '.join(rev_words)


# -----------------------------------------------------

import pytest

def test_reverse_words():
    sent = "i live in a house"
    rev_sent = "house a in live i"
    assert(reverse_words(sent) == rev_sent)

pytest.main()
