slova = input().split()
def jiki(x):
    return len(x)
slova.sort(key=jiki)
print(slova)