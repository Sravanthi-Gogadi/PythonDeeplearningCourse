# declare list 1
python_list = ['Bhargavi', 'Sravanthi', 'Keerthi', 'Deepthi']
# delare list 2
webApplication_list = ['Bhargavi', 'Sravanthi', 'Preethi', 'Sruthi']
# list for common students
common= []
# list for uncommon students
uncommon= []
python_set = set(python_list) #taking python list as a set
webApplication_set = set(webApplication_list) #taking webApplication list as a set
common.extend(list(python_set & webApplication_set)) #taking the intersection of the sets
uncommon.extend(list(python_set - webApplication_set)) #taking the difference of the sets(both sides)
uncommon.extend(list(webApplication_set - python_set))
# print results
print("Students enrolled in Python", python_set)
print("Students enrolled in Web application", webApplication_set)
print("Common students: ", common)
print("Uncommon students: ",uncommon)


