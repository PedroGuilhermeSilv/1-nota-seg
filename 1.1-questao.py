import operator
import random
import sys

cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""



class Attack:
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.freq = {}
        self.mappings = {}
        self.key = {}
        self.freq_eng = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
               'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
               'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
               's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
               'y': 0.0197, 'z': 0.0007}
        self.plain_chars_left = "abcdefghijklmnopqrstuvwxyz"
        self.cipher_chars_left = "abcdefghijklmnopqrstuvwxyz"
    def calculate_freq(self,cipher):
        letter_count = 0;
        for letters in self.alphabet:
            self.freq[letters] = 0

        for c in cipher:
            if c in self.alphabet:
                self.freq[c] +=1
                letter_count +=1

        for letters in self.alphabet:
            self.freq[letters] = round(self.freq[letters] / letter_count,4)

    def print_freq(self):
        for letters in self.freq:
            print(letters,':',self.freq[letters])
    def calculate_matches(self):
        for cipher in self.alphabet:
            map = {} #target letter
            for plain_char in self.alphabet:
                map[plain_char] = round(abs(self.freq[cipher]-self.freq_eng[plain_char]),4)
            self.mappings[cipher] = sorted(map.items(),key=operator.itemgetter(1))
    def guess_key(self):
        for c in self.cipher_chars_left:
            for plain_char, diff in self.mappings[c]:
                if plain_char in self.plain_chars_left:
                    self.key[c] = plain_char
                    self.plain_chars_left = self.plain_chars_left.replace(plain_char,'')
                    break
        return self.key
    def set_key_mapping(self,cipher_char,plain_char):
        if cipher_char not in self.cipher_chars_left or plain_char not in self.plain_chars_left:
            print("ERROR: No Mapping Exists!",cipher_char,'__',plain_char)
            sys.exit(-1)
        self.key[cipher_char] = plain_char
        self.cipher_chars_left = self.cipher_chars_left.replace(cipher_char,'')
        self.plain_chars_left = self.plain_chars_left.replace(plain_char,'')

    
def decrypt(key,cipher):
        message = ""
        for c in cipher:
            if c in key:
                message += key[c]
            else:
                message += c
        return message

attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()
attack.calculate_matches()

#mapping improvement

attack.set_key_mapping('r','e')
attack.set_key_mapping('d','d')
attack.set_key_mapping('v','c')
attack.set_key_mapping('p','h')
attack.set_key_mapping('m','a')
attack.set_key_mapping('w','i')
attack.set_key_mapping('t','y')
attack.set_key_mapping('u','r')
attack.set_key_mapping('x','f')
attack.set_key_mapping('a','x')
attack.set_key_mapping('y','m')
attack.set_key_mapping('s','p')
attack.set_key_mapping('c','w')
attack.set_key_mapping('o','g')
attack.set_key_mapping('g','z')
attack.set_key_mapping('e','v')
attack.set_key_mapping('f','q')

print()
key = attack.guess_key()
print()
print(key)
message = decrypt(key,cipher)
print()
# print(message)

print()
cipher_lines = cipher.splitlines()
plain_lines = message.splitlines()
for i in range(len(cipher_lines)):
    print('M: ',plain_lines[i])
    #print('C: ',cipher_lines[i])