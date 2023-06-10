import re


def check_info_about(text):

    text_new = re.sub('\n+', '\n', text)
    # print(text_new)
    return text_new
