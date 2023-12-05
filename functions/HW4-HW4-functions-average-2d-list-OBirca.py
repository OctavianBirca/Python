# generate a random 2D list
# print the 2D list
# calculate the average value of the 2D list

from random import randint

# list generator
def random2dList(rows, cols, min, max):
    matrix = []
    for ri in range(rows):
        row = []
        for ci in range(cols):
            row.append (randint(min,max))

        matrix.append(row)
    
    return matrix

def print2dList (matrix):
    print()
    for ri in range(len(matrix)):
        for ci in range(len(matrix[0])):
            print(f" { matrix[ri][ci]:3}", end="")
        
        print()

def average2dList(matrix):
    s = 0
    h = len(matrix)
    w = len(matrix[0])

    for ri in range(h):
        for ci in range (w):
            s += matrix[ri][ci]
    average = s / (h*w)
   
    return average 
        

def minMax2dList(matrix, min, max):
    h = len(matrix)
    w = len(matrix[0])
    min_max_list = [min, max]
    for ri in range(h):
        for ci in range(w):

            if matrix[ri][ci] < min:
                min = matrix[ri][ci]
            if matrix[ri][ci] > max:
                max = matrix[ri][ci]
    
    return min_max_list


            


rows = int(input("Input matrix hight: "))
cols = int(input("Input matrix width: "))
min = int(input("From: "))
max = int(input("To: "))




print (f"Matrix size {rows} x {cols}" )
data = random2dList(rows, cols, min, max)
print2dList(data)

avg = average2dList(data)
print ("Average sum of the matrix: ", avg)

list_min_max = minMax2dList(data, min, max)


minimum = list_min_max[0]
maximum = list_min_max[1]

print("The minimum number in the matrix is:", minimum)
print("The minimum number in the matrix is:", maximum)




