#Create a Pretty Table object and save it to a variable called table

from prettytable import PrettyTable
table=PrettyTable()

#crete a 2 column Table with 3-4 entries

table.add_column("Pokemon Name",['Pikachu','Squirtle','Bulbasaur','Charmander'])
table.add_column("Type",['Electric','Water','Grass',""])

#Add alignment to table

table.align='l'


print(table)