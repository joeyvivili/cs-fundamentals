"""This file is self-directed and implemented code for better practice and understand the knowledge of course cs61a
along the process/way of studying the course
Contains most of the cs61a discussion questions
"""
import math

def remove(n,digit):
    """Return all digits of non-negative N that are not DIGIT, 
    for some non-negative DIGIT less than 10
    
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    >>> remove(5677432, 7)
    56432
    >>> remove(5677032, 7)
    56032
    >>> remove(3970882, 0)
    397882
    """
    kept, digits = 0, 1
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = kept + digits * last 
            digits = digits * 10 
    return kept

## discussion02
def make_keeper(n):
    """ Takes a positive integer n and returns a function f that takes as its argument another one-argument function cond. 
    When f is called on cond, it prints out the integers from 1 to n (including n) for which cond returns a true value when called on each of those integers. 
    """    
    def f(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
    return f

## discussion02
def find_digit(k):
    """takes in a positive integer k and returns a function that takes in a positive integer x and returns the kth digit from the right of x. 
    If x has fewer than k digits, it returns 0.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    def f(x):
        return int((x % 10**k) // (10**(k-1)))
    return f

## discussion02
def match_k(k):
    """ Takes in an integer k and returns a function that takes in a variable x and 
    returns True if all the digits in x that are k apart are the same.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def f(x):
        while x // (10**k) > 0:
            if (x % 10) != (x // 10**k) % 10:
                return False
            x //= 10
        return True
    return f

def inverse_cascade(n):
    """
    Docstring for inverse_cascade
    
    :param n: Description
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    ### defining two helper functions to grow and shrink n
    def grow(n):
        if n < 10:
            print(n)
        else:
            grow(n // 10)
            print(n)

    def shrink(n):
        if n < 10:
            print(n)
        else:
            print(n)
            shrink(n // 10)

    grow(n)
    shrink(n // 10)
    ## failed code:
    # if n < 10:
    #     print(n)
    # else:
    #     inverse_cascade(n // 10)
    #     print(n)
    #     inverse_cascade(n // 10)

## discussion03
def swipe(n):
    """ Prints the digits of argument n, one per line, first backward then forward. 
    The left-most digit is printed only once
    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    # base case
    if n < 10:
        print(n)
    # recursion
    else: 
        last_digit = n % 10
        print(last_digit)
        swipe(n // 10)
        print(last_digit)

## discussion03
def skip_factorial(n):
    """ Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    # base case
    if n <= 0:
        return 1
    # recursion
    else:
        return n * skip_factorial(n - 2)
    
## discussion03
""" Define another “helper” function (a function that exists just to help implement this one)
    within a recursive function.
"""
def is_prime(n):
    """ Takes an integer n greater than 1. 
        Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    assert n > 1
    def check_all(i):
        "Check whether no number from i up to n evenly divides n."
        if i == n: # could be replaced with i > (n ** 0.5)
            return True
        elif n % i == 0:
            return False
        return check_all(i + 1)
    return check_all(2)

## discussion03
def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(int(n))
    # base case
    if n == 1:
        return 1
    # recursion
    elif n % 2 == 0:
        return 1 + hailstone(n/2)
    else:
        return 1 + hailstone(3 * n + 1)

## discussion03
def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.
    Logicstic:
    the implementation must keep track of the final number n, the current number i, the player who say i,
    and the current direction that determines the nect player. (direction can be represented using integer
    -1 (decrease, counterclockwise direction) and 1 (increase, clockwise direction))

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        who = who + direction
        if who > k:
            who = 1
        if who < 1:
            who = k
        return f(i + 1, who, direction) ### determine which factors need to change with each iteration (i, who, direction) 
                                        ### and therefore be passed in recursive call, and which do not need to change (n, k)
    return f(1, 1, 1) ### define a recursion function inside of the current function, and calls it with return 
                      ### for the current function with initial conidtions passed in

def has_seven(n):
    """ Recursive function that returns True if an input number n contains 7, False otherwise
    """
    if n == 0:      ## since this function is a recursive call, we exclude n % 7 == 0
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)
    
## discussion05_Tree
# tree definition, data abstrction (constructor & selector), and tree helper functions
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
# tree_recursion
def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6]) # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6]) # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5]) # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6]) # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6]) # There is no path with these labels
    False
    """
    # base case
    if p == [label(t)]:     # if len(p) == 1 and p[0] == label(t)
        return True
    # recursive call
    if label(t) != p[0]:
        return False
    else:
        for b in branches(t):
            if has_path(b, p[1:]):
                return True
        return False
# tree_recursion
def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if label(t) == x:
        return [label(t)]

    for b in branches(t):
        path = find_path(b, x)
        if path is not None:
            return [label(t)] + path

    return None

### linked_list data abstraction 
empty = "empty"
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))
def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]
def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]
def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]
# linked_list_length
def link_len(s):
    """ Return the length of the linked list s 

    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> link_len(four)
    4
    """
    if s == empty:
        return 0
    else:
        return 1 + link_len(rest(s))
# linked_list element selection
def link_get(s, i):
    """ Return the ith element of the linked list s

    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> link_get(four, 0)
    1
    >>> link_get(four, 3)
    4
    """
    if s == None:
        return "Index out of bound"
    if i == 0:
        return first(s)
    else:
        return link_get(rest(s), i - 1)
    
def link_extend(s, t):
    """Return a list with the elements of s followed by those of t.
    
    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> alpha = link("a", link("b", link("c", link("d", link("e", empty)))))
    >>> link_extend(four, alpha)
    [1, [2, [3, [4, ['a', ['b', ['c', ['d', ['e', 'empty']]]]]]]]]
    >>> link_extend(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
    """
    assert is_link(s) and is_link(t)
    if s == empty:
        return t 
    else:
        return link(first(s), link_extend(rest(s), t))
    
def link_apply(f, s):
    """ Apply f to all elements of s.

    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> link_apply(lambda x: x*x, four)
    >>> four
    [1, [4, [9, [16, 'empty']]]]
    """
    if s == empty:
        return None
    else: 
        s[0] = f(first(s))
        link_apply(f, rest(s))
# modifier of link_apply
def apply_to_all_link(f, s):
    """ Return a new list as a result of applying f to all elements of linked list s.
    
    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> apply_to_all_link(lambda x: x*x, four)
    [1, [4, [9, [16, 'empty']]]]
    """
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true.
        
    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> keep_if_link(lambda x: x%2 == 0, four)
    [2, [4, 'empty']]
    """
    if s == empty:
        return empty
    else:
        if f(first(s)):
            return link(first(s), keep_if_link(f, rest(s)))
        else:
            return keep_if_link(f, rest(s))

def join_link(s, separator):
    """Return a string of all elements in s separated by separator.
    
    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> join_link(four, ", ")
    '1, 2, 3, 4'
    """
    if rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)


