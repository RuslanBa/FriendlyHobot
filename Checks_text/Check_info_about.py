import re


def check_info_about(text):

    f = open('Checks_text/Mat_words.txt').readlines()
    f = [x.replace("\n", "") for x in f]

    text_new = re.sub('\n+', '\n', text)

    word = text_new.split()
    for x in word:
        if x.title() in f:
            text_new = text_new.replace(x, '')

    text_new = text_new[:350]

    return text_new
