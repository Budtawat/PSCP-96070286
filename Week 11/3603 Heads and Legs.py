"""Heads and Legs"""
def main():
    """Calculate rabbits and birds."""
    heads = int(input())
    legs = int(input())
    if not legs % 2:
        rabbits = (legs - 2 * heads) // 2
        birds = heads - rabbits
        if rabbits >= 0 and birds >= 0:
            print(rabbits, birds)
            return
    print("Impossible")
main()
