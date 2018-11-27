## A simple Instagram like-bot implemented in Python 3
**  **
######     NOTE: You'll need [Selenium](https://selenium-python.readthedocs.io), [Geckodriver](https://github.com/mozilla/geckodriver/releases) and the webbrowser Mozilla Firefox to make this work.
######     As you can see for yourself - this is save. It won't store your data. 
######     However please note that this programm is solely made for learning and testing purposes. I am not liable for any problems with your accounts.




**  ** 
**Well, how does it work?**

This little program opens your firefox browser autonomously - searches for the disered hashtag you entered and then proceeds to like those 
pictures for you. This will go on until you close the browser.
This is of course not as efficent as working with the instagram api - but it is better in avoiding shadowbans (especialy with the
humanizer option running).

**How do I run it?**
1. Make sure you have all of the necessary stuff linked above installed
2. Open your CMD/Shell in the folder you place this project in
3. To start the programm, type ***py start_igbot username password hashtag*** 
4. You can add a humanizer flag if you want to. This will simulate human behaviour like skipping pictures or
   "looking" at a picture for a random duration before liking it.
   To do that, just enter the parameter ***True*** at the end
  


  
