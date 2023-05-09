# 09
# Medium

# Word Break Problem: Given a String S, which contains letters and no spaces, find 
# if it can be broken it into valid words. Return one such combination of words. 
# Assume you are provided a dictionary of English words.

# For example:
# S = "ilikemangotango"
# Output: any one of the following:
# "i like mango tango"
# "i like man go tan go"
# "i like mango tan go"
# "i like man go tango"


# -----------------------------------------------------

# Time Complexity:​ O(n^​2​) with memoization, because we go over each substring at most once
# Space Complexity:​ O(n) with memoization - both on the memo and on the recursion stack

valid_words = ['i', 'like', 'mango', 'tango', 'man', 'goo', 'tan', 'got', 'an', 'thin', 'think', 'ink', 'about', 'bout', 'out', 'tit', 'it', 'arm', 'karma', 'do', 'ado', 'dog', 'armada', 'a', 'dab', 'on', 'bonk']
s1 = "ilikemangotango"
s2 = "thinkarmadog"
s3 = "thinkaboutit"
s4 = "thinkarmadabonk"
s5 = "thinkarmadabone"

def word_break_main(s: str) -> bool:
    fail_starts = [False] * len(s)
    if word_break(s, 0, [], fail_starts):
        print(f"s={s} successfully parsed")
        return True
    else:
        print(f"s={s} failed to parse")
        return False

def word_break(s: str, s_i: int, words: list, fail_starts: list) -> bool:
    if s_i == len(s):
        print(f">> Success! words={words}")
        return True
    if not fail_starts[s_i]:
        w_buf = []
        for i in range(s_i, len(s)):
            w_buf.append(s[i])
            word = ''.join(w_buf)
            if word in valid_words:
                words.append(word)
                if word_break(s, i+1, words, fail_starts):
                    return True
                failed_word = words.pop()
                # print(f"failed_word={failed_word}")
                w_buf = [c for c in failed_word]
                fail_starts[i+1] = True
    return False

# -----------------------------------------------------

word_break_main(s1)
word_break_main(s2)
word_break_main(s3)
word_break_main(s4)
word_break_main(s5)
    