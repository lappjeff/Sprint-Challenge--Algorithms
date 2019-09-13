'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    th_count = 0

    def handle_word(word):
        nonlocal th_count
        word_length = len(word)

        if word[0:2] == "th":
            th_count += 1

        if word_length == 0:
            return word
        else:
            #remove first character for every iteration
            handle_word(word[1:])

    handle_word(word)

    return th_count


count_th("thth")
