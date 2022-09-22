#ИЗ1
def task(fname):
    with open(fname,"r") as fi:
 
        tmp=[]
        prev=int(fi.readline())
 
        while True:
            
            line=fi.readline()
            
            if len(line) <= 1:
                break
 
            curr=int(line)
            
            s=curr+prev
            p=curr*prev
            
            if s%2==1 and p%13==0:
                tmp.append(s)
            
            prev=curr
        
    if len(tmp)==0:
        return (None,None)
    else:    
        return (len(tmp),max(tmp))
        
k,s=task("C:/Users/Артём/source/repos/Jakepps/Python/2a.txt")  
k1,s=task("C:/Users/Артём/source/repos/Jakepps/Python/2b.txt")      
print("Количество пар в 2a=",k)
print("Количество пар в 2b=",k1)

