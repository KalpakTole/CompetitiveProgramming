import random
name = "f"

f = open(name + ".txt")
lines = []
for line in f:
    lines.append(line[:-1].split(" "))
f.close()

"""
D : the duration of the simulation, in seconds,
I : the number of intersections 
S : the number of streets,
V : the number of cars,
F : the bonus points for each car that reaches
"""

D, I, S, V, F = [int(x) for x in lines[0]]
street_info = {} #name : (start, end, time)
income_and_street = {}

for i in range(S):
    S_info = lines[i+1]
    B = int(S_info[0])  # Start Street
    E = int(S_info[1])  # End Street
    street_name = S_info[2]
    L = int(S_info[3])  # Time on that street from start to end
    street_info[street_name] = (B, E, L)
    income_and_street[E] = []

for k,v in street_info.items():
    income_and_street[v[1]].append(k)

cars_path = {}
for i in range(V):
    V_info = lines[i + S + 1]
    P = int(V_info[0])
    path = V_info[1:]


f = open(name + "_kalpak_submission.txt", "w")
f.write(str(len(income_and_street.keys())) + "\n")
for k, v in income_and_street.items():
    f.write(str(k) + "\n")
    f.write(str(len(v)) + "\n")
    for v1 in v:
        f.write(v1 + " " + str(random.randint(1,len(v))) + "\n")

f.close()
