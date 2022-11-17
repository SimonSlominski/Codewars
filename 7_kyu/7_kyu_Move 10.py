def move_ten(st):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for char in st:
        for idx, value in enumerate(letters):
            if value == char:
                if idx+1 <= 16:
                    result.append(letters[idx+10])
                if idx+1 > 16:
                    result.append(letters[idx+10-26])
    return "".join(result)


# Second Solution
# from string import ascii_lowercase
#
#
# def move_ten(st):
#     new_word = str.maketrans(ascii_lowercase, ascii_lowercase[10:] + ascii_lowercase[:10])
#     return st.translate(new_word)


# Third solution
# def move_ten(st):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     return ''.join(letters[(letters.find(c)+10)%26] for c in st)
