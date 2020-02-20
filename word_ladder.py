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
    from collections import deque
    import copy
    S = []
    S.append(start_word)
    Q = deque()
    Q.append(S)

    While len(Q) != 0:
        Q.pop()
        for word in dictionary_file:
            if _adjacent(word, S[-1]):
                if word == end_word:
                    S.append(word)
                    return S
                Scopy = copy.deepcopy(S)
                Scopy.append(word)
                Q.append(Scopy)
                dictionary_file.pop(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    if len(ladder) <= 1:
        return False
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
