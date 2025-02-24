def sort(lt):
 l=lt
 i=0

 #finds minimum and maximum
 check=[l[0],l[0]]
 for i in l:
  if check[0]>i:
   check[0]=i
  if check[1]<i:
   check[1]=i
 
 #sorts list
 for i in range(check[0],(check[1]+1)):
  for o in range(lt.count(i)):
     l.remove(i)
     l.append(i)
 
 return l