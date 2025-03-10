
# Dnsscan

**Dnsscan** é uma ferramenta simples para realizar scans de subdomínios e CNAMEs de um domínio específico. Ele permite buscar subdomínios com base em uma wordlist personalizada e também obter os alias (CNAME) dos subdomínios encontrados. Os resultados são gravados em um arquivo de log no formato `.json`, contendo informações detalhadas sobre os subdomínios e os IPs encontrados.

## Funcionalidades

- **Scan de Subdomínios**: Busca por subdomínios de um domínio específico usando uma wordlist personalizada.
- **Scan de CNAME**: Encontra os alias (CNAME) dos subdomínios descobertos.
- **Resultados em JSON**: Gera um arquivo de log `.json` com os resultados detalhados de cada operação, incluindo IPs (IPv4 e IPv6).

## Requisitos

- Python 3
- Bibliotecas necessárias:
  - `requests`
  - `dns.resolver`

Você pode instalar as dependências necessárias executando o seguinte comando:

```bash
pip install dnspython
```

## Como Usar

O script `dnsscan.py` oferece duas opções principais de uso: `-s` para scan de subdomínios e `-c` para scan de CNAME. 

### 1. Scan de Subdomínios

Para realizar um scan de subdomínios de um domínio, execute o comando abaixo. Ele usa uma wordlist para tentar encontrar subdomínios e retorna os subdomínios encontrados, junto com os IPs correspondentes (IPv4 e IPv6). 

#### Sintaxe:

```bash
python dnsscan.py -s exemplo.com wordlist/subdomains-top1million-5000.txt
```

- `-s`: Realiza o scan de subdomínios.
- `exemplo.com`: O domínio para o qual deseja realizar o scan.
- `wordlist/subdomains-top1million-5000.txt`: A wordlist que será utilizada para tentar descobrir os subdomínios. O repositório já inclui duas wordlists populares.

#### Exemplo:

```bash
python dnsscan.py -s exemplo.com wordlist/sub.txt
```

Após a execução, o script irá gerar um arquivo `resultado_subdominios.json` com os subdomínios encontrados e seus respectivos IPs (IPv4 e IPv6).

### 2. Scan de CNAME

Para realizar um scan de CNAME, basta executar o seguinte comando:

#### Sintaxe:

```bash
python dnsscan.py -c exemplo.com wordlist/sub.txt
```

- `-c`: Realiza o scan de CNAME para os subdomínios encontrados.
- `exemplo.com`: O domínio para o qual deseja realizar o scan.
- `wordlist/sub.txt`: A wordlist que será utilizada para tentar descobrir os subdomínios.

#### Exemplo:

```bash
python dnsscan.py -c exemplo.com wordlist/sub.txt
```

Esse comando retornará os alias (CNAMEs) dos subdomínios encontrados, e também gerará um arquivo `resultado_cname.json` com as informações.

## Saída

Após o scan de subdomínios ou CNAME, um arquivo de log no formato `.json` será gerado. Exemplo de um arquivo de log:


## Contribuindo

Se você encontrar algum erro ou desejar melhorar a ferramenta, sinta-se à vontade para abrir uma *issue* ou submeter um *pull request*. Todas as contribuições são bem-vindas!