## discussion05_iterator/generator
def differences(t):
    """Yield the differences between adjacent values from iterator t.
    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    last = next(t)
    while True:
        try:
            curr = next(t)
            yield curr - last
            last = curr
        except StopIteration:
            break

def prefixes_gen(s):
    """ Return a generator (iterator) that point to the prefixes of a string s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s  
""" 
👉 yield does NOT return to the caller function.
👉 It returns to the caller of next().
Even within a recursive call, the yield does not return its result to the recursive call one level up
(the call that called this call), instead returns its result to next(g)
The entire recursive call is paused right after hitting the first yield, the entire call stack is frozen 
at that yield. When next(g) is called, all execution resume exactly where it paused.
👉 ** yield from ** does NOT collect results and send them upward.
"""
# without generator version  
def prefixes(s):
    if s == "":
        return []
    prev = prefixes(s[:-1])
    return prev + [s]

def substrings_gen(s):
    """
    Docstring for substrings
    
    >>> list(substrings_gen('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings_gen(s[1:])

## discussion07
def draw(hand, positions):
    """Remove and return the items at positions from hand.
    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    removed = [hand[i] for i in sorted(positions)]
    # for item in removed:
    #     hand.remove(item)
    hand[:] = [x for x in hand if x not in removed] ## this modify the original_list (mutation) instead of name rebinding; 
                                                    # if just simple name rebinding like hand = [....], it would not change the original_list outside of the funcion
    return removed
def draw_one_line_f(hand, positions):
    """Remove and return the items at positions from hand.
    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list(reversed( [hand.pop(i) for i in reversed(sorted(positions))] ))
#     For a list s and integer i, s.pop(i) returns and removes the ith element, which changes the position (index) of all
# the later elements but does not affect the position of prior elements.
# Calling reversed(s) on a list s returns an iterator. Calling list(reversed(s)) returns a list of the elements in s
# in reversed order

## discussion07 keyboard_class_implementation
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class CapsLock:
    def __init__(self):
        self.pressed = 0

    def press(self):
        self.pressed += 1

class Button:
    """A button on a keyboard.

    >>> f = lambda c: print(c, end='')  # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """
    caps_lock = CapsLock()

    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(self):
        "Call output on letter (maybe uppercased), then return the button that was pressed."
        self.pressed += 1
        if self.caps_lock.pressed % 2 == 1:
            self.output(self.letter.upper())
        else:
            self.output(self.letter)
        return self

class Keyboard:
    """A keyboard.

    >>> Button.caps_lock.pressed = 0  # Reset the caps_lock key
    >>> bored = Keyboard()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o']
    >>> bored.keys['l'].pressed
    2

    >>> Button.caps_lock.press()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o', 'H', 'E', 'L', 'L', 'O']
    >>> bored.keys['l'].pressed
    4
    """
    def __init__(self):
        self.typed = []
        self.keys = {c: Button(c, self.typed.append) for c in LOWERCASE_LETTERS}
    ### Why would passing in self.typed.append works?

    def type(self, word):
        "Press the button for each letter in word."
        assert all([w in LOWERCASE_LETTERS for w in word]), 'word must be all lowercase'
        for w in word:
            self.keys[w].press()


## discussion07 bear_class_implementation
class Eye:
    """An eye.

    >>> Eye().draw()
    '•'
    >>> print(Eye(False).draw(), Eye(True).draw())
    • -
    """
    def __init__(self, closed=False):
        self.closed = closed

    def draw(self):
        if self.closed:
            return '-'
        else:
            return '•'

class Bear:
    """A bear.

    >>> Bear().print()
    ʕ •ᴥ•ʔ
    """
    def __init__(self):
        self.nose_and_mouth = 'ᴥ'

    def next_eye(self):
        return Eye()

    def print(self):
        left, right = self.next_eye(), self.next_eye()
        print('ʕ ' + left.draw() + self.nose_and_mouth + right.draw() + 'ʔ')

class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ʕ -ᴥ-ʔ
    """
    def next_eye(self):
        return Eye(True)

class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ʕ -ᴥ•ʔ
    """
    def __init__(self):
        super().__init__()
        self.eye_calls = 0

    def next_eye(self):
        self.eye_calls += 1
        return Eye(self.eye_calls % 2)


## discussion08 linked_list_data_structure
class Link:
    """A linked list is either a Link object or Link.empty
    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
    
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
    #self-defined Link object methods
    def sort(self):
        """Sort the Link in increasing order
        
        >>> s = Link(8, Link(3, Link(7, Link(1, Link(5)))))
        >>> s.sort()
        >>> s
        Link(1, Link(3, Link(5, Link(7, Link(8)))))
        """
        if self.rest is Link.empty:
            return 
        self.rest.sort()
        if self.first > self.rest.first:
            self.first, self.rest.first = self.rest.first, self.first
            self.rest.sort()

def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> ones = Link(1)
    >>> ones.rest = ones
    >>> [ones.first, ones.rest.first, ones.rest.rest.first, ones.rest.rest.rest.first]
    [1, 1, 1, 1]
    >>> ones.rest is ones
    True

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    s = Link(1)
    s.rest = Link(Link(2))
    s.rest.first.rest = s
    return s

def sum_rec(s):
    """
    Returns the sum of the elements inlinked list s using recursion.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_rec(a)
    14
    >>> sum_rec(Link.empty)
    0
    """
    if s is Link.empty:
        return 0
    else:
        return s.first + sum_rec(s.rest)

def sum_iter(s):
    """
    Returns the sum of the elements in linked list s using iteration.
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_iter(a)
    14
    >>> sum_iter(Link.empty)
    0
    """
    sum = 0
    s_pointer = s
    while s_pointer is not Link.empty:
        sum += s_pointer.first
        s_pointer = s_pointer.rest
    return sum

def overlap(s, t):
    """For link list s and t of numbers sorted in increasing order and have no repreated elements within each list, count the numbers that appear in both.
    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b) # 3 and 7
    2
    >>> overlap(a.rest, b) # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    count = 0
    s_pointer, t_pointer = s, t
    while s_pointer is not Link.empty and t_pointer is not Link.empty:
        if s_pointer.first < t_pointer.first:
            s_pointer = s_pointer.rest
        elif s_pointer.first > t_pointer.first:
            t_pointer = t_pointer.rest
        else:
            count += 1
            s_pointer, t_pointer = s_pointer.rest, t_pointer.rest
    return count

def overlap_rec(s, t):
    """For link list s and t of numbers sorted in increasing order and have no repreated elements within each list, count the numbers that appear in both using recursion.
    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap_rec(a, b) # 3 and 7
    2
    >>> overlap_rec(a.rest, b) # just 7
    1
    >>> overlap_rec(Link(0, a), Link(0, b))
    3
    """
    if s is Link.empty or t is Link.empty:
        return 0
    if s.first == t.first:
        return 1 + overlap_rec(s.rest, t.rest)
    elif s.first < t.first:
        return overlap_rec(s.rest, t)
    elif s.first > t.first:
        return overlap_rec(s, t.rest)
    
