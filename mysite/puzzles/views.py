from django.shortcuts import render, render_to_response
from .models import Clue, Puzzle, PuzzleBoard
# Create your views here.

def landing(request):
    return render_to_response(
        'homepage.html',
    )

def clues_count(request):
    total_clues = Clue.objects.count()
    return render_to_response(
        'total_clues.html',
        context={
            'total_clues' : total_clues,
        }
    )

def puzzles_with_10_or_less(request):
    puzzles_with_lt_10 = Clue.objects.filter(puzzle__puzzle_board__width__lte=10)
    return render_to_response(
        'puzzles_lt_10.html',
        context={
            'puzzles_with_lt_10': puzzles_with_lt_10
        }
    )

def devlish_puzzles(request):
    devil_puzzle_clues = Clue.objects.filter(puzzle__difficulty='DE')
    return render_to_response(
        'devlish_puzzles.html',
        context={
            'devil_puzzle_clues': devil_puzzle_clues
        }
    )

def puzzles_not_10x10(request):
    puzzles_not_10x10 = Puzzle.objects.exclude(puzzle_board__width=10, puzzle_board__height=10)
    return render_to_response(
        'puzzles_not_10_x_10.html',
        context={
            'puzzles_not_10x10': puzzles_not_10x10
        }
    )

def puzzles_from_given_clue(request):
    clue = Clue.objects.first()
    puzzles_list = clue.puzzle_set.all()
    return render_to_response(
        'puzzles_that_use_a_clue.html',
        context={
            'puzzles_that_use_a_clue': puzzles_list
        }
    )

def test_puzzles(request):
    puzzles_list = Clue.objects.filter(puzzle__difficulty='DE')
    return render_to_response(
        'clues.html',
        context={
            'puzzles': puzzles_list
        }
    )

def puzzles_with_10_or_less_same_template(request):
    puzzles_list = Clue.objects.filter(puzzle__puzzle_board__width__lte=10)
    return render_to_response(
        'clues.html',
        context={
            'puzzles': puzzles_list
        }
    )

def devlish_puzzles_same_template(request):
    puzzles_list = Clue.objects.filter(puzzle__difficulty='DE')
    return render_to_response(
        'clues.html',
        context={
            'puzzles': puzzles_list
        }
    )
def puzzles_not_10x10_st(request):
    puzzles_list = Puzzle.objects.exclude(puzzle_board__width=10, puzzle_board__height=10)
    return render_to_response(
        'puzzles.html',
        context={
            'puzzles': puzzles_list
        }
    )

def puzzles_from_given_clue_st(request):
    clue = Clue.objects.first()
    puzzles_list = clue.puzzle_set.all()
    return render_to_response(
        'puzzles.html',
        context={
            'puzzles': puzzles_list
        }
    )

def template_fun(request):

    return render_to_response(
    'template_fun.html',
        context={
            'clue': Clue.objects.first(),
            'list_var': [1, [1,2,3], 3, ['grape', 'orange', ['washington apple', 'red delicious']]],
            'dict_var': {'one':1, 'two':2}

        }
    )

def monday_challenge(request):
    puzzles_with_lt_10 = Clue.objects.filter(puzzle__puzzle_board__width__lte=10)
    list_movie = ['Mad Max 2', 'Fantastic Dizzy', 'Dragonfyre',
                    'Yu chang jian', 'A Case for Murder', 'Teresa Venerdi',
                        'Operation Ganymed', 'La guerra de los bikinis',
                        'Atashparehe Tehran', 'Sulla punta del naso', 'Die Vier im Jeep',
                        'Herzensbrecher', 'The Barber of Seville', 'Stealing Chanel',
                        'Josei yokoushu toire', 'No Mans Land Number 11', 'Lultimo combattimento',
                        'Gang xing xian sheng']

    return render_to_response(
        'monday_challenge.html',
        context={
            'puzzles': puzzles_with_lt_10,
            'myList': list_movie,
            'tired': True,
            'noList': [],
        }
    )