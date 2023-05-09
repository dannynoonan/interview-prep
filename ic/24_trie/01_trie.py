# 01
# Hard

# Implement a Trie with insertion, search and deletion operations.


# -----------------------------------------------------

# Time Complexity: O(n) for all operations, where n is the length of the word.
# Space Complexity: Search: O(1), Insert: O(n) for storing new nodes, Delete: O(1)

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.next_nodes = {}
        self.is_word = False

    def __repr__(self) -> str:
        out = f"{self.char} next={[k for k,v in self.next_nodes.items()]}"
        if self.is_word:
            out = f"{out} [W]"
        return out


class Trie(object):
    def __init__(self):
        self.root = TrieNode('ROOT')

    def contains(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.next_nodes:
                node = node.next_nodes[c]
            else:
                return False
        return node.is_word

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c in node.next_nodes:
                node = node.next_nodes[c]
            else:
                node.next_nodes[c] = TrieNode(c)
                node = node.next_nodes[c]
                node.is_word = False
        node.is_word = True

    def delete(self, word: str) -> bool:
        node = self.root
        clipped_end = None
        for c in word:
            if c in node.next_nodes:
                if len(node.next_nodes) == 1 and node.is_word:
                    clipped_end = node
                node = node.next_nodes[c]
            else:
                return False
        if clipped_end:
            clipped_end.next_nodes = {}
            return True
        if node.is_word:
            node.is_word = False
            return True
        return False

# -----------------------------------------------------

import pytest

def test_trie():
    t = Trie()
    t.insert('map')
    t.insert('mar')
    t.insert('mark')
    t.insert('market')
    t.insert('mart')

    assert(t.contains('market'))
    assert(not t.contains('marker'))

    assert(t.contains('mart'))
    t.delete('mart')
    assert(not t.contains('mart'))
    assert(t.contains('market'))

    t.delete('market')
    assert(not t.contains('market'))
    assert(t.contains('mark'))

    t.insert('marker')
    assert(t.contains('marker'))

pytest.main()
