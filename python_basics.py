x=[3,2]
print(x)
age = 28
print(age)
print(type(age))
x="mystring"
print(x)
s=str(3.2)
print(s)
mytuple = (3,4)
print(mytuple)
mylist = [1,"2", mytuple]
print(mylist)
y = "My name is Rose and my age is"
d = 21
print(y), print(d)
z = "supercalifragilisticexpialidocious"
print(z)
print(len(z))
print(type(z))
ad = "This is an ex-parrot"
print(ad.split())
s1 = 1+3
s2 = 2+2
print(s1 * s2)
name = "sara"
age = 23
print(f"My name is {name} and my age is {age}")
a =34
b = 3
c =67
e = 43
print(a>b or c<d)
print(a>b and c<d)
x = 1
if x == 1:
    print(x)
print('rose')
print("rose")
print('rose "laptop"')
print('rose\'s "laptop"')
print ('rose ' + 'rose')
print(r'c:\docs\navin')
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
x = 9
print(x + 10)
name = "youtube"
print(name)
print(name + 'rocks')
print((name) + 'rocks')
print(name[0])
print(name[-1])
print(name[0:2])
print(name[1:])
print(name[3:10])
hello = "hello"
world ="world"
helloworld = hello +" " + world
print(helloworld)
print('my' + helloworld[5:])
one = 1
two = 2
hello = "hello"
print(f"{one} {two} {hello}")
print(str(one) + str(two)+ hello)
nums = [25,13,42,54]
print(nums)
print(nums[2])
print(nums[-1])
print(nums[2:])
names =['rose','anu','dia']
print(names)
values = [9.5,'rose',24]
mil = [nums, names]
print(mil)
nums.append(67)
print(nums)
nums.insert(2,77)
print(nums)
nums.remove(42)
print(nums)
nums.pop(3)
print(nums)
nums.pop()
print(nums)
nums.insert(3,56)
print(nums)
del nums[2:]
print(nums)
nums.extend([29,21,89])
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)
tup = (21,36,14,25)
print(tup)
s = {22,25,14,21,5}
print(s)
data = {1:'rose', 2:'maria',3:'jose'}
print(data)
print(data[3])
print(data.get(2))
print(data.get(1,'not found'))
print(data.get(4,'not found'))
keys = ['navin','kiran','harsh']
values = ['python','java','js']
print(values[1])
data = dict(zip(keys,values))
print(data)
data['Monica'] = 'cs'
print(data)
del data['harsh']
print(data)
prog = { 
    'js':'atom', 
    'cs':'vs', 
    'python':['pycharm','sublime'],
    'java':{
    'jse': 'netbeans',
    'jee': 'eclipse'
    }
}
print(prog['js'])
print(prog['python'])
print(prog['python'][1])
print(prog['java'])
print(prog['java']['jee'])

