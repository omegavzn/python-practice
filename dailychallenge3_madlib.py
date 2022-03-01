# Excercise: String Concatenation
# Create a madlib worksheet that prompts users for input

# Define variables that prompt for user inputs
adj1 = input("Adjective: ")
noun1 = input("Noun: ")
pt_verb = input("Verb (past tense): ")
adverb1 = input("Adverb: ")
adj2 = input("Adjective: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
adj3 = input("Adjective: ")


# Madlib script f-string
madlib = f"Today I went to the zoo. I saw a(n) {adj1} \
{noun1} jumping up and down in its tree. He {pt_verb} \
{adverb1} through the large tunnel that led to its {adj2} \
{noun2}. I got some peanuts and passed them through the cage \
to a gigantic gray {noun3} towering above my head. Feeding that \
animal made me hungry. I went to get a {adj3} scoop of ice cream \
. It filled my stomach."

# Run madlib
print(madlib)