import pandas as pd

obj = pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
print(obj.index)
obj1 = pd.Series([4,7,-5,3],index=['a','b','c','d'])
print(obj1)
print(obj1.index)
print(obj1['a'])

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 =pd.Series(sdata,index=states)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())
print(obj3 + obj4)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print(frame)
