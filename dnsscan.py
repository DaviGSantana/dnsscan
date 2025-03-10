import dnsclass
import sys

dns = dnsclass.Dnsscan

if len(sys.argv) < 4:
    print("Uso: python dnsscan.py <opção> <domínio> <wordlist>")
    sys.exit(1)

try:
    if len(sys.argv) == 1:
        dns.help()
except IndexError:
    None

dominio = sys.argv[2]
wordlist = sys.argv[3]

if sys.argv[1] == "-s":
    dns.subdomainBF(dominio, wordlist)
elif sys.argv[1] == "-c":
    dns.cnamecheck(dominio, wordlist)
else:
    dns.help()
