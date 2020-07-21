# 【中等】208. 实现 Trie (前缀树)
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。


# 非树结构
# class Trie:
#     def __init__(self):
#         self.words = []

#     def insert(self, word: str) -> None:
#         self.words.append(word)

#     def search(self, word: str) -> bool:
#         return word in self.words

#     def startsWith(self, prefix: str) -> bool:
#         for word in self.words:
#             if word.startswith(prefix): return True
#         return False


class TreeNode:
    def __init__(self, val, isEnd):
        self.val = val
        self.isEnd = isEnd
        self.links = []

class Trie:
    def __init__(self):
        self.root = TreeNode('', False)

    def insert(self, word: str) -> None:
        ele = self.root
        isInsert, isContinue = False, True
        while ele.links and isContinue:
            isContinue = False
            for i in range(len(ele.links)):
                link = ele.links[i]
                if link.val[0] == word[0]:
                    if link.val == word:
                        link.isEnd = True
                        isInsert = True
                    elif link.val.__contains__(word):
                        link.val = link.val[len(word):]
                        temp = TreeNode(word, True)
                        temp.links.append(link)
                        ele.links.pop(i)
                        ele.links.append(temp)
                        isInsert = True
                    elif word.__contains__(link.val):
                        word = word[len(link.val):]
                        ele = link
                        isContinue = True
                    else:
                        for j in range(len(word)):
                            if j < len(link.val) and word[j] != link.val[j]:
                                temp = TreeNode(word[:j], False)
                                linkT = TreeNode(word[j:], True)
                                link.val = link.val[j:]
                                temp.links.append(linkT)
                                temp.links.append(link)
                                ele.links.pop(i)
                                ele.links.append(temp)
                                isInsert = True
                                break
                    break
        if not isInsert: ele.links.append(TreeNode(word, True))   

    def search(self, word: str) -> bool:
        ele, isContinue = self.root, True
        while ele.links and isContinue:
            isContinue = False
            for link in ele.links:
                if link.val[0] == word[0]:
                    if link.val == word: return link.isEnd
                    if link.val.__contains__(word): return False
                    if word.__contains__(link.val):
                        word = word[len(link.val):]
                        ele = link
                        isContinue = True
        return False

    def startsWith(self, prefix: str) -> bool:
        ele, isContinue = self.root, True
        while ele.links and isContinue:
            isContinue = False
            for link in ele.links:
                if link.val[0] == prefix[0]:
                    if link.val.__contains__(prefix): return True
                    if prefix.__contains__(link.val):
                        prefix = prefix[len(link.val):]
                        ele = link
                        isContinue = True
        return False



if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # 返回 true
    print(trie.search("app"))     # 返回 false
    print(trie.startsWith("app")) # 返回 true
    trie.insert("app")   
    print(trie.search("app"))     # 返回 true

    print()

    trie = Trie()
    trie.insert("app")
    trie.insert("apple")
    trie.insert("beer")
    trie.insert("add")
    trie.insert("jam")
    trie.insert("rental")

    print(trie.search("apps"))
    print(trie.search("app"))
    print(trie.search("ad"))
    print(trie.search("applepie"))
    print(trie.search("rest"))
    print(trie.search("jan"))
    print(trie.search("rent"))
    print(trie.search("beer"))
    print(trie.search("jam"))

    print(trie.startsWith("apps"))
    print(trie.startsWith("app"))
    print(trie.startsWith("ad"))
    print(trie.startsWith("applepie"))
    print(trie.startsWith("rest"))
    print(trie.startsWith("jan"))
    print(trie.startsWith("rent"))
    print(trie.startsWith("beer"))
    print(trie.startsWith("jam"))