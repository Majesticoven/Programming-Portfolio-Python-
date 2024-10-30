def spiral_matrix(size):
    top,bottom =0,size
    left,right = 0,size
    current_num = 0
    spiral_matrix = [[0]*size for i in range(size)]
    
    while top < bottom and left<right:
        for i in range(left,right):
            current_num +=1
            spiral_matrix[top][i] = current_num
    
        top +=1
        
        for i in range(top,bottom):
            current_num +=1
            spiral_matrix[i][right-1] = current_num

        right -=1
        
        for i in range(right-1,left-1,-1):
            current_num +=1
            spiral_matrix[bottom-1][i] = current_num
        bottom -=1

        for i in range(bottom-1,top-1,-1):
            current_num +=1
            spiral_matrix[i][left] = current_num
        left +=1

    return spiral_matrix        
size = 4

matrix = spiral_matrix(size)
for row in matrix:
    print(row)