import os, sys, string, secrets
import subprocess

entry_template = """username Cleartext-Password := "password"
		Reply-Message := "Welcome to the network!"
"""

infile = "/etc/freeradius/3.0/mods-config/files/authorize"
outfile = "/tmp/authorize"

class Generate:
	def __init__(self, path="./users.txt"):
		self.path = path
		self.users = []
		self.accounts = []
	
	def generate(self):
		users = self.get_users()
		accounts = self.setup_accounts(users)
		self.write_userfile(accounts)

	def generate_ppsk(self, length=12):
		characters = string.ascii_letters + string.digits + "!@#S%^&*()-_=+[]{}"
		return "".join(secrets.choice(characters) for _ in range(length))
	
	def get_users(self):
		self.users.clear()
		users = []
		try:
			with open(self.path, "r") as f:
				for line in f:
					line = line.replace(" ", ".")
					line = line.lower()
					line = line.strip()
					users.append(line)
			self.users = users.copy()
			return users
		except e:
			print("Error reading file.")
			raise e
	
	def setup_accounts(self):
		self.accounts.clear()
		accounts = []
		for user in self.users:
			accounts.append(entry_template.replace("username", user).replace("password", self.generate_ppsk()))
		for account in accounts:
			print(account)
		self.accounts = accounts.copy()
		return accounts
	
	def write_userfile(self):
		with open(outfile, "w") as f:
			f.writelines(self.accounts)
		subprocess.run(["sudo", "mv", outfile, infile])


class Reissue:
	def __init__(self, generator=class):
		self.g = generator
		self.account = None
	
	def get_accounts(self):
		with open(infile, "r") as f:
			accounts = []
			for line in f:
				if line.startswith("\t\t"):
					continue
				accounts.append(line)
		return accounts

	def find_user(self, name):
		name = name.replace(" ", ".")
		name = name.lower()
		name = name.strip()
		accounts = self.get_accounts()
		found = None
		for account in accounts:
			if name in account:
				found = account
		if not found:
			raise ValueError()
		self.account = account
		return account

	def replace_ppsk(self, username, account=None):
		if not account:
			account = self.account
		ppsk = self.g.generate_ppsk()
		print(f"User '{username}' now has password '{ppsk}'")
		with open(infile, "r") as inputfile, open(outfile, "w") as outputfile:
			for line in inputfile:
				if line.startswith(username + " "):
				 line = re.sub(r'"[^"]*"', f'"{ppsk}"', line)
				outputfile.write(line)
		subprocess.run(["sudo", "mv", outfile, infile])

###

if __name__ == "__main__":
	g = Generate()
	g.generate()