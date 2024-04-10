#screwup
import webbrowser
import time
import random

while True:
    sites=random.choice(['google.com','youtube.com','edx.com'])
    visit='http://{}'.format(sites)
    webbrowser.open(visit)
    seconds=random.randrange(5,10)
    time.sleep(seconds)
