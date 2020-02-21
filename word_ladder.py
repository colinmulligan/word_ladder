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

    S = []
    print('test1', S)
    S.append(start_word)
    print('test2',S)
    Q = deque()
    print('test3',Q)
    Q.append(S)
    print('test4',Q)
    
    new_dictionary = []
    for word in dictionary:
        new_dictionary.append(word.strip('\n'))
    while len(Q) != 0:
        t = Q.pop()
        print('this one', Q)
        for word in new_dictionary:
            if _adjacent(word, t[-1]):
                if word == t[-1]:
                    S_copy = copy.deepcopy(t)
                    S_copy.append(word)
                    return S_copy
                S_copy2 = copy.deepcopy(t)
                S_copy2.append(word)
                print(S_copy2)
                Q.append(S_copy2)
                print(Q)
                new_dictionary.remove(word)
                print(S, Q)



def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) == 0:
        return False
    if len(ladder) == 1:
        return True
    for k in range(len(ladder)-1):
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
