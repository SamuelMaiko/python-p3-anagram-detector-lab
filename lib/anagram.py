# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word
    def match(self,liste):
        result=list()
        for each_word in liste:
            letter_list=[each_letter for each_letter in each_word] 
            letter_list.sort()
            word_list=[each_letter for each_letter in self.word]
            word_list.sort()
            if word_list==letter_list:
                result.append(each_word)
        return result