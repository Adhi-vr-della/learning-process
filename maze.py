maze = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,1],
    [1,1,1,1]

]

n= len(maze)



def safe(maze ,x,y,n):
    return 0 <= x < n and 0 <= y < n   and maze[x][y] == 1

def solve(maze ,x,y,n,sol):
    if x == n-1 and y == n-1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
    if safe(maze,x,y,n):
        sol[x][y] = 1




        if solve(maze,x,y+1,n,sol):              #for move right
            return True
        if solve(maze,x+1,y,n,sol):              #for move down
            return True

        if solve(maze,x-1,y,n,sol):              #for move up
            return True
        if solve(maze,x,y-1,n,sol):              #for move left
            return True

        sol[x][y] = 0
        return False

    return False


sol = [[0]*n for _ in range(n)]

if solve(maze,0,0,n,sol):
    print('solution found:')
    for row in sol:
        print(row)
else:
    print('No solution')