## alterantive implementation of link_list_overlap()
def length(s):
    """Return the length of a link list s. """
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)

def filter_link(f, s):
    """Return a linked list containning only elements of s that satisfy function f.
       The linked list version of [x for x in list if f(x)]
    """
    if s is Link.empty:
        return s
    if f(s.first):
        return Link(s.first, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)

def contained_in(s):
    def f(s, x):
        """Return whether a value is in linked list s"""
        if s is Link.empty:
            return False
        else:
            return s.first == x or f(s.rest, x)
    return lambda x: f(s, x)

def overlap_unsorted(s, t):
    """For s and t with no repeats, count the numbers that appear in both.
    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8, Link(12))))))
    >>> overlap_unsorted(a, b) # 3 and 7
    2
    >>> overlap_unsorted(a.rest, b.rest) # just 7
    1
    >>> overlap_unsorted(Link(0, a), Link(0, b))
    3
    """
    return length(filter_link(contained_in(t), s))

### discussion08 
def divide(n, d):
    """Return a linked list with a cycle containing the digits of the infinte decimal expansion of n/d, n & d are integers.

    >>> 1/22
    0.045454545454545456
    >>> x = Link(0, Link(0, Link(4, Link(5))))
    >>> x.rest.rest.rest.rest = x.rest.rest  ## to build a cycle, must detect when a remainder repeats
    >>> display(x, 20)
    0.04545454545454545454...
    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0) # The zero before the decimal point
    cache = {}  # Dictionary to detect repeating remainders. (logic: Same remainder → same future digits → repetition)
    tail = result
    while n not in cache:
        q, r = 10 * n // d, 10 * n % d
        tail.rest = Link(q)
        tail = tail.rest
        cache[n] = tail
        n = r
    tail.rest = cache[n]
    return result
# While constructing the decimal expansion, store the tail for each n in a dictionary keyed by n. When some n appears
# a second time, instead of constructing a new Link, set its original link as the rest of the previous link. That will
# form a cycle of the appropriate length.

def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.
    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')

# def decimal_cycle(n, d):
#     """Return the digits before repeating cycle, and the cycle as a list of integer for the decimal part for n/d.
#        *The logic for this function is number theory using modular arithmetic 
    
#     >>> digits, cycle = decimal_cycle(1, 6)     #1/6 = 0.1666666666...
#     >>> digits
#     [1]
#     >>> cycle
#     [6]    
#     >>> digits, cycle = decimal_cycle(1, 12)    #1/12 = 0.0833333333...
#     >>> digits
#     [0, 8]
#     >>> cycle
#     [3]    
#     >>> digits, cycle = decimal_cycle(1, 7)     #1/7 = 0.142857142857...
#     >>> digits
#     []
#     >>> cycle
#     [1, 4, 2, 8, 5, 7]    
#     >>> digits, cycle = decimal_cycle(1, 13)    #1/13 = 0.076923076923...
#     >>> digits
#     []
#     >>> cycle
#     [0, 7, 6, 9, 2, 3]    
#     """
#     digits_before_cycle = []
#     d_prime = d
#     while d_prime % 2 == 0 or d_prime % 5 == 0:
#         if d_prime % 2 == 0:
#             d_prime /= 2
#         else:
#             d_prime /= 5
#         before_cycle_len += 1
    
#     cycle = []
#     n_prime = n
#     while True:
#         digit = (n_prime * 10) // d
#         n_prime = (n_prime * 10) % d
#         cycle.append(digit)
#         if n_prime == n:
#             break
#     return cycle

