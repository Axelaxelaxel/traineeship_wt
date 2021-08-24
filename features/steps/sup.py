from behave import *
def transfer_money(balance, amount, max_amount):
    if amount > 0 and amount <= 5000:
        if amount > max_amount:
            return False
        else: 
            return True
    return False


@given(u'I have {balance} euro in my bank account')
def step_impl(context, balance):
    context.balance = int(balance)


@given(u'my bank allows me to transfer {max_amount} euro max')
def step_impl(context, max_amount):
    context.max_amount = int(max_amount)


@when(u'I transfer {amount} euro to my friends bank account')
def step_impl(context, amount):
    context.amount = int(amount)
    context.result = transfer_money(context.balance, context.amount, context.max_amount)


@then(u'the money has {transferstate} been transferred')
def step_impl(context, transferstate):
    if transferstate == 'not':
        assert context.result == False
    else: assert context.result == True



