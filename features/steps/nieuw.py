from behave import *

def create_file(name):
    f = open(name, 'w')
    f.close()


@given(u'There is an empty text file available to us')
def step_impl(context):
    context.naam = 'file.txt'
    create_file(context.naam)

@when(u'I write the following table in it')
def step_impl(context):
    f = open(context.naam, 'w')
    for row in context.table:
        c = row["course"]
        p = row["participants"]
        f.write(c + "\t\t"+ p +"\n" )
    f.close()


@when(u'I open this file and check the numner of lines')
def step_impl(context):
    f = open(context.naam, 'r')
    lines = 0
    for i in f.readlines():
        lines += 1
    context.aantal_regels = lines 
    f.close()

@then(u'This file has 3 lines in it')
def step_impl(context):
    assert context.aantal_regels == 3


@given(u'The text file has been opened')
def step_impl(context):
    context.naam = 'file2.txt'
    context.file = open(context.naam, 'w')


@then(u'I write the values {one}, {two} and {three}')
def step_impl(context, one, two, three):
    context.file.write(one)
    context.file.write(two)
    context.file.write(three)


@then(u'I close the file')
def step_impl(context):
    context.file.close()
