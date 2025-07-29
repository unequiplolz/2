# main.py

import RBXBan as RB
from pystyle import Write, Colors

print(RB.getBanner())

reasons = {
    1: {"reason": "Inappropriate Language - Profanity & Adult Content", "comments": ["game has offensive words"]},
    2: {"reason": "Asking for or Giving Private Information", "comments": ["game asks for my password"]},
    3: {"reason": "Bullying, Harassment, Discrimination", "comments": ["game has harassment content"]},
    4: {"reason": "Dating", "comments": ["game has online dating"]},
    5: {"reason": "Exploiting, Cheating, Scamming", "comments": ["game encourages exploits"]},
    6: {"reason": "Account Theft - Phishing, Hacking, Trading", "comments": ["game has phishing links"]},
    7: {"reason": "Inappropriate Content - Place, Image, Model", "comments": ["NSFW content in game"]},
    8: {"reason": "Real Life Threats & Suicide Threats", "comments": ["threats in game chat"]},
    9: {"reason": "Other rule violation", "comments": ["general rule breaking"]}
}

victim_place_id = Write.Input("[?] Target Game Place ID: ", Colors.purple_to_blue, interval=0.0025)
amount          = int(Write.Input("[?] Report Amount (0=inf): ", Colors.purple_to_blue, interval=0.0025))
reason_id       = int(Write.Input("[?] Reason for Report (1-9): ", Colors.purple_to_blue, interval=0.0025))
cooldown        = int(Write.Input("[?] Cooldown (seconds): ", Colors.purple_to_blue, interval=0.0025))

if amount == 0:
	Write.Print(f"\n[>] Reporting game {victim_place_id} infinitely for reason {reason_id}...\n", Colors.purple_to_blue, interval=0.0025)
else:
	Write.Print(f"\n[>] Reporting game {victim_place_id} {amount} times for reason {reason_id}...\n", Colors.purple_to_blue, interval=0.0025)

RB.ban(
	victim_place_id,
	amount,
	reasons[reason_id]["reason"],
	cooldown,
	reasons[reason_id]["comments"]
)
