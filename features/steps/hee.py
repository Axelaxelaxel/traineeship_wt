from behave import *
from hamcrest import *
from splinter import *
import logging


@given(u'I have an open chrome browser')
def step_impl(context):
    context.browser = Browser('chrome') 
    logging.info('hee daar')

@when(u'the browser is on the webpage duckduckgo.com')
def step_impl(context):
    context.browser.visit("https://duckduckgo.com")
    logging.info("hoe gaat het?")


@when(u'I fill in the search bar with hee')
def step_impl(context):
    context.browser.fill('q', 'hee')
    logging.info("Goed bezig")


@when(u'I execute the search')
def step_impl(context):
    button = context.browser.find_by_id('search_button_homepage')
    button.click() 
    logging.info("bijna klaar al.") 


@then(u'I\'ll quit the browser')
def step_impl(context):
    assert_that(context.browser.html, has_string('social'))
    context.browser.quit()
    logging.info("mooi hoor")
