import subprocess, os, requests
from bs4 import BeautifulSoup
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ['yes', 'affirmative', 'si', 'sure', 'go ahead', 'oui', 'yeah', 'positive', 'confirm', 'aye']
        self.cancel = ['no', 'negative', 'non', 'stop', 'nay', 'wait', 'cancel']

    def discover(self, text):
        if 'what' in text and 'name' in text:
            if 'my' in text:
                self.respond('You have not told me your name yet')
            else:
                self.respond('I am PySiri. How are you?')
        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

        if 'open' or 'launch' in text:
            app = text.split(" ", 1)[-1]
            # MacOS only/ Linux probably
            self.respond("Opening " + app)
            os.system('open -a ' + app + '.app')

    def respond(self, response):
        print(response)
        subprocess.call("say '" + response + "'", shell=True)
