# =============================================================================
#  File: userlist_generator.py
#  Author: Dalton Knapp
#  Description: Rewrites a csv file to match formatting for FreeRADIUS and generates PPSK’s.
#  Created: 2025-06-10
#  License: MIT
# =============================================================================
import os, sys, requests, csv, string, secrets


users = []
accounts = []

def get_users():
	users = []
	try:
		with open("users.py", "r") as f:
			reader = csv.reader(f)
			for row in reader:
				first = row[0].strip()
				last = row[1].strip()
				line = first + "." + last
				line = line.lower()
				users.append(line)
			return users
	except FileNotFoundError as e:
		print("Error reading file.")
		raise e

def generate_ppsk(length=12):
	characters = string.ascii_letters
	string.digits + "!@#S%^&*()-_=+[]{}"
	return "".join(secrets.choice(characters) for _ in range(length))

def create_csv(data):
	with open('accounts.py', mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(data)

def setup_accounts(users):
	accounts = []
	for user in users:
		ppsk = generate_ppsk()
		accounts.append([user, ppsk])
	for account in accounts:
		print(account)
	return accounts


# ----------------------- #

###

if __name__ == "__main__":
	if len(sys.argv) > 1:
		if "--setup-accounts" in sys.argv or "-s" in sys.argv:
			users = get_users()
			accounts = setup_accounts(users)
			create_csv(accounts)
		elif "--generate-ppsk" in sys.argv or "-g" in sys.argv:
			new_ppsk = generate_ppsk()
			print("New ppsk:")
			print(new_ppsk)
		else:
			print("You can reference the README.md if unsure about use of this script.")