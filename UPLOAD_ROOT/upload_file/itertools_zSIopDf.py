import itertools
#count
'''for i in itertools.count(5 , 9):
    print(i)
    if i == 10:
        break
###########
a= itertools.count(0.5 , 0.75)
print(next(a))
###########
a = ['a' ,'b' , 'c' , 'd ']
print(list(zip(itertools.count() , a)))'''
#cycle
'''for i in itertools.cycle('AMI'):
    print(i)
    ######
a = ['amir' , 1380]
for i in itertools.cycle(a):
    print(a)
    #####
a = ['amir' , 1380]
b = itertools.cycle(a)
while True:
    print(next(b))'''
#repeat
'''a = 'amir'

print(list(itertools.repeat(a , 5)))'''
#zip_longerst
'''a = [1,2,3,4,5]
b = [52,60,80,88]
print(list(zip(a , b)))
print(list(itertools.zip_longest(a ,b)))'''
#combination
'''a = [1,2,3,4,5,6]
#میخواهیم تعداد زیر مجموعه های سه عضوی ان را مشخص کینم
b = list(itertools.combinations(a  , 3))
print(b)
print(len(b))
######
a = ['s1' , 's2' , 's3' , 's4' , 's5' , 'r1' , 'r2' , 'r3' , 'r4']
b = list(itertools.combinations(a , 4))
counter4 =0 #for kol
for i in b:
    counter3 = 0#for len of list
    counter = 0
    counter2 = 0
    for ii in i:
        counter3 +=1
        if ii in ['s1' , 's2' , 's3' , 's4' , 's5']:
            counter+=1
        if ii in ['r1' , 'r2' , 'r3' , 'r4']:
            counter2 +=1
        if counter3 == 4:
            if counter > counter2:
                counter4 +=1
print(counter4)
######
a = [1,2,3,4,5,6,7]#1,2 = دروازه بان
b = list(itertools.combinations(a , 3))
counter = 0
for i in b:
    counter2 = 0
    counter3 =0
    counter4=0
    for ii in i:
        counter4 +=1
        if ii == 1:
            counter2+=1
        if ii == 2:
            counter3 +=1
        if counter4 == 3:
            if counter2 >=1 and counter3 >=1:
                continue
            else:
                counter +=1
print(counter)
#############
a = [1,2,3,4,5]
b = list(itertools.combinations(a , 2))
c = list(itertools.combinations(a , 3))
d = list(itertools.combinations(a , 4))
e = list(itertools.combinations(a , 5))
print(sum(list(map(lambda f:len(f) , [b , c ,d ,e]))))
#############
a = ['ab' , 'cd' , 'ef' , 'gh' , 'ij' , 'kl' ,'mn']
b= list(itertools.combinations(a , 2))
c =len(b)
d = list(itertools.combinations(['a' , 'b' , 'c', 'd', 'e','f' ,'g','h' ,'i' ,'j' ] , 2))
e = len(d)-5
print(c*e)'''
#combination with replacement
'''a = [1,2,3,4]
print(len(list(itertools.combinations(a,2))))
print(list(itertools.combinations(a,2)))
print(len(list(itertools.combinations_with_replacement(a,2))))
print(list(itertools.combinations_with_replacement(a,2)))'''
#permutations
'''a = [1,2,3,4,5]
print(list(itertools.permutations(a)))
print(len(list(itertools.permutations(a))))
#permutations = n! = n*(n-1)*(n-2)*.....
#########
a = [1,2,3,4,5]
print(len(list(itertools.permutations(a)))*2)
#########
a = ['a1' , 'a2' , 'q1' , 'q2' , 'q3' , 's1' , 's2' , 's3' , 's4']
print(len(list(itertools.permutations(a))))
a = ['a1' , 'a2' ,['q1' , 'q2' , 'q3'] ,'s1' , 's2' , 's3' , 's4' ]
print(len(list(itertools.permutations(a))) * len(list(itertools.permutations(a[2]))))
a = [['a1' , 'a2'] ,['q1' , 'q2' , 'q3'] ,['s1' , 's2' , 's3' , 's4' ]]
print(len(list(itertools.permutations(a))) * len(list(itertools.permutations(a[0]))) * len(list(itertools.permutations(a[1]))) * len(list(itertools.permutations(a[2]))))
a = ['a1' , 'a2' , 'q1' , 'q2' , 'q3' , 's1' , 's2' , 's3' , 's4']
b = [['a1' , 'a2'] , 'q1' , 'q2' , 'q3' , 's1' , 's2' , 's3' , 's4']
print(len(list(itertools.permutations(a))) - (len(list(itertools.permutations(b))) * len(list(itertools.permutations(b[0])))))'''
#accumulate
'''import operator
a=[1 ,2 , 3]
def amir(a ,b):
    return a+b
print(list(itertools.accumulate(a,amir)))
#########
import operator
a=[1 ,2 , 3]
print(list(itertools.accumulate(a , operator.add)))'''
#product
'''a = ['amir' , 'amirali']
b = [1380 , 1388]
c = [1,2 ,3]
print(list(itertools.product(a , b , c)))
##########
from time import perf_counter
start = perf_counter()
a = ['king' , 'Queen' , 'Soldier', 10 , 9,8,7,6,5,4,3,2,1]
b = ['piq' , 'chesht' , 'del' , 'geshniz']
c = list(itertools.product(a , b))
print(c)
print(len(c))
end = perf_counter()
print(end - start)

start = perf_counter()
d = []
for i in a:
    for ii in b:
        d.append((i , ii))
        print(i, ii)
print(len(d))
end = perf_counter()
print(end - start)'''
#tee
'''a = [1,2,3,4,5,6,7,8]
b , c  = itertools.tee(a , 2)
print(next(b))
print(next(c))
##########
a = ['amir' , 1380 , 'amirali' , 1388 , 'azita' , 1360 , 'ebrahim' , 1352]
b ,c = itertools.tee(a  , 2)
for i in b :
    if type(i) == int:
        print(i)

for ii in c:
    if type(ii) == str:
        print(ii)'''
