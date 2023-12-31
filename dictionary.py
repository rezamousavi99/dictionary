from typing import Any
class Dictionary:
    def __init__(self, key=0, *value) -> None:
        self.word = key
        self.meaning = list(value)
        self.dictionary = {}

    def make_dict(self):
        self.dictionary[self.word] = self.meaning
    
    def display_dictionary(self):
        print(self.dictionary)
    
    def display_meaning(self, key):
        print(f'{self.word} meaning: ', end='')
        print(self.dictionary[key])
    
    def reset_dict(self):
        self.dictionary = {}

    def __call__(self, key, *value) -> Any:
        self.word = key
        self.meaning = list(value)


d = Dictionary()


def get_keyvalue():
    word = input('word: ')
    meanig = input('meaning: ').split(',')
    d(word, *meanig)
    d.make_dict()

def commands():
    print('1.add a word with meaning\n2.display whole dictionary\
          \n3.search a word\n4.reset\n5.exit')

def search_word():
    inpt_word = input('word: ')
    d.display_meaning(inpt_word)


def main():

    while True:
        commands()
        uinput = input('Enter a command: ')
        match uinput:
            case '1':
                get_keyvalue()
                print('done')
                print('*' * 20)

            case '2':
                d.display_dictionary()
                print('*' * 20)
            
            case '3':
                search_word()
                print('*' * 20)
            case '4':
                d.reset_dict()
                print('reseted...')
                print('*' * 20)

            case '5':
                break

            case other:
                print('Invalid...')



if __name__ == '__main__':
    main()
