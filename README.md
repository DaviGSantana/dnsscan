Dnsscan

Dnsscan é uma ferramenta simples para realizar scans de subdomínios e CNAMEs de um domínio específico. Ele permite buscar subdomínios com base em uma wordlist personalizada e também obter os alias (CNAME) dos subdomínios encontrados. Os resultados são gravados em um arquivo de log no formato .json, contendo informações detalhadas sobre os subdomínios e os IPs encontrados.
Funcionalidades

    Scan de Subdomínios: Busca por subdomínios de um domínio específico usando uma wordlist personalizada.
    Scan de CNAME: Encontra os alias (CNAME) dos subdomínios descobertos.
    Resultados em JSON: Gera um arquivo de log .json com os resultados detalhados de cada operação, incluindo IPs (IPv4 e IPv6).

Requisitos

    Python 3.x
    Bibliotecas necessárias:
        requests
        dns.resolver

Você pode instalar as dependências necessárias executando o seguinte comando:

pip install -r requirements.txt

Como Usar

O script dnsscan.py oferece duas opções principais de uso: -s para scan de subdomínios e -c para scan de CNAME.
1. Scan de Subdomínios

Para realizar um scan de subdomínios de um domínio, execute o comando abaixo. Ele usa uma wordlist para tentar encontrar subdomínios e retorna os subdomínios encontrados, junto com os IPs correspondentes (IPv4 e IPv6).
Sintaxe:

python dnsscan.py -s exemplo.com wordlist/sub.txt

    -s: Realiza o scan de subdomínios.
    exemplo.com: O domínio para o qual deseja realizar o scan.
    wordlist/sub.txt: A wordlist que será utilizada para tentar descobrir os subdomínios. O repositório já inclui duas wordlists populares.

Exemplo:

python dnsscan.py -s exemplo.com wordlist/sub.txt

Após a execução, o script irá gerar um arquivo resultado_subdominios.json com os subdomínios encontrados e seus respectivos IPs (IPv4 e IPv6).
2. Scan de CNAME

Para realizar um scan de CNAME, basta executar o seguinte comando:
Sintaxe:

python dnsscan.py -c exemplo.com wordlist/sub.txt

    -c: Realiza o scan de CNAME para os subdomínios encontrados.
    exemplo.com: O domínio para o qual deseja realizar o scan.
    wordlist/sub.txt: A wordlist que será utilizada para tentar descobrir os subdomínios.

Exemplo:

python dnsscan.py -c exemplo.com wordlist/sub.txt

Esse comando retornará os alias (CNAMEs) dos subdomínios encontrados, e também gerará um arquivo resultado_cname.json com as informações.
