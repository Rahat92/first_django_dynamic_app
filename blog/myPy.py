name = [
  {
    'name':'kamrul',
    'age':23
  },
  {
    'name':'Hasan',
    'age':20
  }
]

def age(a):
  return a['age']

name.sort(reverse= True,key=age)
print(name)
