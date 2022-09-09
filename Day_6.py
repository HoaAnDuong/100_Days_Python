
maze = []
# num_rows = int(input("Enter the number of rows:"))
# num_cols = int(input("Enter the number of columns:"))
# print("Enter the matrix(o: start/end, .: path, *: wall):")
# for i in range(num_rows):
#     maze.append(input().split(" "))
num_rows = 5
num_cols = 5
maze = [[".", "o", ".", ".", "."], 
        [".", ".", ".", "*", "*"],
        [".", ".", ".", ".", "."],
        ["*", "*", ".", "*", "*"],
        ["o", ".", ".", ".", "."],]
def fillMaze(maze):
    for i in range(num_rows):
        for j in range(num_cols):
            y_pos = i
            x_pos = j
            next_pos = None
            num_next = 1
            while(num_next == 1 and maze[y_pos][x_pos] == "."):
                num_next = 0
                if y_pos > 0:
                    if maze[y_pos-1][x_pos] != "*":
                        next_pos = (y_pos-1,x_pos)
                        num_next += 1    

               
                if  x_pos > 0:
                    if maze[y_pos][x_pos-1] != "*":
                        next_pos = (y_pos,x_pos-1)
                        num_next += 1    
               
                if x_pos < len(maze[0]) - 1:
                    if maze[y_pos][x_pos+1] != "*":
                        next_pos = (y_pos,x_pos+1)
                        num_next += 1    
                
                if y_pos < len(maze) - 1:
                    if maze[y_pos+1][x_pos] != "*":
                        next_pos = (y_pos+1,x_pos)
                        num_next += 1    
                
                if num_next > 1: 
                    break
                else:   
                    maze[y_pos][x_pos] = "*"
                    if num_next == 1:
                        print(next_pos)
                        y_pos = next_pos[0]
                        x_pos = next_pos[1]
                    else: 
                        break

fillMaze(maze)
for r in maze:
    print(r)

