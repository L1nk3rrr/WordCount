import os
import time

VOCAB = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'}


def check_letters(letters: str):
    """
    Function that help check is string contain only letters
    raise TypeError if in a string are not letters ^)
    :param letters: string of letters
    :return: None
    """
    if not letters.isalpha():
        raise TypeError


def gen_show(vocab: list):
    """
    Basic generator for getting value of list
    :param vocab: vocabulary that we want to iterate over
    :yield: element of list
    """
    for i in vocab:
        if i is not None:
            yield i
        else:
            yield None


def only_integer(text: str):
    """
    Ask user to input ONLY integer values or 'q' to quit
    :param text: message to print out
    :return: checked number or 'q'
    """
    while True:
        try:
            num = input(f"\n {text}")
            if num != 'q':
                num = int(num)
            return num
        except ValueError:
            print(" Please input integer only...")


def count_chars(letters: str):
    """
    Function create dict with letters, help to understand how many times letter repeat in input 'letters'
    :param letters: string with letters
    :return: dict with letters and their count numbers
    """

    # make dict for our results
    chars = dict()

    for x in letters:
        if x not in chars:
            chars.update({x: 1})
        elif x in chars:
            plus = chars.get(x) + 1
            chars.update({x: plus})
    return chars


def vocab_menu():
    """
    Menu for work with vocabulary
    :return: None
    """
    while True:
        os.system('cls')
        print('\n ===========[ VOCABULARY MENU ]=============')
        print(' ----------------------------------------')
        print(' 1. Append to vocabulary')
        print(' 2. Replace vocabulary')
        print(' 9. Exit')
        uinp = input('\n Enter your selection: ')

        if uinp == '1':
            append_to_vocab()
        elif uinp == '2':
            replace_vocab()
        elif uinp == '9':
            return
        else:
            os.system('cls')
            input('\n PLEASE SELECT FROM THE MENU.....(press any button)')


def append_to_vocab():
    """
    Function to append words to our vocabulary
    :return: None
    """
    os.system('cls')
    print('\n ===========[ APPEND TO VOCABULARY ]=============')
    print(' ----------------------------------------')
    words = input(' Write your words with separating by \',\' '
                  '\n Example: Hello,World,my,name'
                  '\n Write your words her: ').split(',')
    try:
        VOCAB.update(words)
    except Exception as e:
        print(e)

    print(f' Appending of words {words} successfully completed')
    input('\n .. Press any key .. ')


def replace_vocab():
    """
    Function to replace vocabulary by hands
    :return: None
    """
    global VOCAB

    os.system('cls')
    print('\n ===========[ REPLACE VOCABULARY ]=============')
    print(' ----------------------------------------')
    words = input(' Write your words with separating by \',\' '
                  '\n Example: Hello,World,my,name'
                  ' Write your words her: ').split(',')
    VOCAB = set(words)

    print(f' Replacing vocabulary by words({words}) successfully completed')
    input('\n .. Press any key .. ')


def find_words_menu():
    """
    Main function for finding words
    User needs to input letters(and only letters) and he will see the result
    After result he can see words by input number that he wants to see (if he want) or quit by input 'q'
    :return: None
    """
    result = set()

    os.system('cls')
    print('\n ===========[ FIND WORDS ]=============')
    print(' ----------------------------------------')
    print(' If it is mistake press "Enter" to return back')
    temp_letters = input(' Write letter/s:')
    try:
        check_letters(temp_letters)
        letters = count_chars(temp_letters)
    except TypeError:
        print(' I said you – WRITE LETTER/S')
        input(' You need to restart, "bad boy", I don\'t wanna do while loop because you can\'t heard me')
        return
    if len(temp_letters) >= 1:
        gen_help = iter(letters.items())
        char, count = next(gen_help)
        result.update(find_words_func(char, count))
        for _ in range(len(letters) - 1):
            char, count = next(gen_help)
            result = remove_inappropriate_words(char, count, result)
    result_count = len(result)
    result = list(result)
    print(f" Words count letter '{temp_letters}' : {result_count}")
    time.sleep(2)
    if result_count >= 1:
        show = only_integer("Input 'q' to quit\n Number of words you want to see: ")
        remainder_count = 0
        try:
            gen = gen_show(result)

            while True:
                if show == 'q':
                    return
                show_list = []
                for i in range(show):
                    show_list.append(next(gen))
                print(f' List of words: {show_list}')
                remainder_count = result.index(show_list[-1])
                show = only_integer("Input 'q' to quit\n If you want to show more write a number how many you want: ")
        except StopIteration:
            if remainder_count != result_count - 1:
                print(remainder_count)
                print(" Very big, will show remainder")
                print(f" Okay, all words: {result[remainder_count + 1:]}")
            else:
                print(" List don't have that number of values")
                print(f" Okay, all words: {result}")
        finally:
            input(' .. Press any key .. ')


def find_words_func(letter: str, repeats: int, words=VOCAB):
    """
    Helper function for finding words in our vocabulary
    :param letter: letter that we want to find
    :param repeats: count of repeats of the letter
    :param words: where we will find words
    :return: result list with words that contain letters
    """
    result_list = []
    temp_list = list(words)
    for word in temp_list:
        if word.count(letter) >= repeats:
            result_list.append(word)
    return result_list


def remove_inappropriate_words(letter: str, repeats: int, words: set):
    """
    Function help remove inappropriate words from result, not practical but it way work!
    :param letter: letter that we want to find
    :param repeats: count of repeats of the letter
    :param words: where we will find words
    :return: set of words that contain letters
    """
    temp_words = list(words)
    for word in temp_words:
        if repeats > word.count(letter):
            temp_words.remove(word)
    return set(temp_words)


def main():
    """
    Main menu of the program!
    :return: None
    """
    while True:
        os.system('cls')
        print('\n ===========[ WORD COUNT ]=============')
        print(' Standart vocabulary have been loaded by start of the program')
        print(' ----------------------------------------')
        print(' 1. Vocabulary settings(append, replace)')
        print(' 2. Find words by containing letters')
        print(' 9. Exit')
        uinp = input('\n Enter your selection: ')

        if uinp == '1':
            vocab_menu()
        elif uinp == '2':
            find_words_menu()
        elif uinp == '9':
            return
        else:
            os.system('cls')
            input('\n PLEASE SELECT FROM THE MENU.....(press any button)')


if __name__ == '__main__':
    main()
