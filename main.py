import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather, get_weather_by_location


# ---------------- Logic ---------------- #
def fetch_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    data = get_weather(city)

    if data is None:
        messagebox.showerror("Error", "Unable to fetch weather data")
        return

    display_weather(data, auto=False)


def fetch_weather_location():
    data = get_weather_by_location()

    if data is None:
        messagebox.showerror("Error", "Unable to detect location")
        return

    display_weather(data, auto=True)


def display_weather(data, auto=False):
    title = f"{data['city']} (Auto-detected)" if auto else data["city"]

    result_label.config(
        text=(
            f"City: {title}\n\n"
            f"Temperature: {data['temperature']} °C\n"
            f"Humidity: {data['humidity']} %\n"
            f"Wind Speed: {data['wind_speed']} m/s\n"
            f"Condition: {data['condition']}"
        )
    )


# ---------------- Window ---------------- #
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("440x420")
root.resizable(False, False)
root.configure(bg="#121212")


# ---------------- Title ---------------- #
tk.Label(
    root,
    text="Weather Forecast",
    font=("Segoe UI", 20, "bold"),
    fg="#ffffff",
    bg="#121212"
).pack(pady=(20, 10))


# ---------------- Input ---------------- #
city_entry = tk.Entry(
    root,
    font=("Segoe UI", 12),
    width=30,
    bg="#1e1e1e",
    fg="#ffffff",
    insertbackground="white",
    relief="flat"
)
city_entry.pack(pady=10)
city_entry.focus()


# ---------------- Buttons ---------------- #
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=10)

fetch_btn = tk.Button(
    btn_frame,
    text="Get Weather",
    font=("Segoe UI", 11, "bold"),
    bg="#1f6feb",
    fg="white",
    activebackground="#388bfd",
    relief="flat",
    padx=15,
    pady=8,
    command=fetch_weather
)
fetch_btn.grid(row=0, column=0, padx=5)

location_btn = tk.Button(
    btn_frame,
    text="Use My Location",
    font=("Segoe UI", 11, "bold"),
    bg="#2ea043",
    fg="white",
    activebackground="#3fb950",
    relief="flat",
    padx=15,
    pady=8,
    command=fetch_weather_location
)
location_btn.grid(row=0, column=1, padx=5)


# ---------------- Hover Animations ---------------- #
def hover(btn, color):
    btn.bind("<Enter>", lambda e: btn.config(bg=color))
    btn.bind("<Leave>", lambda e: btn.config(bg=btn.original_bg))


fetch_btn.original_bg = "#1f6feb"
location_btn.original_bg = "#2ea043"

hover(fetch_btn, "#2a7fff")
hover(location_btn, "#3fb950")


# ---------------- Result Card ---------------- #
card = tk.Frame(root, bg="#1e1e1e")
card.pack(padx=20, pady=15, fill="both", expand=True)

result_label = tk.Label(
    card,
    text="",
    font=("Segoe UI", 11),
    fg="#e6e6e6",
    bg="#1e1e1e",
    justify="left",
    wraplength=380
)
result_label.pack(padx=15, pady=15)


# ---------------- Start ---------------- #
root.mainloop()
