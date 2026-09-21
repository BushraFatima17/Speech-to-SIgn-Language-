# Speech-to-Sign Language

A Python prototype that converts spoken words into visual sign-language sequences. The application listens through a microphone, uses Google Speech Recognition to transcribe speech, and displays images for each letter of every recognized word.

## How It Works

1. Captures audio from the system microphone.
2. Adjusts for ambient noise before listening.
3. Transcribes speech with Google Speech Recognition.
4. Splits the recognized text into words.
5. Loads one sign image for each letter from the corresponding dataset folder.
6. Combines the letter images horizontally and displays the resulting visual sequence.

Say **`exit`** to stop the application after the current speech input has been processed.

## Project Structure

```text
FYP/
├── S_to_S.py       # Main speech-to-sign-language script
└── README.md       # Project documentation
```

## Requirements

- Python 3.8 or later
- A working microphone
- Internet access for Google Speech Recognition
- A sign-image dataset organized by alphabet letter

Install the Python dependencies with:

```bash
pip install opencv-python matplotlib SpeechRecognition PyAudio
```

### Installing PyAudio

If `pip install PyAudio` fails on Windows, install a compatible PyAudio wheel or use a package manager such as `pipwin`:

```bash
pip install pipwin
pipwin install pyaudio
```

On Linux, install the PortAudio development package before installing PyAudio:

```bash
sudo apt-get update
sudo apt-get install portaudio19-dev python3-pyaudio
```

## Dataset Setup

The script expects a directory containing one subdirectory for each letter used in the recognized words:

```text
sign_dataset/
├── A/
│   └── sign_a.jpg
├── B/
│   └── sign_b.jpg
├── C/
│   └── sign_c.jpg
└── ...
```

Each letter folder should contain at least one readable image. The script currently uses the first file returned from each folder.

Before running the program, update `dataset_path` in `S_to_S.py` to the location of your dataset. The current value is a machine-specific Windows search path and must be replaced on another computer.

For example:

```python
dataset_path = r"C:\path\to\sign_dataset"
```

## Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/BushraFatima17/FYP.git
   cd FYP
   ```

2. Configure `dataset_path` in `S_to_S.py`.

3. Install the dependencies.

4. Start the application:

   ```bash
   python S_to_S.py
   ```

5. Speak clearly when prompted. The recognized words will be displayed as sign-letter image sequences.

## Limitations

- The project displays fingerspelling-style letter images rather than complete word-level sign-language videos or grammatical signs.
- Speech recognition uses Google's online service, so an internet connection is required.
- Recognition accuracy depends on microphone quality, background noise, pronunciation, and network availability.
- Words containing punctuation or characters without matching dataset folders may not be processed completely.
- Only the first image found in each letter folder is displayed.
- The dataset path is currently hard-coded and should be made configurable for production use.

## Future Improvements

- Replace the hard-coded dataset path with a command-line option or configuration file.
- Add a requirements file for reproducible installation.
- Support multiple images, animations, or videos for each sign.
- Add a graphical user interface with playback controls.
- Improve handling of punctuation, missing letters, and repeated words.
- Add offline speech-recognition support.
- Support complete sign-language vocabulary and sentence structure.

## License

No license has been specified for this project yet. Add a license before distributing or reusing the code.
