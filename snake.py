class snake_game:
    def __init__(self,row,col):
        self.row=row
        self.col=col 
        self.l=[]
        self.l1=[]
        for i in range(0,self.row):
            for i in range(0,self.col):
                self.l1=list('#'*self.col)
                self.l.append(self.l1)

    def display_board(self):
        k=0
        for i in range(0,self.row):
            print("\t\t\t",end="")
            for j in range(0,self.col):
                print(self.l[i][j],end=" ")
                k+=1
            print("\n") 


r,c=map(int,input("Enter the row and column size of the board: ").split())
s=snake_game(r,c) 
s.display_board()  
