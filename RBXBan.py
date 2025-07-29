# RBXBan.py

import requests, json, random, time
from bs4 import BeautifulSoup
from pystyle import Colorate, Colors, Add, Center, Write

validReports = 0

# Load fake cookies
with open("cookies.txt", "r") as f:
	cookies = [line.strip() for line in f.readlines()]

# Utilities
class Utils:
	def getCookie():
		return random.choice(cookies)

	def getRequestVerificationToken(cookie):
		response = requests.get(
			"https://www.roblox.com/build/upload",
			headers={"referer": "https://roblox.com"},
			cookies={".ROBLOSECURITY": cookie}
		)
		soup = BeautifulSoup(response.text, "html.parser")
		return soup.find("input", {"name": "__RequestVerificationToken"}).attrs["value"]

	def getOutput(amount, request):
		global validReports
		if request.status_code == 200:
			Write.Print(f"\n[{amount}] {request.status_code} | Report Success      | {request.reason}", Colors.green, interval=0)
			validReports += 1
		elif request.status_code == 429:
			Write.Print(f"\n[{amount}] {request.status_code} | Rate Limited        | {request.reason}", Colors.purple_to_red, interval=0)
			time.sleep(600)  # 10 minute cooldown
		else:
			Write.Print(f"\n[{amount}] {request.status_code} | Report Failed       | {request.reason}", Colors.purple_to_red, interval=0)

# Banner
def getBanner():
	bannerText = """
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  █▄▀█▀▄█░▄▄░█░▄▄░█▄▀█▀▄████░▄▄▀█░▄▄▀██░▀██░██░▀██░██░▄▄▄██░▄▄▀
  ███░███░▀▄░█░▀▄░███░██████░▄▄▀█░▀▀░██░█░█░██░█░█░██░▄▄▄██░▀▀▄
  █▀▄█▄▀█░▀▀░█░▀▀░█▀▄█▄▀████░▀▀░█░██░██░██▄░██░██▄░██░▀▀▀██░██░
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

Roblox Game Reporter 
meant for educational learning.
[ -x00x- ]
"""
	bannerLogo = """
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⠄⠄⠄⠄⢠⣤⣤⣄⣀⠄⠄⠄⠄⢸⣿⣿⣿⣿⡿⠿⠛⠛⠛⠿⠿⣿⣿⣇
⠄⠄⠄⠄⠈⠉⠭⠿⢿⡛⠄⠄⠄⣼⣿⣿⣿⣿⣷⣆⣀⣠⣤⣀⣤⣀⡌⢿
⠄⢀⡀⠄⠄⠄⠄⣀⣠⣆⠄⠄⢠⣿⣿⣿⣿⣿⠋⠉⠉⠉⠿⣿⢿⣿⣿⣾
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣀⣀⣀⣹⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⡿⢫⣶⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡁⠈⠉⠄⠄⠈⠛⠿⣿⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⣶⣾⣿⣷⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠛⠉⠄⠄⢀⢀⣠⣴⣿⣀⡀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠄⠄⠄⠄⠈⠘⠛⠛⠿⣿⣿⣶⣶⣦⣈⠻⣿⣿⣿⣿⣿⣿⣿
⢻⣿⣧⠄⠄⠄⠄⠄⠙⢿⣿⣷⣶⣶⣶⣶⣶⣦⣭⡉⠄⠈⣿⣿⣿⣿⣿⣿
⠈⢻⡷⠁⣤⣶⣦⣄⠄⠈⠙⠻⠿⠿⠿⠿⢿⣿⣿⣿⣄⣴⣿⣿⣿⣿⣿⣿
⣄⠄⠄⠄⠽⣿⣿⣿⣿⣶⣶⣶⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""
	return Colorate.Vertical(Colors.purple_to_blue, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)

# Report Function (Game Reporter)
def ban(victim_place_id, amount, reason, cooldown, comments):
	if amount == 0:
		amount = 999999999999999

	Write.Print(f"[>] Target Game Place ID: {victim_place_id}\n", Colors.purple_to_blue, interval=0.0025)

	for i in range(amount):
		time.sleep(cooldown)
		cookie = Utils.getCookie()
		session = requests.Session()

		# Get X-CSRF Token
		xcsrf_response = requests.post("https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": cookie})
		xcsrfToken = xcsrf_response.headers["x-csrf-token"]

		session.cookies.update({".ROBLOSECURITY": cookie})
		session.headers.update({
			"referer": "https://www.roblox.com",
			"x-csrf-token": xcsrfToken
		})

		# Get request verification token
		requestHTML = session.get("https://www.roblox.com/build/upload")
		soup = BeautifulSoup(requestHTML.text, "html.parser")
		requestVerificationToken = soup.find("input", {"name": "__RequestVerificationToken"}).attrs["value"]

		# Send report request to asset endpoint (game/place)
		reportRequest = session.post(
			f"https://www.roblox.com/abusereport/asset?id={victim_place_id}",
			data={
				"__RequestVerificationToken": requestVerificationToken,
				"ReportCategory": reason,
				"Comment": random.choice(comments),
				"Id": victim_place_id,
				"RedirectUrl": f"https://www.roblox.com/games/{victim_place_id}/",
				"PartyGuid": "",
				"ConversationId": ""
			}
		)

		Utils.getOutput(amount=i+1, request=reportRequest)

	Write.Print(f"\n\n[>] Finished Game Report Simulation.\n[>] Reports Sent: {amount}\n[>] Valid Reports: {validReports}\n\n", Colors.purple_to_blue, interval=0.0025)
	Write.Input("[>] Press Enter to Exit...", Colors.purple_to_blue, interval=0.0025)
	exit()
