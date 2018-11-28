from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from numpy import random
import time


class Instagram_Bot:
	"""LIKE ALL THE PUPPIES!!!!"""

	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()

	def close_browser(self):
		"""close browser"""
		self.driver.close()

	def login(self):
		"""login into the chosen account"""
		driver = self.driver
		driver.get("https://www.instagram.com/accounts/login/")
		time.sleep(3)
		username_elem = driver.find_element_by_xpath("//input[@name='username']")
		username_elem.clear()
		username_elem.send_keys(self.username)

		password_elem = driver.find_element_by_xpath("//input[@name='password']")
		password_elem.clear()
		password_elem.send_keys(self.password)
		password_elem.send_keys(Keys.RETURN)
		time.sleep(3)

	def navigate_photos(self, hashtag, humanizer, comment):
		"""opens the pictures of a given hashtag and performs wanted actions"""
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
		time.sleep(3)

		# scroll down to load a set of pictures
		for i in range(1, 3):
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(3)

		# searching for picture links
		hrefs = driver.find_elements_by_tag_name('a')
		pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
		pic_hrefs =[href for href in pic_hrefs if "/p/" in href]
		print(hashtag + ' photos; ' + str(len(pic_hrefs)))

		for pic_href in pic_hrefs:
			driver.get(pic_href)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			if humanizer:
				print("Ran humanizer")
				if random.choice([True, False], p=(0.65, 0.35)):
					time.sleep(random.choice(list(range(2, 5))))
					self.like_and_comment(driver, comment)
					# sleep time of 18 results in aprox. 200 Likes per hour
					time.sleep(random.choice(list(range(1, 5))))

				# skip a picture
				else:
					time.sleep(random.choice(list(range(3, 20))))
					continue

			else:
				time.sleep(2)
				self.like_and_comment(driver, comment)
				time.sleep(5)

	@staticmethod
	def like_and_comment(driver, comment):
		"""find and click likebutton, skip if already liked, comment if comment"""
		try:
			# only looks for pictures that arent already liked by your account
			like = driver.find_element_by_css_selector('.glyphsSpriteHeart__outline__24__grey_9.u-__7')
			like.click()

			if comment:
				time.wait(2)
				commentfield = driver.find_element_by_class_name('Ypffh')
				commentfield.click()
				commentfield = driver.find_element_by_class_name('Ypffh')
				commentfield.send_keys(comment)
				commentfield.send_keys(Keys.RETURN)

		# Element can't be found if already liked so skip it
		except NoSuchElementException as alreadyliked:
			pass


