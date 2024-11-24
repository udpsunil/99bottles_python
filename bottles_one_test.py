import pytest
from bottles_tdd import Bottles


@pytest.fixture
def bottles():
    return Bottles()

class TestBottlesOne:
    def test_the_first_verse(self, bottles):
        expected = '99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall.\n'       
        assert bottles.verse(99) == expected

    def test_another_verse(self, bottles):
        expected = '3 bottles of beer on the wall, 3 bottles of beer.\nTake one down and pass it around, 2 bottles of beer on the wall.\n'
        assert bottles.verse(3) == expected

    def test_verse_2(self, bottles):
        expected = '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'
        assert bottles.verse(2) == expected

    def test_verse_1(self, bottles):
        expected = '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n'
        assert bottles.verse(1) == expected

    def test_verse_0(self, bottles):
        expected = 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n'
        assert bottles.verse(0) == expected

    def test_a_couple_verses(self, bottles):
        expected = '99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall.\n98 bottles of beer on the wall, 98 bottles of beer.\nTake one down and pass it around, 97 bottles of beer on the wall.\n'
        assert bottles.verses(99, 98) == expected

    def test_song(self, bottles):
        expected = "".join([bottles.verse(n) for n in range(99, -1, -1)])
        assert bottles.song() == expected