### map_link, filter_link
def map_link(f, s):
    """Applies a function f to each element of a linked list object s and constructs a linked list containing the results.
    >>> f = lambda x: x + 1
    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> s2 = map_link(f, s)
    >>> s2
    Link(2, Link(3, Link(4, Link(5))))
    """
    if s.rest is Link.empty:
        return Link(f(s.first))
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Returns a linked list object containing all elements of a linked list s for which f returns a true value.
    
    >>> f = lambda x: x % 2 == 0
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7, Link(8))))))))
    >>> s2 = filter_link(f, s)
    >>> s2
    Link(2, Link(4, Link(6, Link(8))))
    """
    if s is Link.empty:
        return s
    if f(s.first):
        return Link(s.first, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)



### textbook2.9_sets_implementation
# sets are unordered collections where duplicate elements are removed upon construction
"""Abstractly, a set is a collection of distinct objects that supports membership testing, union, intersection, and adjunction. 
Adjoining an element and a set returns a new set that contains all of the original set's elements along with the new element, if it is distinct. 
Union and intersection return the set of elements that appear in either or both sets, respectively. 
As with any data abstraction, we are free to implement any functions over any representation of sets that provides this collection of behaviors."""
class SetLink():
    empty = ()
    def __init__(self, first, rest=empty):
        """Creating an object with Link() link list data structure and Python built in set() behavior."""
        assert rest is SetLink.empty or isinstance(rest, SetLink)
        self.first = first
        self.rest = rest       
    
    def __repr__(self):
        if self.rest is SetLink.empty:
            return f"SetLink({self.first})"
        return f"SetLink({self.first}, {repr(self.rest)})"

    # def is_setlink(self):
    #     pointer = self
    #     elements = set()
    #     while pointer is not SetLink.empty:
    #         if not isinstance(pointer, SetLink):
    #             return False
    #         if pointer.first in elements:
    #             return False
    #         else:
    #             elements.append(pointer.first)
    #             pointer = pointer.rest
    #     return True

    ### Part1 of SetLink: 
    # setlink_functions with unsordered SetLink objects with no duplicates
    def contains(self, v):
        """Return True if and only if self contains value v.
        
        >>> s = SetLink(4, SetLink(1, SetLink(5)))
        >>> s.contains(2)
        False
        >>> s.contains(5)
        True
        """
        pointer = self
        while pointer is not SetLink.empty:
            if pointer.first == v:
                return True
            pointer = pointer.rest
        return False

    def adjoin(self, v):
        """Adjoin element v to self accoding to set behavior (no deplicate elements in SetLink).
        
        >>> s = SetLink(4, SetLink(1, SetLink(5)))
        >>> s.adjoin(2)
        >>> s
        SetLink(2, SetLink(4, SetLink(1, SetLink(5))))
        """
        if self.contains(v):
            return
        else:
            self.first, self.rest = v, SetLink(self.first, self.rest)
    
    def apply_to_all(self, f):
        """Return a SerLink that contains all elements of self applied with function f
        
        >>> s = SetLink(4, SetLink(1, SetLink(5)))
        >>> t = s.apply_to_all(lambda x: x*x)
        >>> t 
        SetLink(16, SetLink(1, SetLink(25)))
        """
        if self.rest is SetLink.empty:
            return SetLink(f(self.first))
        else:
            return SetLink(f(self.first), self.rest.apply_to_all(f))
    
    def map_all(self, f):
        """Apply function f to all elements of SetLink self.
        
        >>> s = SetLink(4, SetLink(1, SetLink(5)))
        >>> s.map_all(lambda x: x*x)
        >>> s
        SetLink(16, SetLink(1, SetLink(25)))
        """
        self.first = f(self.first)
        if self.rest is SetLink.empty:
            return 
        self.rest.map_all(f)

    def intersect(self, s2):
        """Return a SetLink containing all elements common to SetLink self and s2.
        
        >>> s = SetLink(4, SetLink(1, SetLink(5)))
        >>> t = SetLink(16, SetLink(4, SetLink(1, SetLink(5))))
        >>> t.intersect(s.apply_to_all(lambda x: x*x))
        SetLink(16, SetLink(1))
        """
        if s2.contains(self.first):
            if self.rest is SetLink.empty:
                return SetLink(self.first)
            else:
                return SetLink(self.first, self.rest.intersect(s2))
        else:
            if self.rest is SetLink.empty:
                return SetLink.empty
            else:
                return self.rest.intersect(s2)
            
    def copy(self):
        """Return a new SetLink with all elements of self
        
        >>> s = SetLink(2, SetLink(4, SetLink(1)))
        >>> s2 = s.copy()
        >>> s2
        SetLink(2, SetLink(4, SetLink(1)))
        >>> s2 is s
        False
        """
        if self.rest is SetLink.empty:
            return SetLink(self.first)
        else:
            return SetLink(self.first, self.rest.copy())
    
    def union_set(self, set2):
        """Return a set containing all elements either in self or set2.
        
        >>> s = SetLink(2, SetLink(4, SetLink(1)))
        >>> t = SetLink(4, SetLink(1, SetLink(5)))
        >>> t.union_set(s)
        SetLink(2, SetLink(4, SetLink(1, SetLink(5))))
        """
        union = self.copy()
        pointer = set2
        while pointer is not SetLink.empty:
            union.adjoin(pointer.first)
            pointer = pointer.rest
        return union
    
    ### Part2 of SetLink: 
    # below are functions defined for sorted SetLink objects -- compare the runtime efficiency for the same functions for
    # unsorted SetLink and sorted SetLink to see the impact on runtime efficiency between different data structures and algorithms
    def insert(self, v):
        """Insert value v into sorted SetLink self in increasing order.
        
        >>> s = SetLink(1, SetLink(2, SetLink(4, SetLink(7, SetLink(10)))))
        >>> s.insert(5)
        >>> s
        SetLink(1, SetLink(2, SetLink(4, SetLink(5, SetLink(7, SetLink(10))))))
        """
        ## this version returns a new list instead of reassigning and mutating the original SetLink s
        # if self is SetLink.empty or v < self.first:
        #     return SetLink(v, self)
        # elif v == self.first:
        #     return 
        # else:
        #     return SetLink(self.first, self.rest.insert(v))
        if v == self.first:
            return
    
        if v < self.first:
            # insert before current node by shifting values
            self.rest = SetLink(self.first, self.rest)
            self.first = v
            return
    
        if self.rest is SetLink.empty:
            self.rest = SetLink(v)
        else:
            self.rest.insert(v)

    
    def order_set(self):
        """Order the SetLink self in increading order.
        
        >>> s = SetLink(2, SetLink(4, SetLink(1, SetLink(10, SetLink(7)))))
        >>> s.order_set()
        >>> s
        SetLink(1, SetLink(2, SetLink(4, SetLink(7, SetLink(10)))))
        """
        if self.rest is SetLink.empty:
            return

        self.rest.order_set()

        if self.first > self.rest.first:
            self.first, self.rest.first = self.rest.first, self.first
            self.rest.order_set()
    
    def sorted_contains(self, v):
        """Return True if the sorted SetLink self contains value v, False otherwise. 
        ** self has to be sorted in increasing order

        >>> s = SetLink(2, SetLink(4, SetLink(1, SetLink(10, SetLink(7)))))
        >>> s.order_set()
        >>> s.sorted_contains(7)
        True
        >>> s.sorted_contains(5)
        False
        """
        if self.first == v:
            return True
        if self.first > v or (self.rest is SetLink.empty and self.first != v):
            return False
        return self.rest.sorted_contains(v)
    
    def sorted_intersect(self, s2):
        """Return a new SetLink containing all elements that are both in sorted SetLink self and sorted SetLink s2.
        ** self and s2 have to be sorted in increasing order

        >>> s = SetLink(2, SetLink(4, SetLink(1, SetLink(10, SetLink(7)))))
        >>> s.order_set()
        >>> s2 = SetLink(15, SetLink(7, SetLink(5, SetLink(1))))
        >>> s2.order_set()
        >>> t = s.sorted_intersect(s2)
        >>> t
        SetLink(1, SetLink(7))
        >>> s3 = SetLink(3, SetLink(5, SetLink(9)))
        >>> t2 = s.sorted_intersect(s3)
        >>> t2
        'None'
        """
        e1, e2 = self, s2
        intersect = "None"
        while e1 is not SetLink.empty and e2 is not SetLink.empty:
            if e1.first == e2.first:
                if intersect == "None":
                    intersect = SetLink(e1.first)
                    pointer = intersect
                else:
                    pointer.rest = SetLink(e1.first)
                    pointer = pointer.rest
                e1, e2 = e1.rest, e2.rest
            elif e1.first > e2.first:
                e2 = e2.rest
            else:
                e1 = e1.rest
        return intersect
    
    def sorted_adjoin(self, v):
        """Adjoin value v into SetLink self at the appropriate place, *self is a SetLink sorted in increasing order.
        
        >>> s = SetLink(2, SetLink(4, SetLink(1, SetLink(10, SetLink(7)))))
        >>> s.order_set()
        >>> s.sorted_adjoin(5)
        >>> s
        SetLink(1, SetLink(2, SetLink(4, SetLink(5, SetLink(7, SetLink(10))))))
        >>> s2 = SetLink(1, SetLink(2, SetLink(3)))
        >>> s2.sorted_adjoin(5)
        >>> s2
        SetLink(1, SetLink(2, SetLink(3, SetLink(5))))
        >>> s3 = SetLink(3, SetLink(5))
        >>> s3.sorted_adjoin(1)
        >>> s3
        SetLink(1, SetLink(3, SetLink(5)))
        """
        pointer = self
        while pointer.first < v and pointer.rest is not SetLink.empty:
            pointer = pointer.rest
        
        if pointer.first < v: #the case that reach the last element in SetLink self and pointer.rest is SetLink.empty
            pointer.rest = SetLink(v)
        elif pointer.first == v:
            return  #value v already in SetLink self, then nothing need to be done since sets do not allow duplicates
        else:
            pointer.first, pointer.rest = v, SetLink(pointer.first, pointer.rest)
        
    
    def sorted_union(self, s2):
        """Return a new SetLink containing all elements of the union of SetLink self and s2,
        *both self and s2 are SetLink sorted in increasing order.
        
        >>> s = SetLink(3, SetLink(5, SetLink(9, SetLink(6, SetLink(2)))))
        >>> s.order_set()
        >>> s2 = SetLink(9, SetLink(7, SetLink(2, SetLink(1, SetLink(5)))))
        >>> s2.order_set()
        >>> t = s.sorted_union(s2)
        >>> t
        SetLink(1, SetLink(2, SetLink(3, SetLink(5, SetLink(6, SetLink(7, SetLink(9)))))))
        """
        e1, e2 = self, s2
        union = None
        while e1 is not SetLink.empty and e2 is not SetLink.empty:
            if e1.first == e2.first:
                v = e1.first
                e1, e2 = e1.rest, e2.rest
            elif e1.first < e2.first:
                v = e1.first
                e1 = e1.rest
            else:
                v = e2.first
                e2 = e2.rest
            # add the next element to the union
            if union is None:
                union = SetLink(v)
                uni_pointer = union
            else:
                uni_pointer.rest = SetLink(v)
                uni_pointer = uni_pointer.rest

        if e1 is SetLink.empty:
            uni_pointer.rest = e2
        else:
            uni_pointer.rest = e1
        
        return union

            
# class: SetTree()
"""This class s binary tree representation of Python built-in Set object with set behavior. (no duplicates)
   This class is constructed in comparison to the SetLink class above to explore different possibility of data 
   representation, as well as to evaluate the impact of different dta structure and algorithm/function designs on runtime efficiency.
