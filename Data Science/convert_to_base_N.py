
N = int(input("Enter the base: "))
if (N >= 17):
    raise ValueError("Base must be less than 17")
    
s = ''
def convert(num, base):
    if (num == 0):
        return '0'
    s = ''
    n = num
    while (n != 0):
        rem = n % base
        n = n // base
        if (rem >= 10):
            s += chr(65 + (rem % 10))
            pass
        else:
            s += str(rem)
    return s[::-1]

for i in range(50):
    print(f"Base 10: {i} \t Base {N}: {convert(i, N)}")
