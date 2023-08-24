from os import getenv
from dotenv import load_dotenv
from google.cloud import texttospeech
from PyPDF2 import PdfReader

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = getenv("GOOGLE_APPLICATION_CREDENTIALS")

def extract_text_from_pdf(pdf_path):
    """
    Extract text from the first page of a given PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the first page of the PDF.
    """
    # Create a PDF reader object for the given PDF path.
    reader = PdfReader(pdf_path)

    # Initialize an empty string to store the text from all pages.
    text = ""

    # Iterate over each page in the PDF.
    for page in reader.pages:
        # Extract text from the current page and append it to the text variable.
        text += page.extract_text()

    # Extract and return text from the first page.
    return text

def convert_text_to_speech(text):
    """
    Convert a given text to speech using Google's Text-to-Speech API.
    
    Args:
        text (str): Text to be converted to speech.
    
    Returns:
        bytes: Audio data in MP3 format.
    """
    # Create a Text-to-Speech client to interact with the Google API.
    client = texttospeech.TextToSpeechClient()

    # Define the input text for the Text-to-Speech API.
    input_text = texttospeech.SynthesisInput(text=text)
    
    # Define the voice parameters, including language and gender.
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    
    # Define the audio output configuration, setting the format to MP3.
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    
    # Use the client to synthesize the speech and store the response.
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    # Return the audio data from the response.
    return response.audio_content

def save_audio_to_file(audio_data, filename):
    """
    Save the provided audio data to a file.
    
    Args:
        audio_data (bytes): Audio data to be saved.
        filename (str): Name of the file where the audio data should be saved.
    """
    # Open the file in binary write mode and save the audio data.
    with open(filename, 'wb') as out:
        out.write(audio_data)

def main():
    """
    Main function to extract text from a PDF, convert it to speech, and save it as an MP3 file.
    """
    # Extract text from the specified PDF.
    text = extract_text_from_pdf(input("Enter the name of the pdf file you want to convert to audio (filename.pdf): "))

    # Convert the extracted text to speech.
    audio_data = convert_text_to_speech(text)

    # Save the audio data to an MP3 file.
    save_audio_to_file(audio_data, "output.mp3")

    # Print a success message.
    print("Audio has been saved to output.mp3!")

# If this script is being run as the main module, execute the main function.
if __name__ == "__main__":
    main()
