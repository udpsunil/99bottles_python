def downTo(max, min):
    return [n for n in range(max, min, -1)]

def plural(n):
    return '' if n == 1 else 's'

def how_many_bottles(n, capitalize = True):
    no_more = "No more" if capitalize else "no more"
    return no_more if n == 0 else str(n)

def take_a_bottle(n):
    return 'one' if n>1 else 'it'

def take_or_buy(n):
    return f"Take {take_a_bottle(n)} down and pass it around," if n > 0 else "Go to the store and buy some more"

def left_over_bottles(n):
    if n-1 < 0:
        return "99"
    else:
        if n-1 == 0:
            return 'no more'
        else:
            return str(n-1)

class Bottles:
    def song(self):
        return self.verses(99, 0)

    def verses(self,hi, lo):
        return "\n".join([self.verse(n) for n in range(hi, lo-1, -1)])

    def verse(self, n):
        statement = f"{how_many_bottles(n)} bottle{plural(n)} of beer on the wall, {how_many_bottles(n, False)} bottle{plural(n)} of beer.\n"                                                   
        statement += f"{take_or_buy(n)} {left_over_bottles(n)} bottle{plural(n)} of beer on the wall.\n"
        return statement


if __name__ == "__main__":
    b = Bottles()
    print(b.song())
