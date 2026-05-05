import requests
import hashlib

print()
print("🔍 HAVE I BEEN PWNED")
print("checks if your password was leaked in a data breach")
print("-" * 40)
print()

password= input("enter your password: ")

sha1= hashlib.sha1(password.encode()).hexdigest().upper()

prefix= sha1[:5]
suffix= sha1[5:]

url= f"https://api.pwnedpasswords.com/range/{prefix}"
response= requests.get(url)

if suffix in response.text:
	for line in response.text.splitlines():
		if line.startswith(suffix):
			count= line.split(":")[1]
			print()
			print(f"💀 oh no... found in {count} data breaches")
			print("hackers have had this password for years. change it NOW.")
			break

else:
	print()
	print("✅ not found in any known breaches")
	print("okay you're safe... for now 👀")

print()
