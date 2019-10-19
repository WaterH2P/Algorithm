from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('starttag : tag : <%s>; attrs : %s' % (tag, str(attrs)))

    def handle_endtag(self, tag):
        print('endtag : </%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('startendtag : <%s/>' % tag)

    def handle_data(self, data):
        print('data : %s' % data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# 尝试分析 https://www.python.org/events/python-events/