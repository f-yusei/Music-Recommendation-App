import re
import webbrowser

def trans_word(inputtext):
    replacements = {'api': 'open', '/v1': None}
    print('({})'.format('|'.join(map(re.escape,replacements.keys()))))
    track_link = re.sub('({})'.format('|'.join(map(re.escape,replacements.keys()))),\
    lambda m:replacements[m.group()], inputtext)
    webbrowser.open(track_link,1)
    return 0

if __name__ == '__main__':
    trans_word()
