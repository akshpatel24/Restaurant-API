class Find:

    def perfect_square_root(num):
        return int(num**0.5)**2 == num

    def is_square_root(self):
        num = int(input("Enter a number: "))
        if Find.perfect_square_root(num):
            print( "It is a perfect square.")
        else:
            print("This is not a perfect square.")

# Example usage:
Finder = Find()
Finder.is_square_root()
