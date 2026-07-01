#Find the name

def count_name_occur(text, name="Alex"):
    return text.count(name)

def main():
    sample = "Hi Alex WelcomeAlex Bye Alex."
    s = input("Enter the text (or press enter to use the sample):").strip()
    if not s:
        s = sample
    name = input("Enter the name to count (defualt 'ALex'): ").strip()
    if not name:
        name = "Alex"
    count = count_name_occur(s, name)
    print(count)

if __name__ == "__main__":
    main()