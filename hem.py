import random

def hamming(code):
    result = ''
    
    
    code_word=list(code)
    for n in range(0,len(code_word)):
        bin=code_word[n]
        bin=int(bin)
        code_word[n]=bin
    
    k=0
    for n in range(1,10):
        if 2**n>=len(code_word)+n+1:
            k=n
            break
    
    for n in range(0,k):
        code_word.insert(2**n-1, 0)
    
    leen=len(code_word)-1
    for n in range(0,k):
        check_dec=0
        for i in range(2**n-1,len(code_word), 2**n*2):
            for j in range(0, 2**n):
                if (i+j)<=leen:
                    check_dec+=code_word[i+j]
        code_word[2**n-1]=check_dec%2
    
    result += ' '.join(map(str, code_word)).replace(' ', '') + '\n'#to string
    return result

def decod_hamming(code):
    k=0
    while True:
        if 2**k>=len(code)+k+1:
            break
        else:
            k+=1
    arrk=[0,0,0,0,0,0,0,0,0]

    leen=len(code)-1
    for n in range(0,k):
            check_dec=0
            for i in range(2**n-1,len(code), 2**n*2):
                for j in range(0, 2**n):
                    if (i+j)<=leen:
                        check_dec+=code[i+j]
            arrk[n]=check_dec%2

    for n in range(0,k):
        check_dec=0
        for i in range(2**n-1,len(code), 2**n*2):
            check_dec=code[i]
            if check_dec!=arrk[n]:
                if code[i]==1:
                    arrk[n]=0
                else:
                    arrk[n]=1
    sum=0
    for i  in range(0,8):
        sum+=arrk[i]*2**i
    sum-=1
    if sum!=-1:
        if code[sum]==1:
            code[sum]=0
        else:
            code[sum]=1


    k=0
    for n in range(1,10):
        if 2**n>=len(code)+1:
            k=n
            break
    k-=1
    for i in range(k,-1,-1):
        code.pop((2**i)-1)



    if sum==-1:
        return code
    else:
        return (code, sum)

ran=random.randint(3,5)
les=[]
for i in range(0, ran):
    les.append(random.randint(0,1))

counte=3
abc=['a','b','c','d','e','g',]
ret=[]
les=[]
ran=random.randint(3,5)
for n in range(0, counte):
    les=[]
    for i in range(0, ran):
        les.append(random.randint(0,1))
    les=hamming(les)
    les=list(les)
    les.append(" ")
    del les[-2]
    les.insert(0, abc[n])
    les.insert(1, ':')
    print(les)
    for n in range(0, len(les)):
        ret.append(les[n])
ret2=ret[0]
for n in range(1, len(ret)):
    ret2=ret2[:n]+ret[n]
print(ret2)