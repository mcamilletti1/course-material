def contains_duplicates(xs):
    found = set()
    for x in xs:
        if x in found:
            return True
        found.add(x)
    return False


def find_duplicates(xs):
    found = set()
    listed = set()
    result = []

    for x in xs:
        if x in found and x not in listed:
            listed.add(x)
            result.append(x)
        found.add(x)

    return result
