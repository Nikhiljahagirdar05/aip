
start=[1,2,3,4,0,6,7,5,8]
goal=[1,2,3,4,5,6,7,8,0]

def heuristic(state):
    h=0
    for i in range(9):
        if state[i]!=0:
            j=goal.index(state[i])
            h+= abs(i//3 - j//3) + abs(i%3 - j%3)
    return h

open_list=[(start,0)]
visited=set()

while open_list:

    open_list.sort(key=lambda x:x[1] + heuristic(x[0]))

    state,g = open_list.pop(0)

    if state==goal:
        print("Goal Reached...")
        print("Total Moves",g)
        break

    if tuple(state) in visited:
        continue

    visited.add(tuple(state))

    zero = state.index(0)
    x,y  = zero//3, zero%3

    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny = x+dx, y+dy

        if 0 <= nx < 3 and 0 <= ny <  3:
            new=state.copy()
            pos=nx*3 + ny

            new[zero],new[pos]=new[pos],new[zero]

            if tuple(new) not in visited:
                open_list.append((new,g+1))
else:
    print("No solution found....")