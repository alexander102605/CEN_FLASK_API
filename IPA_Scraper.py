from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def returnIPA(lang, word):
    req = Request('https://' + lang + '.wiktionary.org/wiki/' + word ,headers={'User-Agent':'Mozilla/5.0'})
    # en for English, es for Spanish, etc etc
    sb = urlopen(req).read()
    soup = BeautifulSoup(sb,'html.parser')
    HTML_text = soup.get_text().split()
    # catch-all if statements since it's listed differently sometimes
    if 'IPA(key):' in HTML_text:
        IPA_index = HTML_text.index('IPA(key):') + 1
    elif 'IPA:' in HTML_text:
        IPA_index = HTML_text.index('IPA:') + 1
    elif '(AFI)' in HTML_text:
        IPA_index = HTML_text.index('(AFI)') + 1
    else:
        return 'No IPA Data Found'
        # If the chosen website has no IPA
    IPA = HTML_text[IPA_index].replace('/','').replace(',','').replace('ˈ','').replace('[','').replace(']','')
    # cleans up the string so its just the IPA
    return [word, IPA]


