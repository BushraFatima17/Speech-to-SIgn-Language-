import cv2
import os
import matplotlib.pyplot as plt
import speech_recognition as sr

dataset_path = r"search-ms:displayname=Search%20Results%20in%20OneDrive%20-%20Higher%20Education%20Commission&crumb=location:C%3A%5CUsers%5CWhizz%5COneDrive%20-%20Higher%20Education%20Commission\Speech to sign"

def process_word(word):
    combined_image = None
    for letter in word.upper():
        letter_folder = os.path.join(dataset_path, letter)
        if not os.path.exists(letter_folder):
            print(f"Folder not found for letter: {letter}")
            continue
        letter_files = os.listdir(letter_folder)
        if not letter_files:
            print(f"No images found in folder for letter: {letter}")
            continue
        letter_image_path = os.path.join(letter_folder, letter_files[0])

        letter_image = cv2.imread(letter_image_path)
        if letter_image is None:
            print(f"Image not found or could not be read for letter: {letter}")
            continue

        if combined_image is None:
            combined_image = letter_image
        else:
            combined_image = cv2.hconcat([combined_image, letter_image])

    return combined_image

recognizer = sr.Recognizer()

with sr.Microphone() as source:

    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("You can start speaking now!")


    while True:
        try:

            print("Listening...")
            audio_data = recognizer.listen(source)


            text = recognizer.recognize_google(audio_data)
            print(f"Text: {text}")

            words = text.strip().split()
            for word in words:
                print(f"Displaying sign language for word: {word}")
                word_image = process_word(word)

                if word_image is not None:
                    word_image_rgb = cv2.cvtColor(word_image, cv2.COLOR_BGR2RGB)


                    plt.figure(figsize=(10, 5))
                    plt.imshow(word_image_rgb)
                    plt.axis('off')  # Hide axes for a cleaner display
                    plt.title(f"Word: {word}")
                    plt.show()
                else:
                    print(f"Could not process word: {word}")
            if "exit" in text.lower():
                print("Exiting...")
                break

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

print("Processing complete!")