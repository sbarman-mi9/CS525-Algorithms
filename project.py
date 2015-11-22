

class Tsp:
    def __init__(self,filename):
        self.Mylist=[]
        self.Mylist= self.myList(filename)
        self.cities=self.Mylist[0]
        self.cordinate=self.Mylist[1]
        self.distance=self.distance()



    def myList(self,filename):
        f = open(filename)
        cities=[]
 
        cordxy=[]
        for line in f:
            alist = line.split(';') 
            for i in range(0,len(alist)):
                alist[i] = alist[i].rstrip('\n')
                alist[i]=alist[i].rstrip(',')
            cities.append(alist[0])
            x=int(alist[1])
            y=int(alist[2])
            cordxy.append( (x,y) )
        self.Mylist.extend([cities,cordxy])
        f.close()
        return(self.Mylist)

    def distance(self):
        dis=[]
        size=len(self.cordinate)
        for cd in range(0,size):
            deem=[]
            for uu in range(0,size):
                me=(self.cordinate[cd][0]-self.cordinate[uu][0])**2+(self.cordinate[cd][1]-self.cordinate[uu][1])**2
                me=(me)**0.5
                deem.append(me*56.9)
            dis.append(deem)
        return(dis)

    def getcityanddistance(self,n):
        return(self.cities[n],self.distance[n])
        

            
t = Tsp('tour48pro.csv')

print(t.getcityanddistance(2))



    
