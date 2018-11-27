from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from numpy import random
import time



class Instagram_bot:
	"""LIKE ALL THE PUPPIES!!!!"""

	def __init__(self, username, password, humanizer):
		self.username = username
		self.password = password
		self.driver = webdriver.Firefox()
		self.humanizer = humanizer

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

	def like_photo(self, hashtag, humanizer):
		"""like a picture"""
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
				if random.choice([True, False], p=(0.65, 0.35)):
					time.sleep(random.choice(list(range(2, 5))))
					self.click_like(driver)
					# sleep time of 18 results in aprox. 200 Likes per hour
					time.sleep(random.choice(list(range(3, 20))))
					#time.sleep(5)

				else:
					time.sleep(random.choice(list(range(3, 20))))
					#time.sleep(5)
					continue

			else:
				time.sleep(2)
				self.click_like(driver)
				time.sleep(5)

	@staticmethod
	def click_like(driver):
		"""finds like button, clicks it, skips already liked pictures"""
		try:
			# only looks for pictures that arent already liked by your account
			like = driver.find_element_by_css_selector('.glyphsSpriteHeart__outline__24__grey_9.u-__7')
			like.click()

		# Element can't be found if already liked
		except NoSuchElementException as alreadyliked:
			pass

