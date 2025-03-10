import socket
import json
import time
import dns.resolver

class Dnsscan:

	def help():
		print(f"Modo de uso: python3 dnsscan.py [-s/-c [subdominio/cname]] exemplo.com wordlist.txt")

	def cnamecheck(dominio, wlist):
		cname_dict = {}


		with open(wlist) as f:
			for i in f.readlines():
				i = i.replace("\n", "")
				subdominio = f"{i}.{dominio}"

				while True:
					try:
						resposta = dns.resolver.resolve(subdominio, "CNAME")
						cname = str(resposta[0].target)
						cname_dict[subdominio] = cname
						print(f"{subdominio} tem um alias {cname}")
						break

					except dns.resolver.NoAnswer:
						break
					except dns.resolver.NXDOMAIN:
						break
					except dns.resolver.LifetimeTimeout:
						time.sleep(3)
		cname_json = json.dumps(cname_dict)
		with open(f"{dominio}-cname.json", "w") as f:
			f.write(cname_json)
		print(f"Arquivo JSON {dominio}-cname.json criado.")

	def subdomainBF(dominio, wlist):

		def DNSipv4(dominio_sub):
			try:
				dados = socket.getaddrinfo(dominio_sub, None, socket.AF_INET)
				addr = dados[2][4][0]

				print(f"[!] {dominio_sub} - {dados[2][4][0]}")
				return addr
			except socket.gaierror:
				return 0
		def DNSipv6(dominio_sub):
			try:
				dados = socket.getaddrinfo(dominio_sub, None, socket.AF_INET6)
				print(f"Resposta ipv6 {dominio_sub}: {dados}")
				addr = dados[2][4][0]

				print(f"[!] {dominio_sub} - {dados[2][4][0]}")
				return addr
			except socket.gaierror:
				return 0

		consultado = []

		dominios6 = {}
		dominios4 = {}
		dominios = {}

		with open(wlist) as wordlist:
			for i in wordlist.readlines():
				i = i.replace("\n", "")
				dominio_sub = f"{i}.{dominio}"

				if dominio_sub not in consultado:
					addr4 = DNSipv4(dominio_sub)
					addr6 = DNSipv6(dominio_sub)
					if addr6 != 0:
						dominios6[dominio_sub] = addr6
					if addr4 != 0:
						dominios4[dominio_sub] = addr4
					consultado.append(dominio_sub)
		dominios["ipv4"] = dominios4
		dominios["ipv6"] = dominios6

		dominios_json = json.dumps(dominios)
		with open(f"{dominio}-subdomains.json", "w") as f:
			f.write(dominios_json)
		print(f"Arquivo{dominio}-subdomain-json criado.")
