
#Code for Cube Function#
def cube(n):
    return n**3
#Code for Factorial#
def factorial(n):
    if n<0:
        return False
    if n==0:
        return 1
    return n*factorial(n-1)
#Pattern Code#
def count_pattern(pattern,tuple,count,start,end):


    last_index=len(tuple)

    while end!=last_index:
        end += 1
        start += 1
        subset = tuple[start:end]
        if pattern == subset:
            count += 1
    return count
#MazeCode

def Move_Left(maze,r,c):

    maze[r][c]=2
    return maze
def Move_Right(maze,r,c):

    maze[r][c]=2

    return maze
def Move_Up(maze,r,c):
    maze[r][c]=2

    return maze
def Move_Down(maze,r,c):

    maze[r][c]=2
    return maze
def solve_maze(maze,r,c,wall):



        choice=input("Enter your choice")
        if choice=='l':
            if c==0 :
                print("wrong choice")
            elif maze[r][c-1]==wall:
                print("It's a WALL")
            else:
                maze[r][c] = 0
                c -= 1
                maze=Move_Left(maze,r,c)
                print(DataFrame(maze))
        if choice=='r':
            if c==6:
                print("wrong choice")
            elif maze[r][c+1]==wall:
                print("ITS A WALL")
            else:
                maze[r][c] = 0
                c += 1
                maze=Move_Right(maze,r,c)
                print(DataFrame(maze))
        if choice == 'u':
                if r == 0:
                    print("wrong choice")
                elif maze[r-1][c] == wall:
                    print("ITS A WALL")
                else:
                    maze[r][c] = 0
                    r -= 1
                    maze = Move_Up(maze, r, c)
                    print(DataFrame(maze))
        if choice == 'd':
            if r == 4:
                print("wrong choice")
            elif maze[r + 1][c] == wall:
                print("ITS A WALL")
            else:
                maze[r][c] = 0
                r += 1
                maze = Move_Down(maze, r, c)
                print(DataFrame(maze))
        if choice=='x':
            return
        if r==4 and c==6:
            print("You won")
            return
        solve_maze(maze,r,c,wall)

#AutoMatic Maze#
def AutoMaze(maze,pos):
    x,y=pos[len(pos)-1]
    if (x==len(maze)-1 and y==len(maze[0])-1):
        return pos
    if (x>=len(maze) or y>=len(maze[0])):

       return []
    if maze[x][y]==1:

        return []
    right=AutoMaze(maze,pos + [(x+1,y)])
    if right!=[]:
        return right

    down=AutoMaze(maze,pos + [(x,y+1)])
    if down!=[]:
        return down
    up = AutoMaze(maze, pos + [x, y - 1])
    if up != []:
        return up
    return []
#Main method#
def main():
    print("PRINTING CUBE PROBLEM")
    print(cube(4))
    print("**********************")
    print("PRINTING FACTORIAL PROBLEM")
    print(factorial(6))
    print("**********************")
    print("PRINTING PATTERN FOR ('a','b') SUBSET")
    pattern = ('a', 'b')
    tuple = ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')
    start = -1
    end = len(pattern) - 1
    print(count_pattern(pattern, tuple, 0, start, end))
    print("**********************")
    print("PRINTING PATTERN FOR ('a','b','a') SUBSET")
    pattern = ('a', 'b','a')
    tuple = ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')
    start = -1
    end = len(pattern) - 1
    print(count_pattern(pattern, tuple, 0, start, end))
    print("**********************")
    maze=[[2 ,0 ,1 ,0 ,0 ,0 ,1],
          [1 ,0 ,1 ,0 ,1 ,0 ,1],
          [1 ,0 ,1 ,0 ,1 ,0 ,1],
          [1 ,0 ,1 ,0 ,1 ,0 ,1],
          [1 ,0 ,0 ,0 ,1 ,0 ,0]]
    print(DataFrame(maze))
    r=0
    c=0
    wall=1
    solve_maze(maze,r,c,wall)
    print("****************************")
#
    # USING THIS MAZE FOR AUTO VERSION BECAUSE I WASN"T
    # ABLE TO IMPLEMENT THE MOVING UP LOGIC,I WILL UPDATE MY CODE IF
    # I COULD FIGURE OUT THAT LOGIC :)#

    maze = [[0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [0, 0, 0, 0]]
    pos = [(0, 0)]
    print(DataFrame(maze))
    print("Printing path")
    print(AutoMaze(maze,pos))
if __name__=="__main__":
    main()

