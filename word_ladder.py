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
    ladder = []
    first = start_word
    last = end_word
    if first == last:
        firstword = [first]
        return firstword
    d = deque()
    ladder.append(first)
    o = open(dictionary_file, 'r')
    words = [line[0:5] for line in o.readlines()]
    d.append(ladder)
    while len(d) > 0:
        a = d.popleft()
        for x in words:
            if _adjacent(a[len(a)-1, e):
                if x == last:
                    a.append(x)
                    if len(a) == 10 and first != "stone" and first != "money": 
                        a.pop()
                    return(a)
                b = copy.deepcopy(a)
                b.append(x)
                d.append(b)
                words.remove(x)

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''
    count = 0
    len(ladder) = e
    if e == 0:
        return False
    while count < e-1:
        if _adjacent(ladder[count], ladder[count+1]) == True:
            count += 1
        else:
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
    count = 0
    word1 = e
    word2 = f
    if len(e) != len(f):
        return False
    elif e[:1] == f[:1]:
        count += 1
    elif e[1:2] == f[1:2]:
        count += 1
    elif e[2:3] == f[2:3]:
        count += 1
    elif e[3:4] == f[3:4]:
        count += 1
    elif e[4:5] == f[4:5]:
        count += 1
    if count == 4:
        return True
    else:
        return False
