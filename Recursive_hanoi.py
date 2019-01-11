def TowerofHanoi(n,a,b,c):
  if(n==1) :
    print(str(a)+" "+str(b))
    return
  
  TowerofHanoi(n-1,a,c,b)
  print(str(a)+" "+str(b))

  TowerofHanoi(n-1,c,b,a)

n = int(input("넣어라"))

a=1
b=2
c=3;
TowerofHanoi(n, a, b, c)
