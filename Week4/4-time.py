import time
start = time.time()
import string
words = {}
everything = set(open('words.txt'))
for line in everything:
    line = line.strip()
    length = len(line)
    if length not in words:
        words[length] = set()
    words[length].add(line)

precalc = time.time() - start

message = raw_input('encrypted: ').lower()
startd = time.time()

encrypted = sorted([ m.strip(string.punctuation) for m in message.split() if m.strip(string.punctuation)], key=len, reverse=True)

# print encrypted

def unbleh(encrypted, letters):
    orig_table, decode_table = zip(*letters.items())
    trans_table = string.maketrans(''.join(orig_table), ''.join(decode_table))
    return encrypted.translate(trans_table)

def decode(encrypted, letters={"'":"'"}):
    if len(encrypted) == 0:
        return letters
    nextword = encrypted[0]
    decrypt_string = ''.join(letters.values())
    # print 'testing:', nextword
    for letter in nextword:
        if letter not in letters:
            break
    else:
        # t_orig, t_decode = zip(*letters.items())
        # t_table = string.maketrans(''.join(t_orig), ''.join(t_decode))
        # t_nextword = nextword.translate(t_table)
        # if t_nextword not in everything:
        #     return False
        # print 'SOMETHI!', nextword
        # print 'This word not checked:', unbleh(nextword,letters)
        unblehed = unbleh(nextword,letters)
        if unblehed not in words[len(unblehed)]:
            # print 'Not in words!'
            return False
        result = decode(encrypted[1:], letters)
        # print result, nextword
        if not result:
            return False
        return result


    for word in words[len(nextword)]:           # Check each word of the same length
        # if nextword == 'rh':print 'check:', word
        # if nextword == 'sihkz' and word == 'dirks':
        #     print word
        templetters = dict(letters)
        tempdecrypt = decrypt_string
        for l in xrange(len(nextword)):         # Go through each letter of the _ENCRYPTED_ word
            # if nextword == 'sihkz' and word == 'dirks':print nextword[l], word[l], letters
            letter = nextword[l]
            # print letter,
            if letter in templetters:               # If its already in the decrypt dict
                if templetters[letter] != word[l]:  # If the decrypted doesn't match the proposed word then go to next word
                    # print templetters
                    break
            else:
                if word[l] in tempdecrypt:    # If the encoded letter hasn't been seen but the decrypted is already there, NOT ALLOWED!
                    break
            templetters[letter] = word[l]       # Add decrypted letter to temp decrypt dict
            tempdecrypt += word[l]
        else:
            # This word worked
            # if nextword == 'sihkz' and word == 'dirks': print'dirks worked!'
            # if nextword == 'rh':print 'FOUND!  ', word, len(nextword), len(word)
            result = decode(encrypted[1:], templetters) # Get the result after successful decoding of current word
            if not result:
                # print 'cont.   ', nextword
                continue                        # Continue with next words
            letters.update(templetters)         # Update letters to reflect the latest check
            # if len(encrypted[1:]) == 0:               # If all the letters are taken care of
            #     if nextword == 'rh':print 'returning', letters

            return letters                  # give them back
        # if nextword == 'sihkz' and word == 'dirks':print 'WHY?', letters
    else:
        # no words in nextword worked
        # if nextword == 'rh':print 'FAIL!', letters
        return False

letters = decode(encrypted)

# print letters.items()



print 'decrypted:', unbleh(message, letters)
decodet = time.time() - startd

print
print 'precalc:', precalc
print 'decode:', decodet
print 'total:', precalc + decodet
# for word in encrypted:
#     print word.translate(trans_table)
