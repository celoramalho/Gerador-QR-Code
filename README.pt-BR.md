# Gerador de QR Code

Um gerador de QR Codes em Python que cria códigos a partir de arquivos Excel ou links individuais. Esta ferramenta é ideal para a geração em massa de QR Codes, especialmente para links, e também permite gerar QR Codes únicos para qualquer texto ou URL.

## Funcionalidades

- **Integração com Excel**: Carrega um arquivo Excel com URLs e gera QR Codes individuais para cada link.
- **Geração de QR Code Único**: Gera um QR Code a partir de um único link ou texto fornecido.
- **Organização de Saída**: Salva os QR Codes em pastas organizadas e com nomes baseados na data e hora.

## Instalação

Clone o repositório e instale as dependências necessárias:

```bash
git clone <repository_url>
cd QR-Code-Generator
pip install -r requirements.txt


## Uso

### Arquivo Excel
Coloque seu arquivo Excel na pasta `/Planilha`. A planilha precisa ter pelo menos duas colunas com os nomes exatos:

- **Nome do QRCode**: Nome que será utilizado para salvar o QR Code.
- **Link pro QRCode**: O link que será transformado em QR Code.

#### Exemplo de uso

```python
from qr_code_generator import QRCodeGenerator

qr_gen = QRCodeGenerator()
qr_gen.generate_qr_code_excel_file()
```

### QR Code Único

Para gerar um QR Code único:

```python
qr_gen.generate_qr_code_from_link("https://www.example.com")
```

## Dependências

## Dependências

- `qrcode`: Para gerar QR Codes.
- `qrcode.image.svg`: Suporte para QR Codes no formato SVG.
- `pandas`: Para manipulação e processamento de dados.
- `numpy`: Para operações numéricas.
- `re`: Para operações com expressões regulares.
- `unicodedata`: Para normalização de texto.
- `os`: Para operações de sistema e manuseio de arquivos.
- `pathlib`: Para manipulação de caminhos de arquivos.
- `json`: Para manipulação de dados JSON.
- `datetime`: Para manipulação de datas e horários.

## Licença

Este projeto está licenciado sob a Licença MIT.