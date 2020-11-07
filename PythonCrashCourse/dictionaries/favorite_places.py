favorite_places = {
    'rabbi': ['dhaka', 'sajek', 'cox bazar'],
    'piash': ['sherpure', 'sajek', 'cox bazar'],
    'borna': ['noakhali', 'sajek', 'cox bazar'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()} favorite places:")
    for place in places:
        print(f"\t{place}")