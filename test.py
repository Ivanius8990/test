a='asssdgDDd'

def letter_count(word):
    letter_dict= {}
    for i in range(len(word)):
        count = 1
        for j in range(len(word)):
            if i != j and word[i].upper()==word[j].upper():
                count+=1
        letter_dict[word[i]] = count
    max_element = max(letter_dict.values())
    max_val_key = max(letter_dict, key=letter_dict.get)
    return max_val_key,max_element


print(letter_count(a))
