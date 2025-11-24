story = """
Today, I went to the {place}. I saw a {adjective} {animal} jumping up and down in {thing}.
It made me feel {emotion}, so I {verb} as fast as I could. When I got home, I {past_tense_verb}
and had a {food} for dinner. What a {adjective} day!
"""

words = {
   "place": input("Enter a place: "),
   "adjective": input("Enter an adjective: "),
   "animal": input("Enter an animal: "),
   "thing": input("Enter a thing: "),
   "emotion": input("Enter an emotion: "),
   "verb": input("Enter a verb: "),
   "past_tense_verb": input("Enter a past tense verb: "),
   "food": input("Enter a type of food: ")
}

print("\nHere’s your Mad Libs story:\n")
print(story.format(**words))