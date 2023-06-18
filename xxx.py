from math import log2
def getcrc(message):
    register = [0]*17
    for i in message:
        register.pop(0)
        register.append(int(i))
        if register[0] == 1:
            register[0] ^= 1
            register[4] ^= 1
            register[11] ^= 1
            register[16] ^= 1
    return "".join([str(i) for i in register[1:]])
msg = input("enter the input in  binary form")
crc = getcrc(msg+'0'*16)
print(f'the message sent with crc is {msg+crc}')
m = input("enter the message received\t")
for i in range(20):
    n = ""
    n = m[:i]
    if m[i] == '0':
        n += '1'
    else:
        n += '0'
    n += m[i+1:]
    print(n)
    print(m)
    n = getcrc(n)
    print(n)
    if int(n,base=2) == 0:
        print("there is no error")
    else:
        x = 0
        for i in n[::-1]:
            x += 1
            if i == '1':
                break
        print(f'the error is in {x}')