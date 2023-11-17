from collections import deque
def g_solution(start_state,goal_state):
    def g_neighbor(state):
        e_spot=state.index(0)
        nei=[]
        for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            nx=e_spot%3+dx
            ny=e_spot//3+dy
            if ((0<=nx<3)and(0<=ny<3)):
                new_state=list(state)
                
                new_state[e_spot],new_state[ny*3+nx]=new_state[ny*3+nx], new_state[e_spot]
                nei.append(tuple(new_state))
        return nei
    visited=set()
    queue = deque([(start_state, [])])
    while queue:
        c_state,path=queue.popleft()
        if c_state==goal_state:
            return path+[c_state]
        if c_state not in visited:
            visited.add(c_state)
            for n in g_neighbor(c_state):
                queue.append((n,path+[c_state]))
    return None
#main module
start=(1,2,3,0,4,6,7,5,8)
goal=(1,2,3,4,5,6,7,8,0)
sol=g_solution(start,goal)
if sol:
    for step, state in enumerate(sol):
        print(f"Step {step + 1}:")
        for i in range(3):
            print(state[i * 3:i * 3 + 3])
        print()
else:
    print("No solution found.")
