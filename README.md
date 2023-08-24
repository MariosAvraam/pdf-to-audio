# PDF to Audio Converter

A simple Python script that extracts text from a PDF and converts it into an audio (MP3) format using Google's Text-to-Speech API.

## Prerequisites

- **Python 3.x**
- A **Google Cloud account** with Text-to-Speech API enabled and a service account key generated (in JSON format).
- A `.env` file containing the path to your Google Cloud service account key, set as `GOOGLE_APPLICATION_CREDENTIALS`.

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MariosAvraam/pdf-to-audio.git
```

### 2. Navigate to the directory
```bash
cd pdf-to-audio
```

### 3. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install Required Packages
```bash
pip install -r requirements.txt
```

### 5. Set Up Your .env File
Create a `.env` file in the root directory of the project. Add the path to your Google Cloud service account key:

```bash
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service/account/key.json
```

## Usage

1. Follow the prompts and wait for the script to generate the output.mp3 file.
2. Listen to the generated audio file!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT