#!/usr/bin/python3

# Simple installer script

if not __name__=='__main__':
	raise Exception('This is a program, not a module.')

import os
import sys
import shutil


try:
	from termcolor import colored
except ImportError:
	# We can run even if we do not have termcolor
	def colored(text, *ignore_args, **ignore_these_too):
		return text

## HELPER FUNCTIONS

def print_usage():
	print(
"Install dotfiles.\n"
"\n"
"Usage:\n"
"        dotfiles -h\n"
"        dotfiles [-f]\n"
"\n"
"Options:\n"
"        -h --help       Show this screen\n"
"        -f --force      Force installation\n"
"        -v --verbose    Increase verbosity\n"
"        --version       Print version\n"
	)
	sys.exit(-1)

def args_parse(args):
	fail=False
	if '-h' in args or '--help' in args:
		print_usage()

	for a in args[1:]:
		if a=='-h' or a=='--help':
			pass
		elif a=='-f' or a=='--force':
			global force
			force=True
		elif a=='-v' or a=='--verbose':
			global verpose
			verbose=1
		else:
			print('Unknown option: '+a)
			fail=True

	if fail:
		print('Use -h for help.')
		sys.exit(-1)

def install(src, dest):
	"""Installs the file <src> to <dest> and prints useful messages.
	Raises an exception if installation failed"""
	dest=os.path.expanduser(dest)
	sys.stdout.write('{0: <71}'.format('Installing {} -> {}'.format(src,dest)))
	try:
		try:
			os.mkdir(os.path.dirname(dest))
		except FileExistsError:
			pass
		shutil.copy2(src,dest)
	except:
		status=colored('FAILED','red')
		raise
	else:
		status=colored('  OK  ','green')
	finally:
		print ('[{}]'.format(status))


## SET SOME GLOBAL PARAMETERS

homedir=os.path.expanduser('~')
markfile=os.path.join(homedir,'.dotfiles')

verbose=0
force=False

args_parse(sys.argv)

## START OF MAIN CODE

if os.path.isfile(markfile) and not force:
	print('Dotfiles are already installed. Use -f to override.')
	sys.exit(-1)


print('Done! Writing markfile.')
install('markfile',markfile)
