# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, word_list):
        matches = []
        for word in word_list:
            if self.is_anagram(word):
                matches.append(word)
        return matches
    
    def is_anagram(self, word):
        word = word.lower()
        if len(word) != len(self.word):
            return False
        if word == self.word:
            return False
        for char in word:
            if char not in self.word:
                return False
            if word.count(char) != self.word.count(char):
                return False
        return True


listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
