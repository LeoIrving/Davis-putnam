from copy import deepcopy

class Atom:
    def __init__(self,index,name) -> None:
        self.index = index
        self.name=name
        self.binding=None

# input
clause_set = []
atom_list = []
with open("cnf.txt") as f:
    while True:
        info = f.readline()
        if info == "0\n":
            break
        clause =info.rstrip("\n").split(" ")
        clause = [int(i) for i in clause]
        clause_set.append(clause)
    for line in f:
        info = line.rstrip("\n").split(" ")
        atom_list.append(Atom(int(info[0]),info[1]))

# recursive davis-putnam algorithm
def dpll(cs,b):
    while True:
        if not cs:
            return b
        for item in cs:
            if not item:
                return -1
        if easyCaseIn(cs,b):
            cs,b=easyCase(cs,b)
        else:
            break
    cs_copy = deepcopy(cs)
    b_copy = deepcopy(b)
    p = None
    for item in b_copy:
        if item.binding == None:
            p = item.index
            break
    cs_copy,b_copy = propagate(cs_copy,b_copy,p,True)
    answer = dpll(cs_copy,b_copy)
    if answer != -1:
        return answer
    cs,b = propagate(cs,b,p,False)
    return dpll(cs,b)

# easy case identifier
def easyCaseIn(cs,b):
    # singleton clasue
    for item in cs:
        if len(item) == 1:
            return True
    # pure literal
    pure_literal = False
    for item in b:
        if item.binding == None:
            atom1 = item.index
            atom2 = -1*item.index
            repeat_atom1 = 0
            repeat_atom2 = 0
            for i in cs:
                for ii in i:
                    if ii == atom1:
                        repeat_atom1 = 1
                    elif ii == atom2:
                        repeat_atom2 = 1
            if (repeat_atom1 == 1 and repeat_atom2 == 0) or (repeat_atom1 == 0 and repeat_atom2 == 1):
                pure_literal = True
    return pure_literal

# dealing with easy case
def easyCase(cs,b):
    p = 0
    # singleton clause
    for item in cs:
            if len(item) == 1:
                p = item[0]
                break
    # pure literal
    if p == 0:
        flat_list = []
        all_count = {}
        abs_all_count = {}
        for item in cs:
            flat_list.extend(item)
        for item in flat_list:
            abs_item = abs(item)
            count = all_count.get(item, 0)
            all_count[item] = count + 1
            count = abs_all_count.get(abs_item, 0)
            abs_all_count[abs_item] = count + 1

        for item in set(flat_list):
            abs_item = abs(item)
            if all_count[item] == abs_all_count[abs_item]:
                p = item
                break
    if p > 0:
        return propagate(cs,b,p,True)
    else:
        return propagate(cs,b,p,False)

# propagate a atom
def propagate(cs,b,p,state):
    if state == False:
        b[abs(p)-1].binding = "F"
    else:
        b[abs(p)-1].binding = "T"
    if (p>0 and state==False) or (p<0 and state==True) :
        p = -1*p
    cs = list(filter(lambda x:p not in x, cs))
    p_neg = -1*p
    for index in range(len(cs)):
        cs[index] = list(filter(lambda x:p_neg != x, cs[index]))
    return cs,b

# output
with open("result.txt","w") as f:   
    answer = dpll(clause_set,atom_list)
    if answer == -1:
        f.write("0\n")
    else:
        for item in answer:
            output = str(item.index)+" "+ (item.binding or "T")
            f.write(output)
            f.write("\n")
        f.write("0\n")
        for item in answer:
            output = str(item.index)+" "+item.name
            f.write(output)
            f.write("\n")

