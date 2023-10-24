import speech_recognition as sr
import threading


def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Настройка шумоподавления")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Запись на 3 секунды")
        record_audio = recognizer.listen(source, timeout=3)
        print("Запись завершена")
    return record_audio


def recognize_speech(audio):
    recognizer = sr.Recognizer()
    try:
        print("Распознавание текста...")
        text = recognizer.recognize_google(
            audio,
            language="ru-RU"
        )
        print("Распознанный текст : {}".format(text))
    except Exception as ex:
        print(ex)


def main():
    record_thread = threading.Thread(target=recognize_speech, args=(record_audio(),))
    record_thread.start()
    record_thread.join()


if __name__ == "__main__":
    main()