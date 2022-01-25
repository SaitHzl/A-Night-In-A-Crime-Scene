handle = open('crime_scene.txt','r')
line_list = []
word_list = []
for line in handle:
    line_list.append(line)
for i in range(len(line_list)):
    if line_list[i].split() != []:
        word_list.append(line_list[i].split())
print(word_list)
weight = int(word_list[0][0])
time = int(word_list[0][1])
N = int(word_list[1][0])

evidence_dict = {}
id_list = []

def evidence(n,i):
    if n == i:
        return
    id = int(word_list[i][0])
    w = int(word_list[i][1])
    t = int(word_list[i][2])
    v = int(word_list[i][3])
    id_list.append(id)
    evidence_dict[id] = {'w':w , 't':t , 'v':v}
    evidence(n,i+1)
    return
evidence(N+2,2)

sublists = []
def sublist(lst,i,subl):
    if i == 0:
        temp = subl.copy()
        sublists.append(temp)
        return
    subl.append(lst[0])
    sublist(lst[1:],i-1,subl)
    subl.pop()
    sublist(lst[1:],i-1,subl)

sublist(id_list,len(id_list),[])

def sum_w(lst,i,weight_sum):
    if i == len(lst):
        return weight_sum
    weight_sum += evidence_dict[lst[i]]['w']
    return sum_w(lst,i+1,weight_sum)
def sum_t(lst,i,time_sum):
    if i == len(lst):
        return time_sum
    time_sum += evidence_dict[lst[i]]['t']
    return sum_t(lst,i+1,time_sum)
def sum_v(lst,i,value_sum):
    if i == len(lst):
        return value_sum
    value_sum += evidence_dict[lst[i]]['v']
    return sum_v(lst,i+1,value_sum)

v1=0
choosen_lst1 = []
def choose1(lst,i):
    global v1
    global choosen_lst1
    if i == len(lst):
        return
    if sum_v(lst[i],0,0) > v1 and sum_w(lst[i],0,0) <= weight:
        v1 = sum_v(lst[i],0,0)
        choosen_lst1 = lst[i]
    choose1(lst,i+1)
    return

v2=0
choosen_lst2 = []
def choose2(lst,i):
    global v2
    global choosen_lst2
    if i == len(lst):
        return
    if sum_v(lst[i],0,0) > v2 and sum_t(lst[i],0,0) <= time:
        v2 = sum_v(lst[i],0,0)
        choosen_lst2 = lst[i]
    choose2(lst,i+1)
    return


v3=0
choosen_lst3 = []
def choose3(lst,i):
    global v3
    global choosen_lst3
    if i == len(lst):
        return
    if sum_v(lst[i],0,0) > v3 and sum_w(lst[i],0,0) <= weight and sum_t(lst[i],0,0) <= time:
        v3 = sum_v(lst[i],0,0)
        choosen_lst3 = lst[i]
    choose3(lst,i+1)
    return

choose1(sublists,0)
choose2(sublists,0)
choose3(sublists,0)

def sorter(lst,i,j):
    if i == len(lst):
        return lst
    if j == len(lst):
        sorter(lst,i+1,0)
        return lst
    if lst[i] < lst[j]:
        lst[i],lst[j] = lst[j],lst[i]
    sorter(lst,i,j+1)
    return lst

f = open('solution_part1.txt','w')
f.write(str(v1)+'\n')
for el in sorter(choosen_lst1,0,0):
    f.write(str(el)+' ')
f.close()

f = open('solution_part2.txt','w')
f.write(str(v2)+'\n')
for el in sorter(choosen_lst2,0,0):
    f.write(str(el)+' ')
f.close()

f = open('solution_part3.txt','w')
f.write(str(v3)+'\n')
for el in sorter(choosen_lst3,0,0):
    f.write(str(el)+' ')
f.close()

