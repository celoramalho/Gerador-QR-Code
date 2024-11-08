# QR Code Generator
[Read in Portuguese](README.pt-BR.md)

A Python-based QR Code generator that creates codes from Excel files or individual links. This tool is ideal for batch QR Code generation, especially for links, and also allows generating unique QR Codes for any text or URL.

## Features

- **Excel Integration**: Loads an Excel file with URLs and generates individual QR Codes for each link.
- **Single QR Code Generation**: Generates a QR Code from a single provided link or text.
- **Output Organization**: Saves QR Codes in organized folders with names based on date and time.

## Installation

Clone the repository and install the necessary dependencies:

```bash
git clone <repository_url>
cd QR-Code-Generator
pip install -r requirements.txt
```

## Usage

### Excel File
Place your Excel file in the `/Planilha` folder. The spreadsheet must have at least two columns with the exact names:

- **QRCode Name**: The name that will be used to save the QR Code.
- **QRCode Link**: The link that will be transformed into a QR Code.

#### Example Usage

```python
from qr_code_generator import QRCodeGenerator

qr_gen = QRCodeGenerator()
qr_gen.generate_qr_code_excel_file()
```

### Single QR Code

To generate a single QR Code:

```python
qr_gen.generate_qr_code_from_link("https://www.example.com")
```

## Dependencies

- `qrcode`: To generate QR Codes.
- `qrcode.image.svg`: Support for QR Codes in SVG format.
- `pandas`: For data manipulation and processing.
- `numpy`: For numerical operations.
- `re`: For regular expression operations.
- `unicodedata`: For text normalization.
- `os`: For system operations and file handling.
- `pathlib`: For file path management.
- `json`: For handling JSON data.
- `datetime`: For date and time manipulation.

## License

This project is licensed under the MIT License.