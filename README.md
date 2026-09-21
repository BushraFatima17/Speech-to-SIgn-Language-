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

## Demo Video

https://github.com/user-attachments/assets/fcea4dee-4ac5-46ee-85fb-aa836912db8e

## Project Structure

```text
FYP/
├── Speech_to_Sign.py       # Main speech-to-sign-language script
├── ASL_Dataset/    # Dataset folder for ASL images (0-9 digits and A-Z alphabets)
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
ASL_dataset/
├── A/
│   └── sign_a.jpg
├── B/
│   └── sign_b.jpg
├── C/
│   └── sign_c.jpg
└── ...
```

You can download the dataset from here
"https://www.kaggle.com/datasets/ayuraj/asl-dataset"

Each letter folder should contain at least one readable image. The script currently uses the first file returned from each folder.

Before running the program, update `dataset_path` in `Speech_to_Sign.py` to the location of your dataset. The current value is a machine-specific Windows search path and must be replaced on another computer.

For example:

```python
dataset_path = r" "  #Add the path of the dataset
```

## Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/BushraFatima17/FYP.git
   cd FYP
   ```

2. Configure `dataset_path` in `Speech_to_Sign.py`.

3. Install the dependencies.

4. Start the application:

   ```bash
   python Speech_to_Sign.py
   ```

5. Speak clearly when prompted. The recognized words will be displayed as sign-letter image sequences.

## Results
<img width="2929" height="798" alt="Hello picture" src="https://github.com/user-attachments/assets/6db08999-6b66-40e5-820a-ef9a20ee696e" />

<img width="4391" height="505" alt="Presentation_picture" src="https://github.com/user-attachments/assets/eef9759c-2c9f-43fc-99f4-f4b89f271fc6" />

## Limitations

- Speech recognition uses Google's online service, so an internet connection is required.
- Recognition accuracy depends on microphone quality, background noise, pronunciation, and network availability.

## Future Improvements

- Support multiple images, animations, or videos for each sign.
- Add offline speech-recognition support.
- Support complete sign-language vocabulary and sentence structure.
- Introduce datasets for Urdu language, enabling text-to-sign conversion for diverse linguistic communities.


