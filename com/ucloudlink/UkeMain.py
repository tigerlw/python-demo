
#from Utils import *

import  Utils

msg = Utils.getStringName("liuwei")

print msg


number_list = [number for number in range(0,6)]

print number_list

word = "letter"

letter_count = {tmp:word.count(tmp) for tmp in set(word)}

print  letter_count

def add_ints(a,b):
    return a+b

print add_ints(1,2)


def change_word(word1):
    # word = "123"
    print word

change_word(word)

print  word

try:
   print letter_count.get('s')
except Exception as error:
    print  error.message + " error"
finally:
    print "finally"