def any_in_any(a, b):
    """return true if any item of 'a' is found
    inside 'b'
    else return false
    """
    if len([x for x in a if x in b]) > 0:
        return True
    else:
        return False


def all_in_any(a, b):
    """return true if every item of 'a' is found
    inside 'b'
    else return false
    """
    if len([x for x in a if x in b]) == len(a):
        return True
    else:
        return False


def all_in_all(a, b):
    """return true if every item of 'a' is matched
    with every item in 'b'
    else return false
    """
    if len([x for x in a if x in b]) == len(a) == len(b):
        return True
    else:
        return False


def value_in_many_any(a, b):
    """return true if item 'a' is found
    inside 'b': a list/tuple of many iterators
    else return false
    """
    for c in b:
        if a in c:
            return True
    return False


def any_in_many_any(a, b):
    """return true if any item of 'a' is found
    inside 'b': a list/tuple of many iterators
    else return false
    """
    for c in b:
        if any_in_any(a, c):
            return True
    return False
