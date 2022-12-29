my_mat=[[1,2,3],[4,5,6],[7,8,9]]
inputtar=input("row and col")
row = int(inputtar[0])
col = int(inputtar[1])
my_mat[row-1][col-1]="X"
print(my_mat)