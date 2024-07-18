# backend

## Getting Started

### Prerequisites

1. Setup your Python virtual environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
1. Install tesseract
   - `brew install tesseract`
   - `apt-get install tesseract-ocr`
   - Or see [instructions](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file#installing-tesseract)

## Run

```bash
flask --app dog_stuff run
```
