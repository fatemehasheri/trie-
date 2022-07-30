# define alphabet size (26 characters for a – z)
Char_size = 26
class Node:
    # Constructor
    def __init__(self):
        self.children = [None]*Char_size
        self.exit = False

#A class to store a Trie node   
class trie:
    # Constructor
    def __init__(self,):
        self.root = Node()
        
    #Converting the format of object tree items to string 
    def __str__(self):
        wordperfix = self.findPrefix('')
        string = ''
        for i in wordperfix:
            string+=i
            string+='\n'
        return string
        
    # do for each character of the key
    def chartoint(self,character):
        return ord(character)-ord('a')
    
    #Adding a new word
    def addWord(self,str):
        parrent = self.root
        length = len(str)
        for x in range(length):
            i = self.chartoint(str[x])
            if parrent.children[i] is not None:
                parrent = parrent.children[i]
            else:
                parrent.children[i] = Node()
                parrent = parrent.children[i]
        parrent.exit = True

    #Delete the word that was in the words
    def deleteWord(self,str):
        parrent = self.root
        length = len(str)
        for x in range(length):
            i = self.chartoint(str[x])
            if parrent.children[i] is not None:
                parrent = parrent.children[i]
            else:
                print("Keyword doesn't exist in trie")
        if parrent.exit is not True:
                print("Keyword doesn't exist in trie")
        parrent.exit = False
        return

    #Search for a word whose output is a boolean   
    def findword(self,str):
        parrent = self.root
        length = len(str)
        for x in range(length):
            i = self.chartoint(str[x])
            if parrent.children[i] is not None:
                parrent = parrent.children[i]
            else:
                return False
        if parrent.exit is not True:
            return False
        return True
    
    
    def __getall(self,ptr,key,key_list):
        if ptr is None:
            key_list.append(key)
            return
        if ptr.exit==True:
            key_list.append(key)
        for i in range(26):
            if ptr.children[i]  is not None:
                self.__getall(ptr.children[i],key+chr(ord('a')+i),key_list)

    #Search for a letter of words  
    def findPrefix(self,key):
        parrent = self.root
        key_list = []
        length = len(key)
        for x in range(length):
            i = self.chartoint(key[x])
            if parrent.children[i] is not None:
                parrent = parrent.children[i]
            else:
                return None
        
        self.__getall(parrent,key,key_list)
        return key_list


trie1 = trie()

trie1.addWord("zahra")
trie1.addWord("fatemeh")
trie1.addWord("maryam")
trie1.addWord("parisa")
trie1.addWord("food")
trie1.addWord("exiting")
trie1.addWord("smart")
trie1.addWord("parham")

print("word search fatemeh: ",trie1.findword("fatemeh"))
print("word search zahra: ",trie1.findword("zahra"))
print("word search mina: ",trie1.findword("mina"))
print("Search letters m: ",trie1.findPrefix('m'))
print("Search letters par: ",trie1.findPrefix('par'))
print("Delete the word parisa: ",trie1.deleteWord("parisa"))
print("Delete the word food: ",trie1.deleteWord("food"))
print("Delete the word foo: ",trie1.deleteWord("foo"))
print(trie1)
