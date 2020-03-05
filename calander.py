year = int(input("Enter Year\n"))
p=0
leap=0
c=year-1600
if(year%100==0):
  if(year%400==0):
    leap==1
else:
  if(year%4==0):
    leap=1
  
for i in range(1,c+1):
  if((i-1)%4==0):
    if((i-1)%100==0):
      if((i-1)%400==0):
        p+=2
      else:
        p+=1
    else:
      p+=2
  else:
    p+=1
t=0
month = ["JANURARY","FEBURARY",'MARCH',"APRIL","MAY","JUNE","JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
for k in range(12):
  print("\n________________________________________")
  print("\n          ",month[k],year,end="     \n")
  print("________________________________________")
  day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
  m=t
  t=0
  
  for i in range(7):
     print(day[i],end="   ")
  print("\n")
  if(m==0):
    if((6+p)%7==0):
     for j in range(6):
      print(end="      ")
      t+=1
    else:
     for j in range(((6+p)%7)-1):
      print(end="      ")
      t+=1
   
  else:
   if(m%7==0):
    for z in range(6):
      print(end="      ")
      t+=1
   else:
    for z in range(((m%7)-1)):
      print(end="      ")
      t+=1
  t+=1
  if(k+1==1 or k+1==3 or k+1==5 or k+1==7 or k+1==8 or k+1==10 or k+1==12):      
   for l in range(1,32):
     if(l<10):
        print(l,end="     ")
     else:
        print(l,end="    ")
     if(t%7==0 and t!=0):
        print("\n")
     t+=1
  elif(k+1==2 and leap==1):
   for l in range(1,30):
     if(l<10):
        print(l,end="     ")
     else:
        print(l,end="    ")
     if(t%7==0 and t!=0):
        print("\n")
     t+=1
  elif(k+1==2 and leap==0):
   for l in range(1,29):
     if(l<10):
        print(l,end="     ")
     else:
        print(l,end="    ")
     if(t%7==0 and t!=0):
        print("\n")
     t+=1
  else:
   for l in range(1,31):
     
     if(l<10):
        print(l,end="     ")
     else:
        print(l,end="    ")
     if(t%7==0 and t!=0):
        print("\n")
     t+=1

 
