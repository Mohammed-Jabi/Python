List = [10,9,30]
print(List)
List.append("Append")
print(List)
List.reverse()
print(List)
List.remove("Append")
List.sort()
print(List)

Tuple = (10,20,30,40,70,50,40)
print("The tuple is: ",Tuple)
print(Tuple.count(40))


Set = {30,40,0, "Jabir", 20,0}
print(Set)
Set.add("Mohammed")
print(Set)
Set.remove(0)
print(Set)
Set.clear()
print(Set)

dictionary = {"Jabir":"SDET","Izhaar":"FrontEnd Developer", "Hafsa":"BPO", "Anjeeth":"SDE", "Iqra":"Intern"}
print(dictionary)
dictionary.pop("Hafsa")
print(dictionary)

lst = [20.30,10,100]
lst1 = [20,30,10,100]
print(lst is lst1)