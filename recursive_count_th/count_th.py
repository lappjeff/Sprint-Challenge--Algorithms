'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    #tracker for amount of th's in string
    th_count = 0

    #helper function to maintain main function state
    def handle_word(word):
        nonlocal th_count
        word_length = len(word)

        #select first two chars in word and increment if they equal "th"
        if word[0:2] == "th":
            th_count += 1

        #exit case
        if word_length == 0:
            return word
        else:
            #pass slice of string from index 1 on for every call
            handle_word(word[1:])

    handle_word(word)

    return th_count


count_th("thth")
