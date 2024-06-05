#!/usr/bin/python
print('Content-type: text/html\n')

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Dream</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""

html= HTML_HEADER
html+= '<p> You close your eyes </p>'

print(html)

