import tkinter as tk
from tkinter import messagebox, ttk

class TicketBookingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ticket Booking System")
        self.geometry("400x300")
       
        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        self.label = ttk.Label(self.main_frame, text=".....BOOK YOUR TICKETS.....", font=('Arial', 16))
        self.label.pack(pady=10)

        self.choice_var = tk.IntVar()
        self.choice_var.set(0)

        self.movie_button = ttk.Button(self.main_frame, text="Movies", command=self.show_movie_options)
        self.movie_button.pack(pady=5)

        self.series_button = ttk.Button(self.main_frame, text="Series", command=self.show_series_options)
        self.series_button.pack(pady=5)

    def show_movie_options(self):
        self.clear_frame()
        self.label = ttk.Label(self.main_frame, text="Select a Movie", font=('Arial', 14))
        self.label.pack(pady=10)

        self.movie_var = tk.IntVar()

        movies = {
            1: "Saripodha Saniraram",
            2: "G.O.A.T",
            3: "Raayan"
        }

        for key, value in movies.items():
            ttk.Radiobutton(self.main_frame, text=value, variable=self.movie_var, value=key).pack(pady=2)

        self.next_button = ttk.Button(self.main_frame, text="Next", command=self.show_theater_options)
        self.next_button.pack(pady=10)

    def show_theater_options(self):
        self.selected_movie = self.movie_var.get()
        if self.selected_movie not in [1, 2, 3]:
            messagebox.showerror("Error", "Please select a movie.")
            return

        self.clear_frame()
        self.label = ttk.Label(self.main_frame, text="Select a Theater", font=('Arial', 14))
        self.label.pack(pady=10)

        self.theater_var = tk.IntVar()

        theaters = {
            1: "Imax",
            2: "Prasad"
        }

        for key, value in theaters.items():
            ttk.Radiobutton(self.main_frame, text=value, variable=self.theater_var, value=key).pack(pady=2)

        self.next_button = ttk.Button(self.main_frame, text="Next", command=self.show_time_options)
        self.next_button.pack(pady=10)

    def show_time_options(self):
        self.selected_theater = self.theater_var.get()
        if self.selected_theater not in [1, 2]:
            messagebox.showerror("Error", "Please select a theater.")
            return

        self.clear_frame()
        self.label = ttk.Label(self.main_frame, text="Select a Showtime", font=('Arial', 14))
        self.label.pack(pady=10)

        self.time_var = tk.IntVar()

        times = {
            1: "8:00 AM",
            2: "12:00 PM",
            3: "5:00 PM"
        }

        for key, value in times.items():
            ttk.Radiobutton(self.main_frame, text=value, variable=self.time_var, value=key).pack(pady=2)

        self.next_button = ttk.Button(self.main_frame, text="Next", command=self.enter_seat_count)
        self.next_button.pack(pady=10)

    def enter_seat_count(self):
        self.selected_time = self.time_var.get()
        if self.selected_time not in [1, 2, 3]:
            messagebox.showerror("Error", "Please select a time.")
            return

        self.clear_frame()
        self.label = ttk.Label(self.main_frame, text="Enter Seat Count", font=('Arial', 14))
        self.label.pack(pady=10)

        self.seat_count_var = tk.IntVar()

        ttk.Label(self.main_frame, text="Available Seats: 20").pack(pady=5)
        ttk.Entry(self.main_frame, textvariable=self.seat_count_var).pack(pady=5)

        self.next_button = ttk.Button(self.main_frame, text="Confirm", command=self.confirm_booking)
        self.next_button.pack(pady=10)

    def confirm_booking(self):
        try:
            seats = self.seat_count_var.get()
            if seats <= 0 or seats > 20:
                raise ValueError

            theater_names = {1: "Imax", 2: "Prasad"}
            time_names = {1: "8:00 AM", 2: "12:00 PM", 3: "5:00 PM"}

            movie_name = {1: "Saripodha Saniraram", 2: "G.O.A.T", 3: "Raayan"}[self.selected_movie]
            theater_name = theater_names[self.selected_theater]
            time_name = time_names[self.selected_time]

            messagebox.showinfo("Booking Confirmed", f"Your Ticket is booked\nMovie: {movie_name}\nTheater: {theater_name}\nTime: {time_name}\nSeats: {seats}\nMake sure you reach 10 mins before the show time.")
            self.quit()
        except (ValueError, KeyError):
            messagebox.showerror("Error", "Invalid seat count. Please enter a valid number of seats.")

    def show_series_options(self):
        self.clear_frame()
        self.label = ttk.Label(self.main_frame, text="Select a Series", font=('Arial', 14))
        self.label.pack(pady=10)

        self.series_var = tk.IntVar()

        series = {
            1: "Gyarah Gyarah",
            2: "Lucifer",
            3: "Taaga Khabbar",
            4: "One Piece (Anime)"
        }

        for key, value in series.items():
            ttk.Radiobutton(self.main_frame, text=value, variable=self.series_var, value=key).pack(pady=2)

        self.next_button = ttk.Button(self.main_frame, text="Next", command=self.show_series_info)
        self.next_button.pack(pady=10)

    def show_series_info(self):
        selected_series = self.series_var.get()
        if selected_series not in [1, 2, 3, 4]:
            messagebox.showerror("Error", "Please select a series.")
            return

        self.clear_frame()
        self.label = ttk.Label(self.main_frame, text="Series Information", font=('Arial', 14))
        self.label.pack(pady=10)

        if selected_series in [1, 3]:
            message = "Gyarah Gyarah and Taaga Khabbar are available on Hotstar."
        else:
            message = "Lucifer and One Piece are available on Netflix."

        ttk.Label(self.main_frame, text=message).pack(pady=10)
        self.back_button = ttk.Button(self.main_frame, text="Back to Main Menu", command=self.create_widgets)
        self.back_button.pack(pady=10)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = TicketBookingApp()
    app.mainloop()
