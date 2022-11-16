
from msilib import sequence
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


def foo(d):
    true=True 

    while true:
        ran=random.randint(3,5)
        les=[]
        for i in range(0, ran):
            les.append(random.randint(0,1))

        counte=3
        abc=['a','b','c','d','e','g',]
        abc2="a,b,c,d,e,g"
        ret=[]
        les=[]
        #ran=random.randint(3,5)
        ran=d
        randlol=random.randint(1,2)
        for n in range(0, counte):
            les=[]
            for i in range(0, ran):
                les.append(random.randint(0,1))
        
            for i in range(randlol):
                les=hamming(les)
                les = les[:-1]
            les=list(les)
            les.append(" ")
            #del les[-2]
            les.insert(0, abc[n])
            les.insert(1, ':')
            print(les)
            for n in range(0, len(les)):
                ret.append(les[n])
        ret2=ret[0]
        text="Задание 13 [короткий ответ]. По каналу связи с помощью равномерного двоичного корректирующего кода Хэмминга передаются сообщения, содержащие только 4 буквы: . Кодовые слова для всех четырёх букв известны:. Сколько ошибок может исправить такой код?"
        for n in range(1, len(ret)):
            ret2=ret2[:n]+ret[n]
        print(ret2)
        text=text[:156] + abc2[:5] +text[156:204] +ret2 +text[204:]
        print(text)

        diff=5
        arr=[]
        arr2=[]
        #sequenc=1
        for sequenc in range(1, counte):
            for i in range((sequenc-1)*len(les), (sequenc)*len(les)-3):
                arr.append(ret2[i+2])

            for i in range((sequenc),counte):
                g=0
                for j in range(len(les)*i, len(les)*i-3+len(les)):
                    arr2.append(ret2[j+2])
                #print(arr2)
                for j in range(0,len(les)-3):
                    if arr[j]!=arr2[j]:
                        g=g+1
                arr2=[]
                #print(g)
                if g<diff:
                    diff=g
                #print(diff)
            arr=[]

        #print(arr)
        print(diff, randlol)
        if diff !=0 and diff !=4:
            true=False
        return diff, text

foo(5)


