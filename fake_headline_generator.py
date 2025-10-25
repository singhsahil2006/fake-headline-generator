import random


subjects=["The government",
         "A celebrity", 
         "Scientists", 
         "A tech company", 
         "An influencer"
]
action=["announced",
        "discovered",
        "revealed",
        "launched",
        "investigated"
]
place_or_object=["a new policy",
                 "a groundbreaking study",
                 "a revolutionary gadget",
                 "a controversial trend",
                 "a hidden truth"
]
while True:
    subjects=random.choice(subjects)
    action=random.choice(action)
    place_or_object=random.choice(place_or_object)
    fake_news_headline=f"{subjects} {action} {place_or_object}."
    print("\n" + fake_news_headline)
    user_input=input("Do you want another headline? (yes/no): ").strip() 
    if user_input.lower() != 'yes':
        break

print("Thank you for using the Fake News Headline Generator!")