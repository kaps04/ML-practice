import men_profile
import random 
import time

names =["John","Corey","Adam","Steve","Rick","Thomas"]
majors =["Math", "Enginnering","CompiSci","Arts","Business"]

print("memory(Before):{Mb}".format(men_profile.memory_usage_resource()))

def people_list(num_people):
  result=[]
  for i in range(num_people):
    person={
      "id":i,
      "name":random.choice(names),
      "major":random.choice(majors)
    }
    result.append(person)
  return result

def people_generator(num_people):
  for i in xrange(num_people):
      person = {  "id":i,
      "name":random.choice(names),
      "major":random.choice(majors)
        
      }
      yield person
t1=time.clock()
people = people_list(100000)
t2 = time.clock()  
# t1=time.clock()
# people = people_list(100000)
# t2 = time.clock()  

print("Memory (After) :{}Mb".format(men_profile.memory_usage_resource()))
print("Took {} Seconds".format(t2-t1))


  

























def square_numbers(nums):
  for i in nums:
    yield (i*i)

my_nums=square_numbers([1,2,3,4,5])


for num in my_nums:
  print (num)   
  #print(list(my_nums))
  
print(my_nums)
