# import whois
from whois import whois

# masukkan input
data = input("Masukkan Domain Untuk WHOIS: ")
whoisLookup = whois(data)

# Result WHOIS
print(whoisLookup.text)
