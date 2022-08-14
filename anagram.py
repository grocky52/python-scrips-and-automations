
#!/usr/bin/python3
class anagram_class:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def find_anagram(self):
        lenght_str1 = len(self.str1)
        length_str2 = len(self.str2)

        if lenght_str1 != length_str2:
            print(f'{str1} and {str2} are not anagram')

        sorted_str1 = sorted(self.str1)
        sorted_str2 = sorted(self.str2)

        if sorted_str1 == sorted_str2:
            print(f'{self.str1} and {self.str2} are anagram')

        else:
            print(f'{self.str1} and {self.str2} are not anagram')

if __name__ == '__main__':
    string1, string2 = input('enter two words separated by a comma:       ').split(',')
    class_obj = anagram_class(string1, string2)
    class_obj.find_anagram()
