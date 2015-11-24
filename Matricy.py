__author__ = 'student'
class Matrix:
    def __init__(self,m,n=None):
        A=[]
        self.m=m
        self.n=n
        for x in range(m):
            A.append([])
            for y in range(n):
                A[x].append(0)
        self.A=A
    def __add__(self, other):
        C=self.A
        J=self.A
        K=other.A
        if self.m==other.m and self.n==other.n:
            for x in range(self.m):
                for y in range(self.n):
                    C[x][y]=J[x][y]+K[x][y]
        self.C=C
        return self.C
    def determinant(self):
        if self.n==self.m:
            if self.n==2:
                self.det=self.C[0][0]*self.C[1][1]-self.C[0][1]*self.C[1][0]
            if self.n==3:
                self.det=self.C[0][0]*(self.C[1][1]*self.C[2][2]-self.C[1][2]*self.C[2][1])-self.C[0][1]*(self.C[1][0]*self.C[2][2]-self.C[1][2]*self.C[2][0])+self.C[0][2]*(self.C[1][0]*self.C[2][1]-self.C[1][1]*self.C[2][0])
        if self.n!=self.m or self.n>3:
            raise Exception()
            print('Ne mogu!')
    def __eq__(self,other):
        t=0
        if self.m==other.m and self.n==other.n:
            t=1
            for x in range(self.m):
                for y in range(self.n):
                    if self.A[x][y]!=other.A[x][y]:
                        t=0
                        break
        if t==0:
            return False
        else:
            return True
    def get(self,i,j):
        return self.A[i][j]
    def get_m(self):
        return self.m
    def get_n(self):
        return self.n
    def get_size(self):
        return self.m,self.n
    def __mul__(self,other):
        if type(other)==float or type(other)==int:
            for x in range(self.n):
                for y in range(self.m):
                    self.A[x][y]=self.A[x][y]*other
    #Umnozhenie FIXME!
    def set(self,i,j,value):
        self.A[i][j]=value
    def __sub__(self, other):
        P=self.A
        B=self.A
        U=other.A
        if self.m==other.m and self.n==other.n:
            for x in range(self.m):
                for y in range(self.n):
                    P[x][y]=B[x][y]-U[x][y]
        self.P=P
        return self.P
    def transpose(self):
        H=[]
        for x in range(self.n):
            H.append([])
            for y in range(self.m):
                H[self.n].append(self.A[x][y])
        self.H=H
        return H
    def __truediv__(self,other):
        for x in range(self.m):
            for y in range(self.n):
                self.A[x][y]=self.A[x][y]/other
        return self.A
