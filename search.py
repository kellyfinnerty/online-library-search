import webbrowser
import csv
import pdb


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   ITALICS = '\033[3m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def format(col, txt):
 	return col + txt + color.END

def format_input(txt):
 	return input(format(color.PURPLE, txt))


def read_file(filename):
	global urls

	with open(filename) as f:
		reader = csv.reader(f, delimiter=",", skipinitialspace=True)
		urls = [row for row in reader]

	urls = urls[1:len(urls)]


def welcome():
	print('\n\nWelcome to ' + format(color.DARKCYAN, 'Library Search') +'!\n')

	print('Here you can search for the title and/or author in all the Overdrives and other library resources' 
			+ ' using your default web browser.')

	print('\nSimply search a title and/or author as you would normally.')
	print('You have the option to search sites one at a time or all at once.\n')


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
	search = format_input("\nEnter a title and/or author: ")
	print("\nDo you prefer a search all at once or one at a time?")
	print("  (1) " + format(color.YELLOW, "All at once: ") + " type " + format(color.UNDERLINE, "all") + " or any other characters")
	print("  (2) " + format(color.YELLOW, "One at a time:") + " just " + format(color.UNDERLINE, 'press enter'))
	speed_input = format_input("\nYour choice: ")

	return check_speed(speed_input), search


def search_fast(search):
	first_loop = True

	print('\nYou are searching all at once.')

	for site_name, url in urls:
		url = url.format(search)

		if first_loop:
			webbrowser.open(url, new=1, autoraise=True)

			print("Searching {}".format(site_name), end="")
			first_loop = False
		else:
			webbrowser.open_new_tab(url)

			print(", {}".format(site_name), end="")

	print('\n\nYour search is complete. We hope you found what you were looking for!')


# helper method for search_slow(search)
def check_done(input):
	if input.lower() == 'done':
		return True
	else:
		return False


def search_slow(search):
	first_loop = True

	print("\nYou are searching one at a time.")

	print("\nPress " + format(color.UNDERLINE, "enter") + " when you are ready to search the next website. " 
			+ "\nFound what you're looking for? Type " + format(color.UNDERLINE, 'done') + " to skip remaining searches.\n")

	for site_name, url in urls:
		url = url.format(search)
		print(format(color.ITALICS, "Searching {}...".format(site_name)))

		if first_loop:
			webbrowser.open(url, new=1, autoraise=True)
			first_loop = False
		else:
			webbrowser.open_new_tab(url)

		# edge case of the last one - check if this works
		last_url = (urls[-1])[1].format(search)
		if url != last_url:
			usr_done = format_input("Continue? ")
			
			if check_done(usr_done):
				break

	print('\nYour search is complete. I hope you found what you were looking for!')


def goodbye():
	print('\n\nThank you for using' + format(color.DARKCYAN, 'Library Search') + ".")
	print('Enjoy your new read or listen!\n')


def main():
	read_file("urls.csv")

	welcome()

	while True:
		fast, search = user_input()
		if fast:
			search_fast(search)
		else:
			search_slow(search)

		print("\nType " + format(color.UNDERLINE, 'exit') + " or any character(s) to quit the program. Press " 
				+ format(color.UNDERLINE, 'enter') + " to continue.")
		exit = format_input("Input: ")
		if exit != '':
			break


	goodbye()


if __name__ == '__main__':
	main()











