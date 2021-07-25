import pandas as pd

employee = {'number':[1,2,3,4], 'name':["addy","john","lina","mark"],'salary':[15,20,30,40]}
#creating dataframes
table1 = pd.DataFrame(employee)
print(table1)
#####################################################################################
employee1 = {'number':[1,2,3,4,5], 'name':["addy","john","lina","mark","harry"],'salary':[15,20,30,40,10]}

table = pd.DataFrame(employee)
#slicing the dataframe
print(table1.head(3))       # starts from upside
print(table1.tail(2))       # starts from downside
#####################################################################################
food = {'number':[1,2,3], 'name':["burger","pizza","hotdog"],'price':[150,200,300]}
bevarage = {'number':[1,2,3], 'name':["coke","pepsi","coffee"],'price':[50,100,250]}

table1 = pd.DataFrame(food)
table2 = pd.DataFrame(bevarage)
# merging two tables
fusion = pd.merge(table1,table2)
print(fusion)
#####################################################################################
food1 = {'number':[1,2,3], 'name':["burger","pizza","hotdog"],'price':[150,200,300]}
bevarage1 = {'index':[1,2,3],'drink':["coke","pepsi","coffee"],'amount':[50,100,250]}

tab1 = pd.DataFrame(food)
tab2 = pd.DataFrame(bevarage)
# joining two tables
joini = tab1.join(tab2)
print(joini)
#####################################################################################
csv_file = pd.read_csv("Data_Set.csv")
# converting csv file to html
csv_file.to_html("new_file")
