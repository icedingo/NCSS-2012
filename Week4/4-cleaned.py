import string
words = {}
everything = set(open('words.txt'))
for line in everything:
    line = line.strip()
    length = len(line)
    if length not in words:
        words[length] = set()
    words[length].add(line)

message = raw_input('encrypted: ').lower()

encrypted = sorted([ m.strip(string.punctuation) for m in message.split() if m.strip(string.punctuation)], key=len, reverse=True)

def unbleh(encrypted, letters):
    orig_table, decode_table = zip(*letters.items())
    trans_table = string.maketrans(''.join(orig_table), ''.join(decode_table))
    return encrypted.translate(trans_table)

def decode(encrypted, letters={"'":"'"}):
    if len(encrypted) == 0:
        return letters
    nextword = encrypted[0]
    decrypt_string = ''.join(letters.values())
    for letter in nextword:
        if letter not in letters:
            break
    else:
        unblehed = unbleh(nextword,letters)
        if unblehed not in words[len(unblehed)]:
            return False
        result = decode(encrypted[1:], letters)
        if not result:
            return False
        return result


    for word in words[len(nextword)]:           # Check each word of the same length
        templetters = dict(letters)
        tempdecrypt = decrypt_string
        for l in xrange(len(nextword)):         # Go through each letter of the _ENCRYPTED_ word
            letter = nextword[l]
            if letter in templetters:               # If its already in the decrypt dict
                if templetters[letter] != word[l]:  # If the decrypted doesn't match the proposed word then go to next word
                    break
            else:
                if word[l] in tempdecrypt:    # If the encoded letter hasn't been seen but the decrypted is already there, NOT ALLOWED!
                    break
            templetters[letter] = word[l]       # Add decrypted letter to temp decrypt dict
            tempdecrypt += word[l]
        else:
            # This word worked
            result = decode(encrypted[1:], templetters) # Get the result after successful decoding of current word
            if not result:
                continue                        # Continue with next words
            letters.update(templetters)         # Update letters to reflect the latest check
            return letters                  # give them back
    else:
        return False

letters = decode(encrypted)

print 'decrypted:', unbleh(message, letters)