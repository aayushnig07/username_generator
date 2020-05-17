import requests
from random import randint

url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
def get_names_list():
    usernames = requests.get(url)
    text = usernames.text
    # print(text)
    return text.split()

def get_random_word():
    name_list = get_names_list()
    random_number = randint(0,len(name_list))
    random_word = name_list[random_number]
    random_salt = randint(0,9999)
    print(random_word + str(random_number+random_salt))

get_random_word()

