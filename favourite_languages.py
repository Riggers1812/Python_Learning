favourite_languages = {
    'daniel' : 'sql', 
    'kamrul' : 'python', 
    'danielle' : 'looker', 
    'sam' : 'c'
}

for name, language in favourite_languages.items():
    print(f"\n{name.title()}'s favourite language is {language.title()}.\n")


friends = ['daniel', 'kamrul']



for name in favourite_languages.keys():
    print(f"\nHi {name.title()}.")
    
    if name in friends:
        language = favourite_languages[name].title()
        print(f"{name.title()}, I see you love {language}")


for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll.")

print("\nThe following languages have been mentioned:")
for languages in sorted(set(favourite_languages.values())):
    print(languages.title())

