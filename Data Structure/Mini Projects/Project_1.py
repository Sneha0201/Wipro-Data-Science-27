#People & facts

def main():
    people = {
        "Jeff": "Is afraid of dogs.",
        "David": "Plays the piano.",
        "Jason": "Can fly an airplane."
    }
    print("Sample Output:\n")
    for name, fact in people.items():
        print(f"{name}: {fact}")
    print()
    people["Jeff"] = "Is afraid of heights."
    people["Jill"] = "Can hull dance."
    print("Updated Output:\n")
    for name, fact in people.items():
        print(f"{name}: {fact}")

if __name__ == "__main__":
    main()