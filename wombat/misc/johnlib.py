ANIMALS = ['wombat',
           'pterodactyl',
           'least weasel']

def main():
    print("Hi Mom!")
    print("I like wombats!")
    ham()
    spam()
    print("I am in your codebase, killing your d00dz")


def spam():
    print("Hello from spam()")

def ham():
    print("Hello from ham()")
    _toast()

def _toast():
    print("   ...and _toast()")

print("my name is", __name__)

if __name__ == '__main__':  # if NOT imported
    main()


