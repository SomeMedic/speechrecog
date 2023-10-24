import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import threading


def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_text.insert(tk.END, "Настройка шумоподавления\n")
        root.update_idletasks()
        recognizer.adjust_for_ambient_noise(source, duration=1)
        root.update_idletasks()
        output_text.insert(tk.END, "Запись на 3 секунды\n")
        root.update_idletasks()
        recorded_audio = recognizer.listen(source, timeout=3)
        output_text.insert(tk.END, "Запись завершена\n")
    return recorded_audio


def recognize_speech(audio):
    recognizer = sr.Recognizer()
    try:
        output_text.insert(tk.END, "Распознавание текста\n")
        root.update_idletasks()
        text = recognizer.recognize_google(
            audio,
            language="ru-RU"
        )
        output_text.insert(tk.END, "Распознанный текст: " + text + "\n")
        root.update_idletasks()
        result_label.config(text="Распознанный текст: " + text)
        progress_bar.stop()
    except Exception as ex:
        output_text.insert(tk.END, "Ошибка при распознавании: " + str(ex) + "\n")
        root.update_idletasks()
        result_label.config(text="Ошибка при распознавании")
        progress_bar.stop()


def start_recognition():
    progress_bar.start()
    output_text.insert(tk.END, "Запуск распознавания\n")
    root.update_idletasks()
    recorded_audio = record_audio()
    recognize_thread = threading.Thread(target=recognize_speech, args=(recorded_audio,))
    recognize_thread.start()


root = tk.Tk()
root.title("Распознавание речи")
root.geometry("600x500")

# Цветовая палитра
BG_COLOR = "#FFFFFF"  # Белый
BTN_COLOR = "#E74C3C"  # Красный
TEXT_COLOR = "#2C3E50"  # Темно-синий

root.configure(bg=BG_COLOR)

# Frame для всего содержимого
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=40, padx=20)

# Текстовое поле для вывода программы
output_text = tk.Text(frame, height=15, width=60, wrap=tk.WORD, bg="#ECF0F1", fg=TEXT_COLOR, font=("Arial", 12))
output_text.pack(pady=20)

# Кнопка для начала распознавания
start_button = tk.Button(frame, text="Начать распознавание", command=start_recognition, bg=BTN_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"))
start_button.pack(pady=20)

result_label = tk.Label(frame, text="", bg='white', font=("Arial", 12, "bold"))
result_label.pack(pady=10)


# Полоса загрузки (индикатор прогресса)
progress_bar = ttk.Progressbar(frame, mode='indeterminate', length=400)
progress_bar.pack(pady=20)

root.mainloop()