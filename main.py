import tkinter as tk
from tkinter import messagebox

# Lista e pyetjeve gramatikore, opsioneve dhe përgjigjeve të sakta
quiz_data = [
    {
        "question": "Könnten Sie mir bitte ... bringen?",
        "meaning": "Could you please bring me the card?",
        "options": ["der Karte", "die Karte", "das Karte"],
        "answer": "die Karte"
    },
    {
        "question": "Er hat ... Buch gelesen.",
        "meaning": "He has read the book.",
        "options": ["dem", "den", "das"],
        "answer": "das"
    },
    {
        "question": "Das ist das Auto ..., ich dir gestern gezeigt habe.",
        "meaning": "That is the car which I showed you yesterday.",
        "options": ["die", "das", "der"],
        "answer": "das"
    },
    {
        "question": "Ich gehe morgen in ... Schule.",
        "meaning": "I am going to the school tomorrow.",
        "options": ["der", "die", "das"],
        "answer": "die"
    },
    {
        "question": "Die Frau ... Buch auf dem Tisch liegt, ist meine Lehrerin.",
        "meaning": "The woman whose book is on the table is my teacher.",
        "options": ["deren", "dessen", "der"],
        "answer": "deren"
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grammatik Quiz")
        self.root.geometry("500x450")
        self.root.configure(bg="#f0f4f7")  # Sfondi i dritares

        self.score = 0
        self.current_question = 0

        # Titulli i quiz-it
        self.title_label = tk.Label(root, text="Grammatik Quiz", font=("Arial", 24, "bold"), bg="#f0f4f7", fg="#34495e")
        self.title_label.pack(pady=10)

        # Pyetja
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center", bg="#f0f4f7")
        self.question_label.pack(pady=10)

        # Kuptimi
        self.meaning_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400, justify="center", fg="gray", bg="#f0f4f7")
        self.meaning_label.pack(pady=5)

        # Opsionet (butonat) - nuk ka opsion të parazgjedhur
        self.option_var = tk.StringVar()
        self.option_var.set(None)

        # Stilizimi i butonave të opsioneve
        self.option1 = tk.Radiobutton(root, text="", variable=self.option_var, value="", font=("Arial", 12), bg="#d5e8f9", activebackground="#aed6f1", anchor="center", width=25)
        self.option1.pack(pady=5)

        self.option2 = tk.Radiobutton(root, text="", variable=self.option_var, value="", font=("Arial", 12), bg="#d5e8f9", activebackground="#aed6f1", anchor="center", width=25)
        self.option2.pack(pady=5)

        self.option3 = tk.Radiobutton(root, text="", variable=self.option_var, value="", font=("Arial", 12), bg="#d5e8f9", activebackground="#aed6f1", anchor="center", width=25)
        self.option3.pack(pady=5)

        # Butoni për të kontrolluar përgjigjen
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12, "bold"), bg="#5dade2", fg="white", activebackground="#3498db")
        self.submit_button.pack(pady=20)

        # Fillon quiz-in
        self.load_question()

    def load_question(self):
        if self.current_question < len(quiz_data):
            question_data = quiz_data[self.current_question]

            # Vendos pyetjen dhe opsionet
            self.question_label.config(text=f"Frage {self.current_question + 1}: {question_data['question']}")
            self.meaning_label.config(text=f"Bedeutung: {question_data['meaning']}")
            self.option_var.set(None)  # Nuk ka opsion të parazgjedhur

            # Vendos opsionet dhe i stilizon
            self.option1.config(text=question_data["options"][0], value=question_data["options"][0])
            self.option2.config(text=question_data["options"][1], value=question_data["options"][1])
            self.option3.config(text=question_data["options"][2], value=question_data["options"][2])
        else:
            # Shfaq rezultatin final
            messagebox.showinfo("Ergebnis", f"Quiz beendet! Sie haben {self.score} von {len(quiz_data)} Fragen richtig beantwortet.")
            self.root.quit()

    def check_answer(self):
        selected_answer = self.option_var.get()
        correct_answer = quiz_data[self.current_question]["answer"]

        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Richtige Antwort", "Richtige Antwort!")
        else:
            messagebox.showinfo("Falsche Antwort", f"Falsche Antwort! Die richtige Antwort ist: {correct_answer}")

        # Kalon te pyetja tjetër
        self.current_question += 1
        self.load_question()

# Krijo ndërfaqen grafike
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
