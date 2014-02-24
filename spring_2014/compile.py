import os
from subprocess import Popen
from sys import exit


# List of TeX files
texfiles = []
for root, dirs, files in os.walk('.'):
	for f in files:
		if f.endswith('.tex'):
			texfiles.append((os.path.join(root,f),False))
			
			
# Default arguments
mode = 'batchmode'
out_frmt = 'pdf'
		
		
# Print options
print('[q] Quit')
print('[v] Verbose messages')
# print('[d] Output format DVI (PDF default)')
print('[a] Compile all TeX files')
for i in range(0,len(texfiles)):
	print('[%s] %s' % (i,texfiles[i][0]));
# Get selection(s)
input = input('Selection(s): ')
# Parse user selection(s)
for s in input:
	if s is 'q':
		exit()
	elif s is 'v':
		mode = 'nonstopmode'
	# elif s is 'd':
		# out_frmt = 'dvi'
	elif s is 'a':
		texfiles = list(map(lambda x: (x[0], True), texfiles))
	elif s.isdigit():
		i = int(s)
		if 0 <= i < len(texfiles):
			texfiles[i] = (texfiles[i][0], True)
		else:
			print('ERROR: Index "%s" is outside possible range'%(i))
	else:
		print('ERROR: Unknown selection "%s"' % (s))
	
	
# Configure arguments
out_dir = './out-'+out_frmt
args = (
	'pdflatex',
	'-halt-on-error',
	'-interaction='+mode,
	'-output-dir='+out_dir,
	'-output-format='+out_frmt,
)
	
	
# Compile output documents
if not os.path.exists(out_dir):
	os.makedirs(out_dir)
error_msgs = []
errors = False;
for f in texfiles:
	if f[1]:
		file = os.path.abspath(f[0])
		status = Popen(args+(file,))
		status.wait()
		if status.returncode is 1:
			errors = True
			error_msgs.append('ERROR: Failed to compile %s' % f[0])
		

# Clean up
extensions = ('.aux', '.log')
for f in os.listdir(out_dir):
	if any(f.endswith(ext) for ext in extensions):
		os.remove(os.path.join(out_dir,f))


if errors:
	print()
	print('--- ERRORS: ---')
	for e in error_msgs:
		print('"%s"'%e)
	os.system('Pause')