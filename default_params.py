# def laugh(strength=2):
#     print("HA" * strength)

# laugh(10)
# laugh()

def slugify(phrase, sep="-"):
    return  phrase.lower().strip().replace(" ", sep)

slugify("hello pretty face")
slugify("hello pretty face", "_")

def greet(person, msg):
    print(f"{msg}, {person}!")