from tictactoe import *
from behave import *

def pythonator(c, r):
    return int(c)-1, int(r)-1

@given(u'we have an empty tic-tac-toe board')
def step_impl(context):
    context.board = EMPTY_BOARD


@when(u'I play {p} on column {c} and row {r} on the board')
def step_impl(context, c, r, p):
    nc, nr = pythonator(c,r)
    context.board, context.winner = play(context.board, p, nc, nr)


@when(u'I ask the computer to do its best move for O')
def step_impl(context):
    context.board, context.winner = play_best_move(context.board, 'O')


@then(u'the board has a O in column 1 and row 1 on the board')
def step_impl(context):
    assert context.board[0] == 'O'


@then(u'O is the winner of the game')
def step_impl(context):
    assert context.winner == 'O'

@when(u'the following game is being played')
def step_impl(context):
    for i in context.table:
        nc, nr = pythonator(i['c'], i['r'])
        context.board, context.winner = play(context.board, i['p'], nc, nr)

@then(u'it\'s a tie')
def step_impl(context):
    assert context.winner == 'T'
