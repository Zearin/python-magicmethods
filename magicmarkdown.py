"""
magicmarkdown.py
utility script for changing markdown from magic methods guide into HTML
"""

import io
import markdown

HEADER = u"""<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<title>A Guide to Python's Magic Methods &laquo; rafekettler.com</title>
<meta name="description" content="A guide to all the Magic Methods in Python" />
<meta name="keywords" content="python, programming, magic methods, object-oriented, oop" />
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
"""

FOOTER = u"""<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-18615621-3']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
</body>
</html>
"""

MARKDOWN_BASENAMES = ('table', 'magicmethods', 'appendix')
TEXT = dict()


def main():
    for basename in MARKDOWN_BASENAMES:
        filename = basename + '.markdown'
        with io.open(filename, mode='r') as file:
            contents = file.read()
            TEXT[basename] = contents

    table_text = markdown.markdown(TEXT['table'])
    body_text = markdown.markdown(TEXT['magicmethods'], ['def_list', 'codehilite'])
    appendix_text = markdown.markdown(TEXT['appendix'], ['tables'])
    
    with io.open('magicmethods.html', mode='w', encoding='UTF-8') as out:
        out.write(HEADER)
        out.write(table_text)
        out.write(body_text)
        out.write(appendix_text)
        out.write(FOOTER)


if __name__ == '__main__':
    import sys
    sys.exit(main())
