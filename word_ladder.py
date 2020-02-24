#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    with open('words5.dict') as dictionary_file:
        dictionary = dictionary_file.readlines()
    from collections import deque
    import copy

    if start_word == end_word:
        return [start_word]

    S = []                   #create stack
    S.append(start_word)     #add start_word to stack
    Q = deque()             #create queue
    Q.append(S)             #append stack to queue
 
    new_dictionary = []     #create new dictionary to strip words of '\n'
    for word in dictionary: #for each word in old dictionary
        new_dictionary.append(word.strip('\n')) #strip each word of '\n' and add to new dictionary
    while len(Q) != 0:      #while queue is not empty
        t = Q.popleft()         #pop the leftmost stack from the queue
        for word in new_dictionary:     #for each word in the new dictionary
            if _adjacent(word, t[-1]):  #if the dictionary word is adjacent to the last word in the popped stack
                if word == end_word:    #if the dictionary word is also the end_word of the word ladder
                    S_copy = copy.deepcopy(t)   #make a copy of the popped stack
                    S_copy.append(word)         #append the dictionary word to the copy of the stack
                    for i in range(1,len(t)-1):
                        if _adjacent(S_copy[i-1],S_copy[i+1]):
                            S_copy.pop(i)
                    return S_copy               #return the word ladder
                S_copy2 = copy.deepcopy(t)      #if the dictionary word doesn't equal the end_word of the word ladder, make a copy of the popped stack
                S_copy2.append(word)            #append the dictionary word to the stack copy
                Q.append(S_copy2)               #append the stack copy to the queue
                new_dictionary.remove(word)     #remove the dictionary word match from the dictionary then run while loop again



def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:                #if word ladder is empty
        return False                    #return False because it's not a true word ladder
    if len(ladder) == 1:                #if word ladder has one word
        return True                     #return True
    for k in range(len(ladder)-1):      #for each element in the 
        if not _adjacent(ladder[k], ladder[k+1]):
            return False
    return True
 


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    count = 0
    for j in range(len(word1)):
        if word1[j] != word2[j]:
            count += 1
    if count == 1:
        return True
    else:
        return False
