from behave import *
from hamcrest import *
from splinter import *


@given(u'I got me some open browser')
def step_impl(context):
    context.browser = Browser('chrome') 


@given(u'the browser is on the webpage terschelling.nl/home-terschelling')
def step_impl(context):
    context.browser.visit("https://terschelling.nl/home-terschelling")


@when(u'i press {button}')
def step_impl(context, button):
    try:
        a = context.browser.find_by_text(button)
        a.click()
    except:
        try:
            a = context.browser.find_by_name(button)
            a.click()
        except:
            try:
                a = context.browser.find_by_id(button)
                a.click()
            except:
                try:
                    a = context.browser.find_by_value(button)
                    a.click()
                except:
                    try:
                        a = context.browser.links.find_by_partial_text(button)
                        a.click()
                    except:
                        context.browser.find_by_name(button).first.click()

@when(u'i type hello in the searchbar')
def step_impl(context):
    context.browser.fill('trefwoord', 'hello')

@then(u'i\'am at {url}')
def step_impl(context, url):
    assert url == context.browser.url

@then(u'i close the browser')
def step_impl(context):
    context.browser.quit()

@then(u'{var} {vorm} is present')
def step_impl(context,var, vorm):
    if vorm == 'text':
        assert context.browser.is_text_present(var)    