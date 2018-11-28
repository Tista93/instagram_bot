from instagrambot import Instagram_Bot

tester = Instagram_Bot('crazy_dog_sir', 'FuchsBau1993!')
tester.login()
tester.navigate_photos('puppie', False, 'Wow cute!')
tester.close()