"""
class SetTree():
    empty = None
    def __init__(self, root, left=None, right=None):
        """The entry of the root of the tree holds one element of the set. 
        The entries within the left branch include all elements smaller than the one at the root. 
        Entries in the right branch include all elements greater than the one at the root.
        >>> t = SetTree(5, SetTree(3, SetTree(1), SetTree(4)), SetTree(8, SetTree(6), SetTree(10)))
        """
        self.root = root
        self. left = left
        self.right = right

        # Enforce BST property
        assert self.is_settree()

    def __repr__(self):
        if self.left is SetTree.empty and self.right is SetTree.empty:
            return f"SetTree({self.root})"
        return f"SetTree({self.root}, {repr(self.left)}, {repr(self.right)})"
    
    # ***this is a good example to enhance the property of a class through constructor and verification method(s)
    def is_settree(self, min_val=None, max_val=None):
        """Check that the SetTree self is a valid SetTree that satisfy the SetTree behavior.
        Recursively verify:
        min_val < self.entry < max_val
        """
        if min_val is not None and self.root <= min_val:
            return False
        if max_val is not None and self.root >= max_val:
            return False

        # Validate left subtree
        if self.left is not SetTree.empty:
            return self.left.is_settree(min_val, self.root)

        # Validate right subtree
        if self.right is not SetTree.empty:
            return self.right.is_settree(self.root, max_val)

        return True
    
    def contains(self, v):
        """Return True if the SetTree self contains value v, False otherwise.
        
        >>> t = SetTree(5, SetTree(3, SetTree(1), SetTree(4)), SetTree(8, SetTree(6), SetTree(10)))
        >>> t.contains(6)
        True
        >>> t.contains(9)
        False
        """
        if self.root == v:
            return True
        elif self.root < v:
            if self.right is SetTree.empty:
                return False
            else:
                return self.right.contains(v)
        else:
            if self.left is SetTree.empty:
                return False
            else:
                return self.left.contains(v)
    
    def add_val(self, v):
        """Add the value v as a leaf to SetTree v according to the SetTree behavior/property.
        
        >>> t = SetTree(5)
        >>> t.add_val(3)
        >>> t
        SetTree(5, SetTree(3), None)
        >>> t.add_val(8)
        >>> t
        SetTree(5, SetTree(3), SetTree(8))
        >>> t.add_val(4)
        >>> t
        SetTree(5, SetTree(3, None, SetTree(4)), SetTree(8))
        >>> t.add_val(3)   # duplicate, should do nothing
        >>> t
        SetTree(5, SetTree(3, None, SetTree(4)), SetTree(8))
        """
        if self.root == v:
            return
        elif self.root < v:
            if self.right is SetTree.empty:
                self.right = SetTree(v)
            else:
                self.right.add_val(v)
        else:
            if self.left is SetTree.empty:
                self.left = SetTree(v)
            else:
                self.left.add_val(v)
### To-do Deep Tree understanding and functions
    # def intersect(self, s2):
    #     """Return a SetTree containing elements common to self and s2.

    #     >>> t1 = SetTree(5,
    #     ...              SetTree(2),
    #     ...              SetTree(8, None, SetTree(9)))
    #     >>> t2 = SetTree(7,
    #     ...              SetTree(2),
    #     ...              SetTree(9))
    #     >>> t = t1.intersect(t2)
    #     >>> t
    #     SetTree(2, None, SetTree(9))

    #     >>> t3 = SetTree(1)
    #     >>> t1.intersect(t3)
    #     None
    #     >>> t1.intersect(t1)
    #     SetTree(2, None, SetTree(5, None, SetTree(8, None, SetTree(9))))
    #     """
    # def union(self, s2):
        # """
        # Return a SetTree containing all elements from self and s2.

        # >>> t1 = SetTree(5,
        # ...              SetTree(2),
        # ...              SetTree(8))

        # >>> t2 = SetTree(7,
        # ...              SetTree(2),
        # ...              SetTree(9))

        # >>> t = t1.union(t2)
        # >>> t
        # SetTree(2, None, SetTree(5, None, SetTree(7, None, SetTree(8, None, SetTree(9)))))

        # >>> t1.union(None)
        # SetTree(2, None, SetTree(5, None, SetTree(8)))

        # >>> t2.union(t2)
        # SetTree(2, None, SetTree(7, None, SetTree(9)))
        # """
    # def balance_settree(self):
        # """
        # Return a balanced version of self.

        # >>> t = SetTree(1,
        # ...              None,
        # ...              SetTree(2,
        # ...                       None,
        # ...                       SetTree(3,
        # ...                                None,
        # ...                                SetTree(4))))

        # >>> t
        # SetTree(1, None, SetTree(2, None, SetTree(3, None, SetTree(4))))

        # >>> b = t.balance_settree()
        # >>> b
        # SetTree(2,
        #         SetTree(1),
        #         SetTree(3, None, SetTree(4)))

        # >>> # Balanced tree should still contain same elements
        # >>> b.union(None)
        # SetTree(1, None, SetTree(2, None, SetTree(3, None, SetTree(4))))
        # """

## how to sort an unsorted tree?

### Lecture_data_examples  
## built-in functions & List comprehension 
def min_indices(s, f=abs):
    """Return a list of the indices of all elements in a list s that have the smallest f(s) value. f is by default abs.
    
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> min_indices(s)
    [2, 4]
    >>> s2 = [1, 2, 3, 4, 5]
    >>> min_indices(s2)
    [0]
    """
    f_list = [f(e) for e in s]
    return [i for i in range(len(s)) if f_list[i] == min(f_list)]

