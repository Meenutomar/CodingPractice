data = [
    {'id':1,
     "name":'mee'
     },
     {
         "id":2,
         "name":'poo'
         },
         {
             "id":3,
             "name":'sinhaG'
             }]
dictt = {}

for i in data:
    dictt.setdefault(i.get('id'), i)


print("Map::", dictt)
          
          




#dictt = {data[i]:data[i + 1]  for i in range(0,len(data))}
#print(dictt)
#print(type(dictt))

def sayHello():
    print("Hello, World!", len(data))

sayHello()