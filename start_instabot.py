from instagrambot import Instagram_Bot
import argparse
from selenium.common.exceptions import NoSuchWindowException, WebDriverException, InvalidSessionIdException

def main():

	# exceptions
	exceptions = (NoSuchWindowException, WebDriverException, InvalidSessionIdException)
	# create argparser for commandline argument parsing
	parser = argparse.ArgumentParser(description="A simple instagram like-bot based on selenium")
	parser.add_argument('username', type=str, help='IG Username')
	parser.add_argument('password', type=str, help='IG Password')
	parser.add_argument('hashtag', type=str, help='Hashtag')
	parser.add_argument('--humanizer', type=bool, nargs='?', help='Sim. human behaviour')
	parser.add_argument('--comment', type=str, nargs='+', help='"Comment you want to post"')
	arguments = parser.parse_args()

	print(arguments)

	instabot = Instagram_Bot(arguments.username, arguments.password)

	instabot.login()
	try:
		instabot.navigate_photos(arguments.hashtag, arguments.humanizer, arguments.comment)

	# this is just temporary.
	except exceptions:
		print("Program has been prematurely closed!")

	instabot.close_browser()


if __name__ == '__main__':
	main()
	print("DONE")