import re

def format_file(file):
	lines = []

	end_pattern = re.compile("\)[ \t]+\{")
	pattern = re.compile('([ \t]+)(.*\)[ \t]+)\{', flags=re.MULTILINE)

	with open(file) as f:
		for line in f:
			match = pattern.match(line)
			if pattern.match(line):
				indent_level =  match.groups()[0]
				line = end_pattern.sub(")\n" + indent_level + "{", line)
			lines.append(line)


	with open(file, 'w') as f:
		f.write("".join(lines))


if __name__ == '__main__':
  import sys
	format_file(sys.argv[1])
