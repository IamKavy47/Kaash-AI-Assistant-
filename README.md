
# Kaash - Your Personal AI Assistant

Kaash is a Python-based desktop AI assistant that offers a seamless blend of automation, conversational abilities, real-time search engine functionality, text-to-speech (TTS), speech-to-text (STT), and a user-friendly GUI. With its advanced features and modular design, Kaash can enhance productivity and simplify daily tasks.

## Features

### 1. Automation
- **Web Automation**: Perform web-based tasks such as searching, form-filling, and more.
- **Application Control**: Open and close applications seamlessly.
- **System Automation**: Control system settings like volume adjustment and file handling.
- **Notepad Automation**: Write and save notes or letters directly into Notepad.

### 2. Conversational Abilities
- Chat with Kaash for assistance, advice, or casual conversation through the integrated chatbot powered by advanced AI models.

### 3. Real-Time Search Engine
- Perform real-time searches directly from the assistant and get accurate results instantly.

### 4. Text-to-Speech (TTS) and Speech-to-Text (STT)
- Convert text into natural-sounding speech with TTS.
- Recognize and process voice commands using STT for a hands-free experience.

### 5. Graphical User Interface (GUI)
- An interactive and user-friendly GUI developed in Python, allowing easy access to all functionalities.

## File Structure

'''
├── .env               # Configurations (username, assistant name, API keys, etc.)
├── Main.py            # Entry point for the application
├── requirements.txt   # Dependencies
├── Backend/
│   ├── Automation.py  # Handles automation features
│   ├── Chatbot.py     # AI conversation engine
│   ├── ImageGeneration.py  # AI-based image generation
│   ├── Model.py       # Backend model logic
│   ├── Realtimesearchengine.py  # Real-time search logic
│   ├── stt.py         # Speech-to-text processing
│   └── tts.py         # Text-to-speech processing
├── Frontend/
│   ├── gui.py         # GUI implementation
│   ├── Files/         # Contains required data files
│   └── graphics/      # Stores GUI components
'''

## Environment Variables

The `.env` file includes the following configurations:
- `HuggingFaceAPIKey`: API Key for Hugging Face models.
- `CohereAPIKey`: API Key for Cohere.
- `GroqAPIKey`: API Key for Groq.
- `Username`: User's name.
- `AssistantName`: The name of the assistant (Kaash).
- `InputLanguage`: Preferred input language for the assistant.
- `AssistantVoice`: Voice type for TTS.

## Requirements

To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository.
2. Configure the `.env` file with your API keys and settings.
3. Run the assistant using:
```bash
python Main.py
```

## License

This project is licensed under the MIT License. Feel free to customize and use it as per your requirements.