# Mad Libs Project in Python

def mad_libs():
    print("Welcome to Mad Libs!")
    print("Fill in the blanks to create a fun story.\n")

    # Ask for inputs
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb ending in 'ing': ")

    # The story
    story = f"""
    Once upon a time, there was a person named {name}.
    {name} lived in a magical land called {place}, where the skies were always {adjective}.
    One day, {name} met a {adjective} {animal} that loved {verb}.
    Together, they went on an adventure to find the best {food} in all of {place}.
    It was a {adjective} day filled with laughter and joy!
    """

    # Output the story
    print("\nHere is your Mad Libs story:\n")
    print(story)

# Run the Mad Libs game
if __name__ == "__main__":
    mad_libs()