def largest_adjacent_sum(s):
    """Return the largest sum of two adjacent elements in a list s
    
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> largest_adjacent_sum(s)
    6
    >>> s2 = [-4, 3, -2, -3, 2, -4]
    >>> largest_adjacent_sum(s2)
    1
    """
    return max([s[i]+s[i+1] for i in range(len(s)-1)])

def last_digits(s):
    """Return a dictionary mapping each didgit d to the lists of elements in list s that ends with d
    
    >>> s = [5, 8, 13, 21, 34, 55, 89]
    >>> t = last_digits(s)
    >>> t
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    sorted_s = sorted(s, key=lambda x: x % 10)
    return {x % 10: [v for v in sorted_s if v % 10 == x % 10] for x in sorted_s}

def is_all_duplicate(s):
    """Return whether every element equal some other elment in s.
    
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> is_all_duplicate(s)
    False
    >>> s1 = [4, 3, 2, 3, 2, 4]
    >>> is_all_duplicate(s1)
    True
    >>> s2 = [3, 4, 2, 3, 2, 3, 4]
    >>> is_all_duplicate(s2)
    True
    """
    # version 1
    # sorted_s = sorted(s)
    # return all([(sorted_s[i] == sorted_s[i+1] or sorted_s[i] == sorted_s[i-1]) for i in range(1,len(s) - 1)])
    # version 2
    return min([s.count(x) for x in s]) > 1

### Lecture_data_examples  
## linked_list
def is_sorted(s, f=lambda x: x):
    """Return True if a linked list s is sorted in increasing order using function f.
    
    >>> s = Link(1, Link(3, Link(4)))
    >>> is_sorted(s)
    True
    >>> t = Link(1, Link(4, Link(3)))
    >>> is_sorted(t)
    False
    >>> s2 = Link(1, Link(-3, Link(4)))
    >>> is_sorted(s2, abs)
    True
    >>> t2 = Link(1, Link(4, Link(-3)))
    >>> is_sorted(t2, abs)
    False
    """
    pointer = s
    while pointer.rest is not Link.empty:
        if f(pointer.first) > f(pointer.rest.first):
            return False
        pointer = pointer.rest
    return True

def is_sorted_rec(s, f=lambda x: x):
    if s is Link.empty:
        return True
    elif f(s.first) > f(s.rest.first):
        return False
    else:
        return is_sorted_rec(s.rest, f)

def all_elements(s, t):
    """Return a new sorted Link containing all elements of both sorted Links s and t
    
    >>> s = Link(1, Link(5))
    >>> t = Link(1, Link(4))
    >>> all_elements(s, t)
    Link(1, Link(1, Link(4, Link(5))))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    if s.first <= t.first:
        return Link(s.first, all_elements(s.rest, t))
    else:
        return Link(t.first, all_elements(s, t.rest))

def sorted_combine(s, t):
    """Mutate sorted Link s and t so that they are the same sorted object containing all the elements 
       of both and no new Link is created
       
    >>> s = Link(1, Link(5))
    >>> t = Link(1, Link(4))
    >>> sorted_combine(s, t)
    Link(1, Link(1, Link(4, Link(5))))
    >>> s
    Link(1, Link(1, Link(4, Link(5))))
    >>> t
    Link(1, Link(4, Link(5)))
    """
    if s is Link.empty:
        return t
    elif t is Link.empty:
        return s
    if s.first <= t.first:
        # return Link(s.first, all_elements(s.rest, t))
        s.rest = sorted_combine(s.rest, t)
        return s
    else:
        # return Link(t.first, all_elements(s, t.rest))
        t.rest = sorted_combine(s, t.rest)
        return t

