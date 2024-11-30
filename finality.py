import tkinter as tk
from tkinter import messagebox
import sqlite3
import requests

class DatabaseManager:
    """Клас для роботи з базою даних SQLite."""
    def __init__(self, db_name="users.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def add_user(self, name, email):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

class UserParser:
    """Клас для отримання даних користувачів із зовнішнього API."""
    @staticmethod
    def fetch_random_user():
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            user = data['results'][0]
            name = f"{user['name']['first']} {user['name']['last']}"
            email = user['email']
            return name, email
        else:
            raise Exception("Failed to fetch user data.")

class Application:
    """Клас для управління графічним інтерфейсом."""
    def __init__(self, root):
        self.root = root
        self.root.title("лохотрон")
        self.db_manager = DatabaseManager()

        # Поля для введення даних
        self.name_label = tk.Label(root, text="ім'я:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="ємаіл:")
        self.email_label.grid(row=1, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Кнопки
        self.add_button = tk.Button(root, text="добавити лоха", command=self.add_user)
        self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.fetch_button = tk.Button(root, text="придумати лоха", command=self.fetch_random_user)
        self.fetch_button.grid(row=2, column=1, padx=10, pady=5)

        self.view_button = tk.Button(root, text="подивитись лохів", command=self.view_users)
        self.view_button.grid(row=3, column=0, columnspan=2, pady=5)

        # Список користувачів
        self.user_listbox = tk.Listbox(root, width=50)
        self.user_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def add_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        if name and email:
            self.db_manager.add_user(name, email)
            messagebox.showinfo("+лох", "лох повівся!")
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.view_users()
        else:
            messagebox.showerror("ти сліпий?", "все заповни!")

    def fetch_random_user(self):
        try:
            name, email = UserParser.fetch_random_user()
            self.name_entry.insert(0, name)
            self.email_entry.insert(0, email)
            messagebox.showinfo("рандомний лох", f"придумано: {name} - {email}")
        except Exception as e:
            messagebox.showerror("помилка", str(e))

    def view_users(self):
        self.user_listbox.delete(0, tk.END)
        users = self.db_manager.get_users()
        for user in users:
            self.user_listbox.insert(tk.END, f"{user[0]}. {user[1]} - {user[2]}")

    def on_close(self):
        self.db_manager.close()
        self.root.destroy()

# Запуск програми
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()