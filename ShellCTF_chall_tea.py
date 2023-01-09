def rev_addSuger(n):
    x = len(n)//2
    a = n[:x]
    b = n[x:]
    c = ''
    for i,j in zip(a,b): 
        c += chr(j) + chr(i)
    return c 

def rev_addTea(n):
    flag = []
    for i in range(16):
        flag.append(n[i] + 3 * (i // 2))
    for i in range(16,32):
        flag.append(n[i] - i//6)
    return flag

def rev_addMilk(n): 
    for i in range(32):
        for j in range(i,32):
            check = 0 
            a = n[:i]
            b = n[i:j]
            c = n[j:]
            d = c + b + a
            d = rev_addSuger(rev_addTea(d))
            if d.startswith('shellctf{') and d.endswith('}'): 
                print(d)

cipher = 'R;crc75ihl`cNYe`]m%50gYhugow~34i'
flag = []
for i in cipher:
    flag.append(ord(i))
rev_addMilk(flag)
# shellctf{T0_1nfiNi7y_4nD_B3y0nd}
