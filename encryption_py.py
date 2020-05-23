word = input('Enter a word you want to encrypt: ')
word_pass = input('Enter a word that you want to use as pass: ') #Dont use long strings for this

def word_encryption(word, word_pass):
    key = 0
    for i in range(len(word_pass)): #creates a key that will be used for encryption
        key += ord(word_pass[i])
    word_encrypted = ''
    for i in range(len(word)):
        word_encrypted += chr(ord(word[i]) + (2 + key))
    word_encrypted_temp = word_encrypted
    word_encrypted = ''
    for i in range(len(word)):
        word_encrypted += chr(ord(word_encrypted_temp[i]) -(12 + key)) #this is totally useless, dont do this
    word_encrypted_temp = word_encrypted                               #this does not make it more secure
    word_encrypted = ''                      
    for i in range(len(word)):
        word_encrypted += chr(ord(word_encrypted_temp[i]) + (22 + key)) 
    return word_encrypted

print('encrypted version is:', word_encryption(word, word_pass)) #I just have this for testing
encrypted_word = word_encryption(word, word_pass)

def word_decrypt(word_encrypted, word_pass):
    key = 0
    for i in range(len(word_pass)):
        key += ord(word_pass[i])
    word = ''
    for i in range(len(word_encrypted)): #basically undoes the stuff that other function has done to the string
        word += chr(ord(word_encrypted[i]) - (22 + key))
    word_temp = word
    word = ''
    for i in range(len(word_encrypted)):
        word += chr(ord(word_temp[i]) + (12 + key))
    word_temp = word
    word = ''
    for i in range(len(word_encrypted)):
        word += chr(ord(word_temp[i]) - (2 + key)   )
    return word

print(word_decrypt(encrypted_word, word_pass))

    