#islice
'''a = ['amirali' , 'amirhosein' , 'azita' , 'ebrahim']
b = list(itertools.islice(a ,0 , 4 , 2))
print(b)
print(list(itertools.islice('ABCDEFG', 2, 5)))
print(list(itertools.islice([1, 2, 3, 4, 5], 0, 5, 2)))
print(list(itertools.islice(range(10), 3, None)))
print(list(itertools.islice('ABCDE', 4)))'''
#chain
'''a =['amir' , 1380]
b = ['amirali' , 1388]
print(list(itertools.chain(a , b)))
###########
a = 'whats the'
b = 'fuck'
print(list(itertools.chain((a , b , 'shut up'))))'''
#chain_from_iterable
'''a =[1,2,3,4,5]
b = ['amir' , 'amirali']
print(list(itertools.chain.from_iterable((a ,b))))'''
#fiterfalse
'''a = [1350, 18.5 , 1380 , 0.5]
print(list(itertools.filterfalse(lambda x: type(x) == float, a)))
#########
a = list(i for i in range(0, 100) if i<=21)
print(list(itertools.filterfalse(lambda x : x%2 == 0 , a)))'''
#takewhile
'''a = [2,4,6,8,10,11,3,5]

print(list(itertools.takewhile(lambda x: x%2 == 0 , a)))'''
#dowhile
'''a = [2,4,6,5,4,98]

print(list(itertools.dropwhile(lambda x: x%2 == 0  , a)))'''
#comperess
'''a = list(i for i in range(0,11))

print(list(itertools.compress('Amir hosein' , list(1 if i%2 == 0 else 0 for i in range(0,11)))))'''
#starmap
'''a = [[1380,8,8] , (52,6,60) , (1,2,3)]
print(list(itertools.starmap(lambda x , y ,z: 'yes' if x<y<z else 'no', a)))
#########
a = {(1,3,5) : (561,6548,8)}
print(a[(1,3,5)])
print(list(itertools.starmap(min , a)))
########
a = {(1,3,5) , (561,6548,8)}
print(list(itertools.starmap(min , a)))'''