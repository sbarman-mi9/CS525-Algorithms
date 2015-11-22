

class Tsp:
    def __init__(self,filename):
        self.Mylist=[]
        self.Mylist= self.myList(filename)  # The function myList(self) reads the file and put the names of cities and x,y cordinates in two diffrent list eg[[cities],[(x,y)]] 
        self.cities=self.Mylist[0]                  # This is a list containing cities only ie. [cities]
        self.cordinate=self.Mylist[1]           # This list contains cordinates point only 
        self.distance=self.distance()           # This is a list of distance for the entire data. this list contains 50 sublist [[list1],[list2]...........[list50]]



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

    def getcityanddistance(self,n):                     # This methods returns the name of the city and its distance from each city
        return(self.cities[n],self.distance[n])
        

            
t = Tsp('tour48pro.csv')   # To test the function
print(t.Mylist)
print()
print(t.cordinate)
print()
print(t.cities)
print()
print(t.getcityanddistance(2))
print()





    
