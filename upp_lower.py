def upp_lower(string):
    upper=0
    lower=0
    for char in string:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    print(" No. of upper case character:",upper)
    print("No. of lower case character:",lower)
upp_lower("The quick Brow Fox")