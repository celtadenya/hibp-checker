# 🔍 HIBP Password Checker

checks if your password has been leaked in a data breach.
no account needed. no password ever leaves your device.

## How It Works

your password never gets sent anywhere. the script hashes it
locally using SHA1, sends only the first 5 characters to the
API, and checks the results. your actual password stays on
your machine the whole time.

## How to Run

pip3 install requests
python3 checker.py

## Example

enter your password: 123456

💀 found in 209972844 data breaches
hackers have had this password for years. change it NOW.

---

enter your password: hj£$kl2309fwef

✅ not found in any known breaches
okay you're safe... for now 👀

## Built With

python3 + haveibeenpwned.com API (free, no key needed)
