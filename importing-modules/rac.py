# relies upon __all__ being set in the __init__.py
from larry import *

def main():
    print("hello")

    from fred import world
    world()

    import fred
    fred.world()

    from larry.bob import universe
    universe()

    import larry.bob as bob
    bob.universe()

    import larry.bob
    larry.bob.universe()

    bob.universe()

if __name__ == "__main__":
    main()
