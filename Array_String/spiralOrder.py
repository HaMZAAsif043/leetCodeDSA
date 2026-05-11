# def spiralOrder(matrix):
#     ret =[]
#     while matrix:
#         # Insertaion of the First row as it is 
#         ret += matrix.pop(0)

#         #Insertion of the last elements of the rows
#         if matrix and matrix[0]:
#             for row in matrix:
#                 ret.append(row.pop())

#         # reverse of the last row 
#         if matrix:
#             ret+=(matrix.pop()[::-1])

#         # append all the remaining rows first element 
#         if matrix  and matrix[0]:

#             for row in matrix[::-1]:
#                 ret.append(row.pop(0))
#     return ret

def spiralOrder(matrix):
    ret=[]
    while matrix:
        if matrix:
            ret+= matrix.pop(0)
        
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        
        if matrix:
            ret+= matrix.pop()[::-1]
            
    
        if matrix:
            for row in matrix[::-1]:
                ret.append(row.pop(0))

    return ret

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
print(spiralOrder(matrix))