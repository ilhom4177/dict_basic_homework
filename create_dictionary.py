def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    i = 0
    dict = {}
    while i < len(key):
        dict[key[i]] =  value[i]
        i +=1
    return dict
print(create_dictionary([1,2,3],['o','p','r']))