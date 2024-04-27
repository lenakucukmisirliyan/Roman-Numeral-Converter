import tkinter

def roman_to_int():
    roman_input = roman_entry.get().upper()
    total = 0
    invalid_input = False

    for i in range(len(roman_input) - 1):
        if roman_input[i] == roman_input[i + 1]:
            if roman_input.count(roman_input[i]) > 3 or roman_input[i] not in ['I', 'X', 'C', 'M']:
                invalid_input = True
                result_label.config(text="Please enter a valid roman numeral!")
                return

    for element in roman_input:
        if element not in roman_numeral_dict:
            invalid_input = True
            result_label.config(text="Please enter a valid roman numeral!")
            return

    if invalid_input:
        return

    i = 0
    while i < len(roman_input):
        current_value = roman_numeral_dict[roman_input[i]]
        if i + 1 < len(roman_input):
            next_value = roman_numeral_dict[roman_input[i + 1]]
            if current_value < next_value:
                total += next_value - current_value
                i += 2
                continue
        total += current_value
        i += 1
    result_label.config(text=str(total))


FONT = ("Times New Roman", "24", "normal")

window = tkinter.Tk()
window.title("Roman Numeral Converter")
window.minsize(width=450, height=450)
window.config(padx=50, pady=50)

roman_label = tkinter.Label(window, text="Roman Numeral", font=FONT, pady=30)
roman_label.pack()

roman_entry = tkinter.Entry(window, width=20, font=FONT)
roman_entry.focus()
roman_entry.pack()

button_frame = tkinter.Frame(window, padx=30, pady=30)
button_frame.pack()

convert_button = tkinter.Button(button_frame, text="Convert to Decimal", command=roman_to_int, font=FONT)
convert_button.pack()

result_label = tkinter.Label(window, font=FONT)
result_label.pack()

roman_numeral_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

window.mainloop()
