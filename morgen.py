from splinter import *
import time

browser = Browser('chrome') 
browser.visit("https://www.terschelling.nl/home-terschelling")
find = browser.find_by_id('search_trefwoord')
browser.fill('trefwoord', 'hee')
button = 'ZOEK'
try:
    a = browser.find_by_text(button)
    a.click()

except:
    try:
        a = browser.find_by_name(button)
        a.click()
    except:
        try:
            a = browser.find_by_id(button)
            a.click()

        except:
            try:
                a = browser.find_by_value(button)
                a.click()

            except:
                try:
                    a = browser.links.find_by_partial_text(button)
                    a.click()

                except:
                        browser.find_by_name(button).first.click()

time.sleep(2)

browser.quit()




