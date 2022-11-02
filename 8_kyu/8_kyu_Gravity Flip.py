def flip(d, a):
    if d == "L":
        return sorted(a, reverse=True)
    else:
        return sorted(a, reverse=False)
