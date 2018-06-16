"""
Consider the following scenario. You have a list of students who are attending class "Python"

and another list of students who are attending class "Web Application".Find the list of students who are attending both the classes.

Also find the list of students who are not common in both the classes. Print the both lists.

"""
python_list = ['Bhargavi', 'Sravanthi', 'Keerthi', 'Deepthi']
webApplication_list = ['Bhargavi', 'Sravanthi', 'Preethi', 'Sruthi']
common= []
uncommon= []
python_set = set(python_list)
webApplication_set = set(webApplication_list)
common.extend(list(python_set & webApplication_set))
uncommon.extend(list(python_set - webApplication_set))
uncommon.extend(list(webApplication_set - python_set))
print(common)
print(uncommon)