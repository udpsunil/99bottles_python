class Bottles:
    def verse(self, number):
        match number:
            case 0:
                return f"No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
            case 1:
                return f"{number} bottle of beer on the wall, {number} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n"
            case 2:
                return f"{number} bottles of beer on the wall, {number} bottles of beer.\nTake one down and pass it around, {number-1} bottle of beer on the wall.\n"
            case _:
                return f"{number} bottles of beer on the wall, {number} bottles of beer.\nTake one down and pass it around, {number-1} bottles of beer on the wall.\n"

    def verses(self, max, min):
        return "".join([self.verse(n) for n in range(max, min-1, -1)])
    
    def song(self):
        return self.verses(99,0)


if __name__ == "__main__":
    b = Bottles()
    print(b.song())