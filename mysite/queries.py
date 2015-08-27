# from /Users/darwright/PycharmProjects/Django/mysite/puzzles/models.py import Puzzle, Clue, PuzzleBoard

from mysite.puzzles.models import PuzzleBoard

# puz = Puzzle()
# clue = Clue()
# pb = PuzzleBoard()

# def fillBoards(class):
# for i, j in range(1, 3):
#     pb = PuzzleBoard(width=i, height=j)
#     pb.save()

# i = 4
# j = 5
# pb = PuzzleBoard(width=i, height=j)
# pb.save()


# one_entry = Entry.objects.get(pk=1)

test = PuzzleBoard.objects.get(pk=1)
print test

from puzzles.models import PuzzleBoard


def makeBoards():
    for i in range(1,101):
        for j in range(1,101):
            puzb=PuzzleBoard(height=i, width=j)
            puzb.save()

