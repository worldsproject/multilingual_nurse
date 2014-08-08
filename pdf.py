import itertools

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0

pdfmetrics.registerFont(TTFont('Noto', '/usr/share/fonts/TTF/HAN NOM A.ttf'))
pdfmetrics.registerFont(TTFont('other', '/usr/share/fonts/TTF/amiri-regular.ttf'))

width, height = letter
mid = u' \u2B0C '

filenames = ['english.txt', 'spanish.txt', 'german.txt', 'french.txt', 'viet.txt', 'arabic.txt', 'chinese.txt']

c = itertools.combinations(filenames, 2)

"""[x for x in c]"""

def f2l(f):
	with open(f) as fi:
		content = fi.readlines()
		
	for l in content:
		l = l.encode('utf-8')
		
	return content

def create(c, left, right):
	c.drawString(100, height-100, left[0])
	c.drawString(100, height-150, right[0])
	
	c.drawString(100, height-300, left[1] + mid + right[1])
	
	c.drawString(100, height-350, left[2] + mid + right[2])
	
	c.drawString(100, height-400, left[3] + mid + right[3])
	
	c.drawString(100, height-450, left[4] + mid + right[4])
	
	c.drawString(100, height-500, left[5] + mid + right[5])
	
	c.drawString(100, height-550, left[6] + mid + right[6])

c = canvas.Canvas("test.pdf")
create(c, f2l(filenames[0]), f2l(filenames[5]))
c.showPage()
c.save()