""" This section contains codes for cs61a Scheme section, the hw, lab, disc, and projects assignments
in Scheme will first be written in Python here then translate to Scheme in the assignments. """
### hw07
def pow(base, exp):
    """Return the base raised to the power of the nonnegative integer exp.

    >>> pow(8, 7)
    2097152
    >>> pow(6, 9)
    10077696
    """
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return pow(base, exp // 2) ** 2
    else:
        return base * pow(base, exp - 1)

### textbook3.4_Scheme_interpreter
# wrtiting Interepreter && Exception for Calculator in Python
def repeat(f, n):
    """Takes in a procedure f and a number n, and outputs a new procedure. 
    This new procedure takes in a number x and outputs the result of applying f to x a total of n times. 
    
    >>> square = lambda x: x * x
    >>> square_twice = repeat(square, 2)
    >>> square_twice(5)
    625
    >>> square_trice = repeat(square, 3)
    >>> square_trice(3)
    6561
    """
    def helper(x):
        if n == 0:
            return x
        else:
            return f(repeat(f, n-1)(x))
    return helper

def greatest_common_div(a, b):
    """Return the greatest common divisor of integers a and b using Euclid's algorithm

    >>> greatest_common_div(48, 18)
    6
    >>> greatest_common_div(36, 60)
    12
    """
    assert (a != 0 or b != 0) and isinstance(a, int) and isinstance(b, int)
    if b == 0:
        return a
    else:
        return greatest_common_div(min(a, b), max(a, b) % min(a, b))

def fit(total, n):
    """Returns whether there are n different positive perfect squares that sum to total.
    >>> fit(10, 2)
    True
    >>> fit(9, 1)
    True
    >>> fit(9, 3)
    False
    """
    max_int = int(math.sqrt(total))
    def square_sum(sum, n, k):
        if sum == 0 and n == 0:
            return True
        if k > max_int or sum < 0 or n < 0:
            return False 
        return any([square_sum(sum - k*k, n - 1, k + 1), square_sum(sum, n, k + 1)])
    return square_sum(total, n, 1)

#### Must use recursion since Scheme does not have for loop and relies entirely on recursion and higher-order functions
# def pair_up(s):
#     """Returns a linked list of lists that together contain all of the elements of s in order. 
#     Each list in the result should have 2 elements. The last one can have up to 3.
    
#     >>> pair_up(Link(3, Link(4, Link(5, Link(6, Link(7, Link(8)))))))
#     Link(Link(3, Link(4))) #[[3, 4], [5, 6], [7, 8]]
#     >>> pair_up(Link(3, Link(4, Link(5, Link(6, Link(7, Link(8, Link(9))))))))
#     [[3, 4], [5, 6], [7, 8, 9]]
#     """
#     pair_list = []
#     def pairs(s):
#         if s.rest.rest is Link.empty or s.rest.rest.rest is Link.empty:
#             pair_list.append(s)
#             return 
#         else:
#             pair = [s.first, s.rest.first]
#             pair_list.append(pair)
#             pairs(s.rest.rest)
#     pairs(s)
#     return pair_list
def interleave(s1, s2):
    """Return a new linked list that interleaves the elements of the two linked lists s1 and s2.
    The resulting list should contain elements alternating between s1 and s2, starting at s1.
    If one of the input lists to interleave is shorter than the other, then interleave should alternate elements from both lists until one list has no more elements, 
    and then the remaining elements from the longer list should be added to the end of the new list.
    
    >>> s1 = Link(1, Link(3, Link(5)))
    >>> s2 = Link(2, Link(4, Link(6, Link(8, Link(10)))))
    >>> interleave(s1, s2)
    Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(8, Link(10))))))))
    """
    if s1 is Link.empty:
        return s2
    if s2 is Link.empty:
        return s1
    return Link(s1.first, interleave(s2, s1.rest))

def no_repeat(s):
    """Returns a linked list that has all of the unique elements of linked list s in the order that they first appear, but no repeats.
    
    >>> s = Link(5, Link(4, Link(5, Link(4, Link(2, Link(1, Link(2)))))))
    >>> no_repeat(s)
    Link(5, Link(4, Link(2, Link(1))))
    """    
    if s is Link.empty:
        return s
    filtered_rest = filter_link(lambda x: x != s.first, s)
    return Link(s.first, no_repeat(filtered_rest))

def enumerate(s):
    """Takes in a linked list of values and returns a linked list of two-element lists, 
    where the first element is the index of the value, and the second element is the value itself.
    
    >>> s = Link(3, Link(4, Link(5, Link(6))))  # s = '(3 4 5 6)
    >>> enumerate(s)    # ((0 3) (1 4) (2 5) (3 6))
    Link(Link(0, Link(3)), Link(Link(1, Link(4)), Link(Link(2, Link(5)), Link(Link(3, Link(6))))))

    >>> s = Link.empty
    >>> enumerate(s)
    ()
    """
    def index_list(i, s):
        """Return a linked list of linked list of (i, s[i]) syntax"""
        if s is Link.empty:
            return s
        return Link(Link(i, Link(s.first)), index_list(i+1, s.rest))
    return index_list(0, s)

def scheme_merge(f, s1, s2):
    """Takes in a comparator function f and two linked lists that are sorted according to the comparator 
    and combines the two lists into a single sorted list. 
    A comparator defines an ordering by comparing two values and returning a true value if and only if the two values are ordered.
    
    >>> s1 = Link(1, Link(4, Link(6)))
    >>> s2 = Link(2, Link(5, Link(8)))
    >>> scheme_merge(lambda a, b: a < b, s1, s2)
    Link(1, Link(2, Link(4, Link(5, Link(6, Link(8))))))

    >>> s1 = Link(6, Link(4, Link(1)))
    >>> s2 = Link(8, Link(5, Link(2)))
    >>> scheme_merge(lambda a, b: a > b, s1, s2)
    Link(8, Link(6, Link(5, Link(4, Link(2, Link(1))))))

    >>> s1 = Link(1)
    >>> s2 = Link(2, Link(3, Link(5)))
    >>> scheme_merge(lambda a, b: a < b, s1, s2)
    Link(1, Link(2, Link(3, Link(5))))
    """
    if s1 is Link.empty:
        return s2
    if s2 is Link.empty:
        return s1
    
    if f(s1.first, s2.first):
        return Link(s1.first, scheme_merge(f, s1.rest, s2))
    elif f(s2.first, s1.first):
        return Link(s2.first, scheme_merge(f, s1, s2.rest))
    else:
        return Link(s1.first, scheme_merge(f, s1.rest, s2.rest))

def scheme_zip(s):
    """Return a linked list that zips the elements of a linked list s.
    
    >>> s = Link(Link(1, Link(2)), Link(Link(3, Link(4)), Link(Link(5, Link(6)), Link.empty))) #((1 2) (3 4) (5 6))
    >>> scheme_zip(s) # ((1 3 5) (2 4 6))
    Link(Link(1, Link(3, Link(5))), Link(Link(2, Link(4, Link(6)))))
    """
    if s is Link.empty or s.first is Link.empty:
        return Link.empty
    else:
        return Link(map_link(lambda lst: lst.first, s),scheme_zip(map_link(lambda lst: lst.rest, s)))
    
def scheme_print(s):
    """Print the Link list in Python into Scheme list structure/ the scheme list repr of Link list
    
    >>> s = Link(Link(1, Link(3, Link(5))), Link(Link(2, Link(4, Link(6)))))
    >>> scheme_print(s)
    ((1 3 5) (2 4 6))
    """
    def helper(lst):
        if lst is Link.empty:
            return ""
        
        first = lst.first
        
        if isinstance(first, Link):
            first_str = "(" + helper(first) + ")"
        else:
            first_str = str(first)
        
        rest_str = helper(lst.rest)
        
        if rest_str:
            return first_str + " " + rest_str
        else:
            return first_str

    print("(" + helper(s) + ")")

"""Note: Interpreter for Scheme Calculator

   Calculator Binary Tree Structure:
   Construction:
   - #s are all leaves, can NOT have children nodes
   - if "(" (left-parantethese) -> next symbol/# is the child of the current node
        - if current node is a #, go to the parent of the current node, 
        if the parent node's both children are filled, go to the parent of the parent node
   Computation:
   - the value of the operator nodes are the result of applying the operator to all of the node's children
   - if x.is_leaf(): return x

   ## the above structure only works when each () contains exactly 1 operator and 2 operands, which can
   be constructed into BTS. What if there is only 1 or more than 2 operands within a ()? 
   * use () to indicate the start and end of a procedure
   * construct non-binary Tree structure

   Calculator Non-Binary Tree Structure 
   Construction:
   - # node are leaves, have no children -- return to parent
        - if x.value is #: return to x.parent
    - for parentethese:
        - if '('
            - fill in the '(' to the next operator node, and the element next to the operator node is added as a child/branch to the operator node, move to the child node
                - x = the operator next to/after '('
                - x.right_parentethese = True
                - x.branches/x.children.append(next_element)
                - move the pointer to next element
        - if ')'
            - fill in the ')' to the curent operator node, and return to the parent node
                - x.left_parentethese = True
                - return to x.parent
    Computation: same logic as BTS calculator
"""
### this function is used as a tokenizer && parser to transform Scheme input into linked list structure data for evaluation,
# this function aims at helping myself with uderstanding the nesting structure of the data
# this way our interpreter use linked list structure instead of tree AST structure 
def scheme_parse(s):
    """Return a linked list on each element of s nested based on '(' and ')' syntax.

    # >>> s = "(+ 1 (* 2 3))"
    # >>> scheme_parse(s)
    # Link('+', Link(1, Link(Link('*', Link(2, Link(3, nil))), nil)))
    # >>> s = "((a b c) (+ 1 3) (+ a b) (- 2 4))"
    # Link(Link('a', Link('b', Link('c', nil))), Link( Link('+', Link(1, Link(3, nil))), Link(Link('+', Link('a', Link('b', nil))), Link(Link('-', Link(2, Link(4, nil))), nil))))
    """
    ...

# Scheme @trace 
# ; (trace (sum 5))
# (define-macro (trace expr)
#     (let ((fn (car expr))
#         (arg (car (cdr expr))))
#         `(begin
#             (define original ,fn)
#             (define ,fn 
#                 (lambda (n) 
#                     (begin (print ',fn n) (original n))))
#             (define result (,fn ,arg))
#             (define ,fn original)
#             result
#         )
#     )
# )
def square(n):
    return n * n
def pow_exp(base, exp):
    """Return the result of raising base to the power of exp
    
    >>> pow_exp(2, 15)
    32768
    >>> pow_exp(3, 7)
    2187
    """
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return square(pow_exp(base, exp / 2))
    else:
        return base * pow_exp(base, exp - 1)
def pow_expr(base, exp):
    """Return the string representation of the process of raising base to the power of exp"""



## discussion_12
def word_rope(s):
    """Return a rope of the words in string s.
    >>> word_rope('the last week')
    ['t', 'h', 'e', ['l', 'a', 's', 't', ['w', 'e', 'e', 'k']]]
    """
    if len(s) == 1:
        return [s[0]]
    else:
        if s[0] == ' ':
            return [word_rope(s[1:])]
        else:
            return [s[0]] + word_rope(s[1:])

def linear(s):
    """Return the longest linear sublist of a linked list s.
        A linear sublist of a linked list of numbers s is a sublist in which the difference between adjacent
        numbers is always the same. For example <2 4 6 8> is a linear sublist of <1 2 3 4 6 9 1 8 5> because the
        difference between each pair of adjacent elements is 2.

    >>> s = Link(9, Link(4, Link(6, Link(7, Link(8, Link(10))))))
    >>> linear(s)
    Link(4, Link(6, Link(8, Link(10))))
    >>> linear(Link(4, Link(5, s)))
    Link(4, Link(5, Link(6, Link(7, Link(8)))))
    >>> linear(Link(4, Link(5, Link(4, Link(7, Link(3, Link(2, Link(8))))))))
    Link(5, Link(4, Link(3, Link(2))))
    """
    def complete(first, rest):
        """The longest linear sublist of Link(first, rest) with difference d."""
        if rest is Link.empty:
            return Link(first, rest)
        elif rest.first - first == d:
            return Link(first, complete(rest.first, rest.rest))
        else:
            return complete(first, rest.rest)
    
    if s is Link.empty:
        return s
    longest = Link(s.first) # The longest linear sublist found so far
    while s is not Link.empty:
        t = s.rest
        while t is not Link.empty:
            d = t.first - s.first
            candidate = Link(s.first, complete(t.first, t.rest))
            if length(candidate) > length(longest):
                longest = candidate
            t = t.rest
        s = s.rest

    return longest

def length(s):
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)
        

