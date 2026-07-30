#1.Types of List
#Change
subjects = ["English", "Math", "Physics", "Computer"]
#Change Physics to Chemistry.
subjects[2]="chemistry"
print(subjects)

#Adding Items (append)

language=["Python", "Java"]
language.append("C++")
print(language)

#insert()
countries = ["Pakistan", "China", "Turkey"]
#insert Saudi Arabia at index
countries.insert (2,"Saudi Arabia")
print(countries)


#remove()
languages = ["Python", "Java", "C++", "JavaScript"]
#Remove Java from the list
languages.remove ("Java")
print(languages)


#pop()
fruits = ["Apple", "Banana", "Mango", "Orange"]
#Remove Banana from the list
fruits.pop (1)
print(fruits)

#len()
subjects = ["English", "Math", "Physics", "Computer", "Chemistry"]
#total number of subjects using len()
print(len(subjects))


#Loop Through a List (for Loop)
languages= ["Python", "Java", "C++", "JavaScript"]
#Print every language using a for loop.
for language in languages:
    print(languages)

#in Operator
fruits = ["Apple", "Banana", "Mango", "Orange"]
#Check if Mango is in the list.
print("Mango" in  fruits)
