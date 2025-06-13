import os, sys, string, secrets


entry_template = """username Cleartext-Password := "password"
		Reply-Message := "Welcome to the network!"
"""

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
		with open("./authorize", "w") as f:
			f.writelines(self.accounts)


class Reissue:
	def __init__(self, generator=class):
		self.g = generator

	def find_user(self, name):
		for user in self.g.users:

if __name__ == "__main__":
	g = Generate()
	g.generate()