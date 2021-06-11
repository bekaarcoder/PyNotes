from tkinter import *
from tkinter import ttk, messagebox
from database import Database, ConnectionFromPool


class BookDB:
    headers = ["ID", "Name", "Author", "Genre", "Pages", "Rating"]
    books = []

    def __init__(self):
        self.tree = None
        self.initialize_db()
        self.create_widgets()

    def initialize_db(self):
        Database.initialize(
            user="postgres",
            password="postgres",
            database="library",
            host="localhost",
        )

    def create_widgets(self):
        bname_label = Label(main, text="Book Name")
        bname_label.grid(row=0, column=0, padx=5, pady=10, sticky="W")
        self.bname_entry_value = StringVar(main, value="")
        self.bname_entry = ttk.Entry(main, textvariable=self.bname_entry_value)
        self.bname_entry.grid(row=0, column=1, padx=5, pady=10, sticky="W")

        author_label = Label(main, text="Author")
        author_label.grid(row=0, column=2, padx=5, pady=10, sticky="W")
        self.author_entry_value = StringVar(main, value="")
        self.author_entry = ttk.Entry(
            main, textvariable=self.author_entry_value
        )
        self.author_entry.grid(row=0, column=3, padx=5, pady=10, sticky="W")

        rating_label = Label(main, text="Rating")
        rating_label.grid(row=0, column=4, padx=5, pady=10, sticky="W")
        self.rating_entry_value = StringVar(main, value="")
        self.rating_entry = ttk.Entry(
            main, textvariable=self.rating_entry_value
        )
        self.rating_entry.grid(row=0, column=5, padx=5, pady=10, sticky="W")

        genre_label = Label(main, text="Genre")
        genre_label.grid(row=1, column=0, padx=5, pady=10, sticky="W")
        self.genre_entry_value = StringVar(main, value="")
        self.genre_entry = ttk.Entry(main, textvariable=self.genre_entry_value)
        self.genre_entry.grid(row=1, column=1, padx=5, pady=10, sticky="W")

        pages_label = Label(main, text="Pages")
        pages_label.grid(row=1, column=2, padx=5, pady=10, sticky="W")
        self.pages_entry_value = StringVar(main, value="")
        self.pages_entry = ttk.Entry(main, textvariable=self.pages_entry_value)
        self.pages_entry.grid(row=1, column=3, padx=5, pady=10, sticky="W")

        add_button = ttk.Button(main, text="Add Book", command=self.add_book)
        add_button.grid(row=1, column=4, sticky=(W, E))

        bid_label = Label(main, text="ID")
        bid_label.grid(row=2, column=0, padx=5, pady=10, sticky="W")
        self.bid_entry_value = StringVar(main, value="")
        self.bid_entry = ttk.Entry(main, textvariable=self.bid_entry_value)
        self.bid_entry.grid(row=2, column=1, padx=5, pady=10, sticky="W")

        update_button = ttk.Button(
            main, text="Update Book", command=self.update_book
        )
        update_button.grid(row=2, column=2, sticky=(W, E))

        delete_button = ttk.Button(
            main, text="Delete Book", command=self.delete_book
        )
        delete_button.grid(row=2, column=3, sticky=(W, E))

        self.tree = ttk.Treeview(
            main,
            height=15,
            columns=("ID", "Name", "Author", "Genre", "Pages", "Rating"),
            selectmode="browse",
        )
        self.tree.grid(row=3, column=0, columnspan=6)
        self.tree["show"] = "headings"

        i = 1
        for col in self.headers:
            num = f"#{i}"
            self.tree.heading(num, text=col)
            self.tree.column(num, width=150)
            i += 1

        self.update_table()

    def update_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        with ConnectionFromPool() as cursor:
            cursor.execute("select * from books")
            self.books = cursor.fetchall()
        i = 1
        for book_info in self.books:
            num = f"#{i}"
            self.tree.insert("", "end", values=book_info)
            i += 1

    def add_book(self):
        book_name = str(self.bname_entry_value.get())
        author = str(self.author_entry_value.get())
        genre = str(self.genre_entry_value.get())
        pages = int(self.pages_entry_value.get())
        rating = float(self.rating_entry_value.get())
        with ConnectionFromPool() as cursor:
            cursor.execute(
                "insert into books (book_name, author, genre, pages, avg_rating) values (%s, %s, %s, %s, %s)",
                (book_name, author, genre, pages, rating),
            )
        self.update_table()
        messagebox.showinfo(
            title="Message", message="Book successfully added!"
        )

    def update_book(self):
        book_id = int(self.bid_entry_value.get())
        book_name = str(self.bname_entry_value.get())
        author = str(self.author_entry_value.get())
        genre = str(self.genre_entry_value.get())
        pages = int(self.pages_entry_value.get())
        rating = float(self.rating_entry_value.get())
        with ConnectionFromPool() as cursor:
            cursor.execute(
                f"update books set book_name = '{book_name}', author = '{author}', genre = '{genre}', pages = '{pages}', avg_rating = '{rating}' where book_id = '{book_id}'"
            )

        self.update_table()
        messagebox.showinfo(
            title="Message", message="Book successfully updated!"
        )

    def delete_book(self):
        book_id = int(self.bid_entry_value.get())
        with ConnectionFromPool() as cursor:
            cursor.execute(f"delete from books where book_id = '{book_id}'")

        self.update_table()
        messagebox.showinfo(
            title="Message", message="Book successfully deleted!"
        )


root = Tk()
# root.geometry("1400x600")
root.title("Book Database")

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=4, pady=(8, 1))

book_db = BookDB()
root.mainloop()