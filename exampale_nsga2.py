import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Мат фунция
def f1(a, b):
    c = math.exp(math.sin(math.cos(a + b) - b)) ** (a - b)
    axis_z.append(c)
    axis_x.append(a)
    axis_y.append(b)
    return c

# Function to sort by values
def sort_by_values(list1, values):
    sorted_list = []
    while(len(sorted_list)!=len(list1)):
        if index_of(min(values),values) in list1:
            sorted_list.append(index_of(min(values),values))
        values[index_of(min(values),values)] = math.inf
    return sorted_list

def index_of(a,list):
    for i in range(0,len(list)):
        if list[i] == a:
            return i
    return -1

#Function to carry out NSGA-II's fast non dominated sort
def fast_non_dominated_sort(values1):
    S=[[] for i in range(0,len(values1))]
    front = [[]]
    n=[0 for i in range(0,len(values1))]
    rank = [0 for i in range(0, len(values1))]

    for p in range(0,len(values1)):
        S[p]=[]
        n[p]=0
        for q in range(0, len(values1)):
            if (values1[p] > values1[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif(values1[q] > values1[p]):
                n[p] = n[p] + 1
        if n[p]==0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)
    i = 0
    while(front[i] != []):
        Q=[]
        for p in front[i]:
            for q in S[p]:
                n[q] =n[q] - 1
                if( n[q]==0):
                    rank[q]=i+1
                    if q not in Q:
                        Q.append(q)
        i = i+1
        front.append(Q)
    del front[len(front)-1]
    return front

#Function to calculate crowding distance
def crowding_distance(values1, front):
    print(values1, front)
    distance = [0 for i in range(0,len(front))]
    sorted1 = sort_by_values(front, values1[:])
    # sorted2 = sort_by_values(front, values2[:])
    distance[0] = 4444444444444444
    distance[len(front) - 1] = 4444444444444444
    for k in range(1,len(front)-1):
        distance[k] = distance[k]+ (values1[sorted1[k+1]])/(max(values1)-min(values1))
    # for k in range(1,len(front)-1):
    #     distance[k] = distance[k]+ (values1[sorted2[k+1]] - values2[sorted2[k-1]])/(max(values2)-min(values2))
    return distance

#Function to carry out the crossover
def crossover(a,b):
    r=random.random()
    if r>0.5:
        return mutation((a+b)/2)
    else:
        return mutation((a-b)/2)

#Function to carry out the mutation operator
def mutation(solution):
    mutation_prob = random.random()
    if mutation_prob <1:
        solution = min_x+(max_x-min_x)*random.random()
    return solution

#Main program starts here
pop_size = 20
max_gen = 100

#Initialization
min_x=0
max_x=20

min_y = 0
max_y = 20
solution_x=[min_x+(max_x-min_x)*random.random() for i in range(0,pop_size)]
solution_y=[min_y+(max_y-min_y)*random.random() for i in range(0,pop_size)]
gen_no=0

axis_z = []
axis_x = []
axis_y = []
while(gen_no<max_gen):
    function1_values = [f1(solution_x[i], solution_y[i])for i in range(0,pop_size)]
    non_dominated_sorted_solution = fast_non_dominated_sort(function1_values[:])
    crowding_distance_values=[]
    for i in range(0,len(non_dominated_sorted_solution)):
        crowding_distance_values.append(crowding_distance(function1_values[:],non_dominated_sorted_solution[i][:]))
    break
    solution_x2 = solution_x[:]
    solution_y2 = solution_y[:]
    #Generating offsprings
    while(len(solution_x2)!=2*pop_size):
        a1 = random.randint(0,pop_size-1)
        b1 = random.randint(0,pop_size-1)
        solution_x2.append(crossover(solution_x[a1],solution_x[b1]))

        a1 = random.randint(0, pop_size - 1)
        b1 = random.randint(0, pop_size - 1)
        solution_y2.append(crossover(solution_y[a1], solution_y[b1]))

    function1_values2 = [f1(solution_x2[i], solution_y2[i])for i in range(0,2*pop_size)]
    non_dominated_sorted_solution2 = fast_non_dominated_sort(function1_values2[:])
    crowding_distance_values2=[]
    for i in range(0,len(non_dominated_sorted_solution2)):
        crowding_distance_values2.append(crowding_distance(function1_values2[:], non_dominated_sorted_solution2[i]))
    new_solution= []
    for i in range(0,len(non_dominated_sorted_solution2)):
        non_dominated_sorted_solution2_1 = [index_of(non_dominated_sorted_solution2[i][j],non_dominated_sorted_solution2[i] ) for j in range(0,len(non_dominated_sorted_solution2[i]))]
        front22 = sort_by_values(non_dominated_sorted_solution2_1[:], crowding_distance_values2[i][:])
        front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(0,len(non_dominated_sorted_solution2[i]))]
        front.reverse()
        for value in front:
            new_solution.append(value)
            if(len(new_solution)==pop_size):
                break
        if (len(new_solution) == pop_size):
            break
    solution_x = [solution_x2[i] for i in new_solution]
    solution_y = [solution_y2[i] for i in new_solution]
    gen_no = gen_no + 1

function1 = [i * -1 for i in function1_values]
ax = plt.axes(projection='3d')
ax.scatter3D(axis_x, axis_y, axis_z, cmap='Greens')
plt.show()


plt.scatter(axis_x, axis_z)
plt.show()
