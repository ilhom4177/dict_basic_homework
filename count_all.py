def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    i = 0
    counted = {}
    alpha = 0
    digit = 0
    while i < len(txt):
        if txt[i].isalpha():
            alpha += 1
        if txt[i].isdigit():
            digit += 1
        counted["LETTERS"] = alpha
        counted["DIGITS"] = digit
        i += 1
    return counted
print(count_all('Codeschool 2023'))