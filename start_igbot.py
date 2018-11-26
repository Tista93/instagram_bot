from instabot import Instagram_bot
import argparse
from selenium.common.exceptions import NoSuchWindowException, WebDriverException

def main():

	# create argparser for commandline argument parsing
	parser = argparse.ArgumentParser(description="A simple instagram like-bot based on selenium")
	parser.add_argument('username', type=str, help='IG Username')
	parser.add_argument('password', type=str, help='IG Password')
	parser.add_argument('hashtag', type=str, help='Hashtag')
	arguments = parser.parse_args()

	instabot = Instagram_bot(arguments.username, arguments.password)

	instabot.login()
	try:
		instabot.like_photo(arguments.hashtag)

	except(NoSuchWindowException, WebDriverException) as prematurely_closed:
		print("Program has been prematurely closed!")


if __name__ == '__main__':
	main()
	print("DONE")
