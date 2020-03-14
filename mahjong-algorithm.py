A = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[2]]
B = [[1,1,1],[1,1,1],[1,1,1],[3],[2]] 
C = [[1,1,1],[1,1,1],[3],[3],[2]]
D = [[1,1,1],[3],[3],[3],[2]]
E = [[3],[3],[3],[3],[2]]
F = [[2],[2],[2],[2],[2],[2],[2]]

MAN1 = 0
MAN2 = 1
MAN3 = 2
MAN4 = 3
MAN5 = 4
MAN6 = 5
MAN7 = 6
MAN8 = 7
MAN9 = 8
PIN1 = 9
PIN2 = 10
PIN3 = 11
PIN4 = 12
PIN5 = 13
PIN6 = 14
PIN7 = 15
PIN8 = 16
PIN9 = 17
SOU1 = 18
SOU2 = 19
SOU3 = 20
SOU4 = 21
SOU5 = 22
SOU6 = 23
SOU7 = 24
SOU8 = 25
SOU9 = 26
TON = 27
NAN = 28
SHA = 29
PEI = 30
HAK = 31
HAT = 32
CHU = 33

tiles = [	
MAN1,
MAN2,
MAN3,
MAN4,
MAN5,
MAN6,
MAN7,
MAN8,
MAN9,
PIN1,
PIN2,
PIN3,
PIN4,
PIN5,
PIN6,
PIN7,
PIN8,
PIN9,
SOU1,
SOU2,
SOU3,
SOU4,
SOU5,
SOU6,
SOU7,
SOU8,
SOU9,
TON, 
NAN, 
SHA, 
PEI, 
HAK, 
HAT, 
CHU
]

import random
import time
import numpy as np

def isswap(array,i,j):
    if i == j:
        return True
    for n in range(i,j):
        if array[n] != array[j]:  
            continue
        else:
            return False
    return True
def permutations(arr, begin, end,ret):
    if begin == end:
        ret.append(arr.copy())
    else:
        for index in range(begin, end):
            if isswap(arr,begin,index):
                arr[index], arr[begin] = arr[begin], arr[index]
                permutations(arr, begin + 1, end,ret)
                arr[index], arr[begin] = arr[begin], arr[index]


def hucombine(a,ret):
	if(len(a)==1):
		ret.append(a)
		return
	permutations(a,0,len(a),ret)
	h1 = dict()
	for i in range(len(a)):
		for j in range(i+1,len(a)):
			key = str(a[i]+a[j])
			h2 = dict()
			if not key in h1:
				h1[key] = 0
				for k in range(len(a[i])+len(a[j])+1):
					t = [0]*len(a[j]) + a[i] + [0]*len(a[j])
					for m in range(len(a[j])):
						t[k+m] += a[j][m]
					while 0 in t:
						t.remove(0)
					if (len(list(filter(lambda x: x>4,t)))>0):
						continue
					if(len(t)>9):
						continue
					if not str(t) in h2:
						h2[str(t)] = 0
						tr = a.copy()
						del tr[i]
						del tr[j-1]
						hucombine([t]+tr,ret)


def decode(a):
	ret = 0
	len = -1
	for b in a:
		for i in b:
			len += 1
			if i==2:
				ret |= 0b11 << len
				len += 2
			elif i==3:
				ret |= 0b1111 << len
				len += 4
			elif i==4:
				ret |= 0b111111 << len
				len += 6
		ret |= 0b1 << len
		len += 1		
	return hex(ret)



def tilestoint(a):
	tiles = [0]*34
	for i in a:
		tiles[i] += 1
	return tiles

def mahjongcase(a):
	ret = []
	group = []
	for i in range(len(a)-7):
		if a[i] != 0:
			group.append(a[i])
			if(i==9 or i == 18):
				ret.append(group.copy())
				group.clear()

		else:
			ret.append(group.copy())
			group.clear()

	for i in range(len(a)-7,len(a)):
		if a[i] != 0:
			group.append(a[i])
			ret.append(group.copy())
			group.clear()
	while [] in ret:
		ret.remove([])
	return ret

'''
test = []
hucombine(A,test) 
hucombine(B,test) 
hucombine(C,test) 
hucombine(D,test) 
hucombine(E,test) 
hucombine(F,test) 

hu = dict()
test1 = np.array(test)
test2 = np.unique(test1)
print(len(test2))
for i in test2:
	hu[decode(i)] = None

'''
def analysis(p):
	ret = {}	
	for i in tiles:
		for ke_shun in range(2):
			jiang = 0
			kezi = []
			shunzi = []
			gang = []
			t = []
			t = p.copy()
			if t[i] >= 2:
				t[i] -= 2
				jiang = i
				if ke_shun == 0:
					for j in tiles:
						if t[j] >= 3:
							if t[j] == 3:
								kezi.append(j)
							if t[j] == 4:
								gang.append(j)
							t[j] -= t[j]
					for a in range(3):
						b = 0
						while b<7:
							if not sum(i == 0 for i in t[9*a+b:9*a+b+3]):
								t[9*a+b:9*a+b+3] = [x-1 for x in t[9*a+b:9*a+b+3]]
								shunzi.append(9*a+b)
							else:
								b += 1
				else:
					for a in range(3):
						b = 0
						while b<7:
							if not sum(i == 0 for i in t[9*a+b:9*a+b+3]):
								t[9*a+b:9*a+b+3] = [x-1 for x in t[9*a+b:9*a+b+3]]
								shunzi.append(9*a+b)
							else:
								b += 1
					for j in tiles:
						if t[j] >= 3:
							if t[j] == 3:
								kezi.append(j)
							if t[j] == 4:
								gang.append(j)
							t[j] -= t[j]
				if t==[0]*34:
					ret['shunzi'] = shunzi
					ret['kezi']  = kezi
					ret['gangzi'] = gang
					ret['jiang'] = jiang
					break
	return ret

def cal_fan(a):
	ret = {}
	a.sort()
	o = tilestoint(a)

	if sum(o[-3::])>=8:
		for i in o[-3::]:
			if i == 2 :
				ret["小三元"]=6
	if 1 not in a:
		ret["碰碰胡"]=6

	for i in range(3):
		if 9*i<=a[0] and a[-1] <= 8*(i+1):
			ret['清一色'] = 6
	
	return ret


test1 = [
                
                MAN2,MAN3,MAN4,
				MAN3,MAN4,MAN5,
				MAN4,MAN5,MAN6,
				MAN5,MAN6,MAN7,
				MAN1,MAN1,
]


print(analysis(tilestoint(test1)))



'''
print(cal_fan(tilestoint(test1)))


test3 = []
for i in range(100000):
	random.shuffle(tiles)
	test3.append(tiles[:14])


start = time.process_time()
for i in test3:
	if decode(mahjongcase(tilestoint(i))) in hu:
		print("胡了")

end = time.process_time()


print('Time used: %6.3f' % (end - start))
'''


