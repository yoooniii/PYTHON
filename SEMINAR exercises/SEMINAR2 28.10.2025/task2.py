#zad2

s=1
i=0
for y in range(7,70):
    if y%3==0: 
        i+=1; 
        s=(s+y)/i
print("Средноаритметичното на числата е:",s)