## discussion_12
def up(n):
    """Takes a positive integer n and return a linked list rope containing the digits of n 
    that is the shortest rope in which each pair of adjacent numbers in the same list are in increasing order.

    >>> s = up(314152667899)
    >>> scheme_print(s)
    (3 (1 4 (1 5 (2 6 (6 7 8 9 (9))))))
    """
    power = math.floor(math.log10(n))   # scheme equivalent: (/ (log x) (log 10))
    first_digit, rest = n // 10**power, n % 10**power
    second_digit = rest // 10**(power-1)
    if n < 10:
        return Link(n)
    else:
        if first_digit < second_digit:
            return Link(first_digit, up(rest))
        else:
            return Link(first_digit, Link(up(rest)))

### final lecture: lecture_38
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches:
            return f"Tree({self.label}, {self.branches})"
        else:
            return f"Tree({self.label})"

def bigs(t):
    """Return the number of nodes in t that are larger than all their ancestors. 
    (the root node is counted/considered as bigger than all its ancectors)
    
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(a)
    4
    >>> b = Tree(1, [Tree(4, [Tree(4), Tree(3, [Tree(7)])]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(b)
    4
    """
    def f(t, max):
        """"""
        if t.label > max:
            return 1 + sum([f(b, t.label) for b in t.branches])
        else:
            return sum([f(b, max) for b in t.branches])
    return f(t, t.label - 1)

def bigs_2(t):
    """Return the number of nodes in t that are larger than all their ancestors (different approach than big()). 
    (the root node is counted/considered as bigger than all its ancectors)
    
    >>> a = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs_2(a)
    4
    >>> b = Tree(1, [Tree(4, [Tree(4), Tree(3, [Tree(7)])]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs_2(b)
    4
    """
    n = [0]
    
    def f(t, max):
        if t.label > max:
            n[0], max = n[0] + 1, t.label 
        for b in t.branches:
            f(b, max)
    
    f(t, t.label - 1)
    return n[0]

def smalls(t):
    """Return the non-leaf nodes in t that are smaller than all their descendants
    
    >>> a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """
    result = []

    # def min_desc(t):
    #     """Return the minimun label of all descendants of tree t """
    #     if t.is_leaf():
    #         return t.label
    #     return min(t.label, min([min_desc(b) for b in t.branches]))
    # def f(t):
    #     """Add all nodes in t that are smaller than all their descendants to result"""
    #     if not t.is_leaf():
    #         # compute min among descendants ONLY
    #         min_d = min([min_desc(b) for b in t.branches])
    #         if t.label < min_d:
    #             result.append(t)
    #     for b in t.branches:
    #         f(b)
    # f(t)

    def min_desc(t):
        """Return the minimun label of all descendants of tree t and add t to result if t is smaller than all its descendants"""
        if t.is_leaf():
            return t.label
        
        min_d = min([min_desc(b) for b in t.branches])
        if t.label < min_d:
            result.append(t)
        return min(t.label, min_d)
    
    min_desc(t)
    return result 
        


""" Below is personal doctest function that allows for terminal command: 'python3 file_name.py'
    to run doctest on a specific funciton in the file, 
    by default it prints the number of tests a function pass/fail,
    and provide the option to print all/passed/failed cases.
    *** to run doctest on the entire file, terminal command: python3 -m doctest -v file_name.py
"""
import doctest
import io
import contextlib

def run_doctest_for_function(func, show="fail"):
    """
    show options:
      - "fail": print only failed cases
      - "pass": print only passed cases (summary-style)
      - "all":  print everything
      - "none": print only summary
    """
    finder = doctest.DocTestFinder()
    runner = doctest.DocTestRunner(verbose=False)

    output = io.StringIO()

    with contextlib.redirect_stdout(output):
        tests = finder.find(func)
        for test in tests:
            runner.run(test)

        failed, attempted = runner.summarize(verbose=False)

    text = output.getvalue()

    passed = attempted - failed

    print("\nSummary")
    print("-------")
    print(f"Total:  {attempted}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if show == "none":
        return

    print("\nDetails")
    print("-------")

    if show == "all":
        print(text.strip() or "(no output)")

    elif show == "fail":
        if failed == 0:
            print("No failed tests 🎉")
        else:
            print(text.strip())

    elif show == "pass":
        if passed == 0:
            print("No passed tests")
        else:
            print(f"{passed} tests passed ✅")


if __name__ == "__main__":
    run_doctest_for_function(match_k, show="all")



