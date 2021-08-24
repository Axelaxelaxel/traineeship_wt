from splinter import *
import time

browser = Browser('chrome') 
browser.visit("https://www.terschelling.nl/home-terschelling")
find = browser.find_by_id('search_trefwoord')
browser.fill('trefwoord', 'balzak')
button = 'ZOEK'
try:
    a = browser.find_by_text(button)
    a.click()
    print('mamma mia')
except:
    try:
        a = browser.find_by_name(button)
        a.click()
        print('wamba')
    except:
        try:
            a = browser.find_by_id(button)
            a.click()
            print('Chibbi')
        except:
            try:
                a = browser.find_by_value(button)
                a.click()
                print('Halleluja')
            except:
                try:
                    a = browser.links.find_by_partial_text(button)
                    a.click()
                    print('Huh')
                except:
                        browser.find_by_name(button).first.click()

time.sleep(2)

browser.quit()




