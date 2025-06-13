import os, sys, string, secrets


entry_template = """username Cleartext-Password := "password"
		Reply-Message := "Welcome to the network!"
"""

class Generate:
	def __init__(self, path="./users.txt"):
		self.path = path
	
	def generate(self):
		users = self.get_users()
		accounts = self.setup_accounts(users)
		self.write_userfile(accounts)

	def generate_ppsk(self, length=12):
		characters = string.ascii_letters + string.digits + "!@#S%^&*()-_=+[]{}"
		return "".join(secrets.choice(characters) for _ in range(length))
	
	def get_users(self):
		users = []
		try:
			with open(self.path, "r") as f:
				for line in f:
					line = line.replace(" ", ".")
					line = line.lower()
					line = line.strip()
					users.append(line)
			return users
		except e:
			print("Error reading file.")
			raise e
	
	def setup_accounts(self, users):
		accounts = []
		for user in users:
			accounts.append(entry_template.replace("username", user).replace("password", generate_ppsk()))
		for account in accounts:
			print(account)
		return accounts
	
	def write_userfile(self, accounts):
		with open("./authorize", "w") as f:
			f.writelines(accounts)

if __name__ == "__main__":
	g = Generate()
	g.generate()