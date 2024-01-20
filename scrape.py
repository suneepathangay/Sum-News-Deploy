from html.parser import HTMLParser
import requests



class Parser(HTMLParser):
     def __init__(self):
        super().__init__()
        self.inside_p_tag = False
        self.text_content = []

     def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.inside_p_tag = True

     def handle_data(self, data):
        if self.inside_p_tag:
            self.text_content.append(data)

     def handle_endtag(self, tag):
        if tag == 'p':
            self.inside_p_tag = False

     def get_text_content(self):
        return ' '.join(self.text_content)
 
                 
parser=Parser()


text=requests.get('https://www.lse.ac.uk/philosophy/blog/2016/08/17/why-is-doping-wrong-anyway/').text
parser.feed(text)
print(parser.get_text_content())

