from pprint import pprint


lst = [
    {
        'bin': bin(b),
        'dec': b,
        'hex': hex(b),
        'oct': oct(b),
    }
    for b in range(0, 16)]
pprint(lst)
#
