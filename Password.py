#generate password
import random
a=random.randint(0,9)
b=random.randint(0,9)
c=random.choice(['A','B','C','D','E','Q','W','R','T','Y','U','I','O','P','S','F','G','H','J','K','L','Z','X','V','N','M'])
d=random.choice(['A','B','C','D','E','Q','W','R','T','Y','U','I','O','P','S','F','G','H','J','K','L','Z','X','V','N','M'])
f=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
g=random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
print ('Password=',a,b,c,d,f,g)
