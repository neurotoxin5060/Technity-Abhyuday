n=int(input('no_of_commands\n'))
comms=[]
count=0
for i in range(n):
    temp=input('enter command\n')
    comms.append(temp)
# print(comms)
for i in comms:
    if i =='++x' or i=='x++':
        count=count+1
    elif i=='--x' or i=='x--':
        count=count-1
print(count)
        
