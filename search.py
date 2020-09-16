'''
	This program uses your default browser.
	It searches for the title in all the overdrives provided


	More things I could do:
		- allow them to modify their search
			- as they are going for one at a time or restart
		- allow them to use a text file to get the websites

'''

import webbrowser

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


urls = [
			'https://mvlc.overdrive.com/search?query={}',
			'https://bpl.overdrive.com/bpl-visitor/content/search?query={}',
			'https://clamsnet.overdrive.com/clamsnet-visitor/content/search?query={}',
			'https://cwmars.overdrive.com/cwmars-visitor/content/search?query={}',
			'https://minuteman.overdrive.com/minuteman-visitor/content/search?query={}',
			'https://noble.overdrive.com/noble-visitor/content/search?query={}',
			'https://ocln.overdrive.com/ocln-visitor/content/search?query={}',
			'https://sails.overdrive.com/sails-visitor/content/search?query={}',
			'https://mcgill.overdrive.com/search?query={}',
			'https://www.hoopladigital.com/search?page=1&q={}&scope=everything&type=direct',
			'https://mvlc.ent.sirsi.net/client/en_US/manchester1/search/results?qu={}&te='
		]

def bold(txt):
 	return color.BOLD + txt + color.END


def welcome():
	print('\n\nWelcome to ' + bold('library search!') +'\n')

	print('Here you can search for the title and/or author in all the Overdrives and other library resources provided' 
			+ ' using your default web browser.')

	print('\nSimply search as you normally would by searching a title and/or author.')
	print('You have the option to search sites one by one or all at once.\n')


# check if they want to search all at once or one at a time
# helper for user_input()
def check_speed(speed):
	# if slow search
	if speed == '':
		return False
	# else fast search
	else:
		return True


def user_input():
	search = input("\nEnter a title and/or author: ")
	print("\nDo you prefer a search all at once or one at a time?")
	print("  (1) All at once: type '" + bold("all") + "' or any other characters")
	print("  (2) One at a time: just press " + bold('enter'))
	speed_input = input("\nYour choice:")

	return check_speed(speed_input), search


def search_fast(search):
	first_loop = True

	print('\nYou are searching all at once.')

	for url in urls:
		url = url.format(search)

		if first_loop:
			webbrowser.open(url, new=1, autoraise=True)
			first_loop = False
		else:
			webbrowser.open_new_tab(url)

	print('Your search is complete. I hope you found what you were looking for!')


# helper method for search_slow(search)
def check_done(input):
	if input.lower() == 'done':
		return True
	else:
		return False


def search_slow(search):
	first_loop = True

	print("\nYou are searching one at a time.")

	for url in urls:
		url = url.format(search)

		if first_loop:
			webbrowser.open(url, new=1, autoraise=True)
			first_loop = False
		else:
			webbrowser.open_new_tab(url)

		# edge case of the last one - check if this works
		last_url = urls[-1].format(search)
		if url != last_url:
			usr_done = input("\nPress enter when you are ready to do the next search. \nFound what you're looking for? Type '" + bold('done') + "' to skip remaining searches. ")
			
			if check_done(usr_done):
				break

	print('\nYour search is complete. I hope you found what you were looking for!')


def goodbye():
	print('\n\nThank you for using search-libraries.')
	print('Enjoy your new read or listen!\n')


def main():
	welcome()

	while True:
		fast, search = user_input()
		if fast:
			search_fast(search)
		else:
			search_slow(search)

		exit = input("\nType 'exit' to quit the program. Press enter or type anything else to continue.")
		if exit.lower() == 'exit':
			break


	goodbye()


if __name__ == '__main__':
	main()











