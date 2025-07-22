name = ["prajwal", "ramesh","suresh","ram shyam","sh"]
def strp(n,word):
    nm = []
    for item in name:
        if not(item == word):
            nm.append(item.strip(word))
    return nm
print(strp(name,"sh"))