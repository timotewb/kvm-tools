import curses

# define null char
NULL_CHAR = chr(0)

# define function to write to keyboard
def write_report(report):
	with open('/dev/hidg0', 'rb+') as fd:
		fd.write(report.encode())

# define lists of keys
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
number_symbols = ['!','@','#','$','%','^','&','*','(',')']
symbols01 = ['-','=','[',']','\\']
symbols02 = [';',"'"]
symbols03 = [',','.','/']

# define main function
def main(stdscr):
	#stdscr.clear()
	curses.echo()
	while True:
  
		# Store the key value in the variable `key`
		# Catch ctrl+c and send rather than kill script
		try:
			key = stdscr.getch()
		except KeyboardInterrupt:
			key = -1
		
		if key == -1:
			key = 9999

		#--- text
		if str(chr(key)) in lower_case:
			write_report(NULL_CHAR*2+chr((key - 93))+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif str(chr(key)) in upper_case:
			write_report(chr(32)+NULL_CHAR*2+chr((ord(str(chr(key)).lower()) - 93))+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		
		#--- symbols
		elif str(chr(key)) == ' ':
			write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif str(chr(key)) in number_symbols:
			num = number_symbols.index(str(chr(key)))+30
			write_report(chr(32)+NULL_CHAR*2+chr(num)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif str(chr(key)) in symbols01:
			num = symbols01.index(str(chr(key)))+45
			write_report(NULL_CHAR*2+chr(num)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif str(chr(key)) in symbols02:
			num = symbols02.index(str(chr(key)))+51
			write_report(NULL_CHAR*2+chr(num)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif str(chr(key)) in symbols03:
			num = symbols03.index(str(chr(key)))+54
			write_report(NULL_CHAR*2+chr(num)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
			
		#--- numbers
		elif str(chr(key)) in numbers:
			num = numbers.index(str(chr(key)))+30
			write_report(NULL_CHAR*2+chr(num)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		
		#--- action keys
		elif key in [curses.KEY_ENTER, ord('\n')]:
			write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif key in [curses.KEY_BACKSPACE, ord('\b')]:
			write_report(NULL_CHAR*2+chr(42)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif key in [ord('\t')]:
			write_report(NULL_CHAR*2+chr(43)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		
		#--- navigation
		elif key == curses.KEY_UP:
			write_report(NULL_CHAR*2+chr(82)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif key == curses.KEY_DOWN:
			write_report(NULL_CHAR*2+chr(81)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif key == curses.KEY_LEFT:
			write_report(NULL_CHAR*2+chr(80)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
		elif key == curses.KEY_RIGHT:
			write_report(NULL_CHAR*2+chr(79)+NULL_CHAR*5)
			write_report(NULL_CHAR*8)
			
    #--- ctrl+ keys
		elif key == 22:
			print('ctrl+v')
			write_report(chr(17)+chr(0)+chr(25)+chr(0)*5)
			write_report(NULL_CHAR*8)
		elif key == 9999:
			print('ctrl+c')
			write_report(chr(17)+chr(0)+chr(6)+chr(0)*5)
			write_report(NULL_CHAR*8)
		elif key == 24:
			print('ctrl+x')
			write_report(chr(17)+chr(0)+chr(27)+chr(0)*5)
			write_report(NULL_CHAR*8)
		elif key == 15:
			print('ctrl+o')
			write_report(chr(17)+chr(0)+chr(18)+chr(0)*5)
			write_report(NULL_CHAR*8)
		elif key == 55:
			print('ctrl+y')
			write_report(chr(17)+chr(0)+chr(28)+chr(0)*5)
			write_report(NULL_CHAR*8)
		elif key == 10:
			print('ctrl+m')
			write_report(chr(17)+chr(0)+chr(16)+chr(0)*5)
			write_report(NULL_CHAR*8)
			
		else:
			stdscr.addstr(key)
			stdscr.addstr("This program doesn't know that key.....")

# run main function (loop)
curses.wrapper(main)
