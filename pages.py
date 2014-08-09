import itertools

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('pages', 'templates'))

template = env.get_template('/page.html')

files = ['english.txt', 'french.txt', 'german.txt', 'viet.txt', 'chinese.txt', 'spanish.txt', 'arabic.txt']

combs = itertools.combinations(files, 2)

def file_to_list(f):
	with open('lang/' + f) as fi:
		content = fi.readlines()
		
	for l in content:
		l = l.encode('utf-8')
		
	return content
	
def render_from_content(left, right):
	l_header = left[0]
	l_hungry = left[1]
	l_thirsty = left[2]
	l_tired = left[3]
	l_pain = left[4]
	l_feeling = left[5]
	l_bathroom = left[6]
	l_translator = left[7]
	
	r_header = right[0]
	r_hungry = right[1]
	r_thirsty = right[2]
	r_tired = right[3]
	r_pain = right[4]
	r_feeling = right[5]
	r_bathroom = right[6]
	r_translator = right[7]
	
	template = env.get_template('page.html')
	
	return template.render(left_header=l_header, right_header=r_header,
		left_hungry=l_hungry, right_hungry=r_hungry,
		left_thirsty=l_thirsty, right_thirsty=r_thirsty,
		left_tired=l_tired, right_tired=r_tired,
		left_pain=l_pain, right_pain=r_pain,
		left_feeling=l_feeling, right_feeling=r_feeling,
		left_bathroom=l_bathroom, right_bathroom=r_bathroom,
		left_translator=l_translator, right_translator=r_translator)
		
for x in combs:
	if(x[0] < x[1]):
		f = open('pages/' + x[0][:-4] + '_' + x[1][:-4] + '.html', 'w')
		f.write( render_from_content( file_to_list(x[0]), file_to_list(x[1])))
		f.close()
	else:
		f = open('pages/' + x[1][:-4] + '_' + x[0][:-4] + '.html', 'w')
		f.write( render_from_content( file_to_list(x[1]), file_to_list(x[0])))
		f.close()
