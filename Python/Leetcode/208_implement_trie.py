# https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:

    def __init__(self):
        self.root = Node(None)        

    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children.get(c)
            else:
                next_node = Node(c)
                cur_node.children[c] = next_node
                cur_node = next_node
        cur_node.is_end = True
        

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c in cur_node.children:
                cur_node = cur_node.children.get(c)
            else:
                return False
        return cur_node.is_end



    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c in cur_node.children:
                cur_node = cur_node.children.get(c)
            else:
                return False
        return True

        
class Node:
    def __init__(self, val):
        self.val = val
        self.is_end = False
        self.children = dict()
