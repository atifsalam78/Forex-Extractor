import tkinter as tk
from PIL import ImageTk
from tkinter import *
import currency
from tkinter import ttk
import customtkinter

bg_color = "#dab600"

button_bg_color = "#e6d17a"

def load_frame1():
	frame_main.pack_propagate(False)
	# Logo Widget
	logo_img = ImageTk.PhotoImage(file="assets/currency_logo_small.png")
	logo_widget = tk.Label(frame_main, image=logo_img, bg=bg_color)
	logo_widget.image = logo_img
	logo_widget.pack()

	# Label Widget
	tk.Label(frame_main, text="Ready to extract currency data from the web", 
		bg=bg_color,
		fg="black",
		font=("TkMenuFont", 14)).pack()

	# First Frame
	frame1 = tk.Frame(frame_main, width=50, height=27, bg=bg_color)
	frame1.pack(pady=4, padx=6,  expand=False)

	buttonClear = tk.Button(master=frame1, text="C", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:clear(),font=('Arial', 20))
	buttonClear.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("<Escape>",lambda event:clear())

	buttonDiv = tk.Button(master=frame1, text="/", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("/"),font=('Arial', 20))
	buttonDiv.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("/",lambda event:buttonPress("/"))

	buttonMul = tk.Button(master=frame1, text="x", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("*"),font=('Arial', 20))
	buttonMul.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("*",lambda event:buttonPress("*"))

	buttonMin = tk.Button(master=frame1, text="-", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("-"),font=('Arial', 20))
	buttonMin.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("-",lambda event:buttonPress("-"))

	buttonPlus = tk.Button(master=frame1, text="+", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("+"),font=('Arial', 20))
	buttonPlus.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("+",lambda event:buttonPress("+"))


	# Second Frame
	frame1 = tk.Frame(frame_main, width=50, height=27, bg=bg_color)
	frame1.pack(pady=4, padx=6,  expand=False)

	button7 = tk.Button(master=frame1, text="7", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("7"),font=('Arial', 20))
	button7.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("7",lambda event:buttonPress("7"))

	button8 = tk.Button(master=frame1, text="8", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("8"),font=('Arial', 20))
	button8.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("8",lambda event:buttonPress("8"))

	button9 = tk.Button(master=frame1, text="9", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("9"),font=('Arial', 20))
	button9.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("9",lambda event:buttonPress("9"))

	buttonRoot = tk.Button(master=frame1, text="√", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("**0.5"),font=('Arial', 20))
	buttonRoot.pack(padx=2, pady=2, side=tk.LEFT)
	# root.bind("-",lambda event:buttonPress("-", expression))

	buttonSqrt = tk.Button(master=frame1, text="sqr", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("**2"),font=('Arial', 20))
	buttonSqrt.pack(padx=2, pady=2, side=tk.LEFT)
	# root.bind("+",lambda event:buttonPress("+", expression))

    # Third Frame
	frame1 = tk.Frame(frame_main, width=50, height=27, bg=bg_color)
	frame1.pack(pady=4, padx=6,  expand=False)

	button4 = tk.Button(master=frame1, text="4", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("4"),font=('Arial', 20))
	button4.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("4",lambda event:buttonPress("4"))

	button5 = tk.Button(master=frame1, text="5", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("5"),font=('Arial', 20))
	button5.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("5",lambda event:buttonPress("5"))

	button6 = tk.Button(master=frame1, text="6", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("6"),font=('Arial', 20))
	button6.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("6",lambda event:buttonPress("6"))

	buttonBackSpace = tk.Button(master=frame1, text="<<", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:returnExp(),font=('Arial', 20))
	buttonBackSpace.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("<BackSpace>",lambda event:returnExp())

	buttonPer = tk.Button(master=frame1, text="%", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("/100"),font=('Arial', 20))
	buttonPer.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("%",lambda event:buttonPress("%"))

	# Fourth Frame
	frame1 = tk.Frame(frame_main, width=50, height=27, bg=bg_color)
	frame1.pack(pady=4, padx=6,  expand=False)

	button1 = tk.Button(master=frame1, text="1", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("1"),font=('Arial', 20))
	button1.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("1",lambda event:buttonPress("1"))

	button2 = tk.Button(master=frame1, text="2", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("2"),font=('Arial', 20))
	button2.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("2",lambda event:buttonPress("2"))

	button3 = tk.Button(master=frame1, text="3", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("3"),font=('Arial', 20))
	button3.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("3",lambda event:buttonPress("3"))

	button0 = tk.Button(master=frame1, text="0", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("0"),font=('Arial', 20))
	button0.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("0",lambda event:buttonPress("0"))

	buttonDec = tk.Button(master=frame1, text=".", fg="black", bg=button_bg_color,width=3, height=1,
		command=lambda:buttonPress("."),font=('Arial', 20))
	buttonDec.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind(".",lambda event:buttonPress("."))

	# Fifth Frame
	frame1 = tk.Frame(frame_main, width=50, height=27, bg=bg_color)
	frame1.pack(pady=4, padx=6,  expand=False)

	buttonEqual = tk.Button(master=frame1, text="=", fg="black", bg=button_bg_color,width=11, height=1,
		command=lambda:equalPress(),font=('Arial', 20))
	buttonEqual.pack(padx=2, pady=2, side=tk.LEFT)
	root.bind("<Return>",lambda event:equalPress())

    

expression = ""

def clear():    
    global expression  
    equation.set("")
    # return expression

def buttonPress(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
    # return expression

def character_limit(expression):
    if len(equation.get()) >= 16:
        equation.set(equation.get()[:-1])

def equalPress():
    try:
        global expression
        character_limit(expression)
        total = str(eval(expression))
        equation.trace("w", lambda *args: character_limit(expression))
        equation.set(total)        

    except:
        equation.set("Invalid Syntax")
        expression = ""

def returnExp():
    global expression
    expression = expression[:-1]
    equation.set(expression)



def OpenMarket():
	currency.openRates()

def InterBank():
	currency.interBankRates()

def ForeignExchange():
	currency.foreignExchangeRates()

def GoldRates():
	currency.goldRates()

def GoldRatesPak():
	currency.goldRatesPak()

def GoldRatesOthers():
	currency.goldRatesOthers()


def main_frame(title, frame_width, frame_height, screen_width, screen_height):
	"""
    Create the main frame for the application.

    Parameters:
    - title: Title of the main frame
    - frame_width: Width of the frame
    - frame_height: Height of the frame
    - screen_width: Ratio of screen width for positioning
    - screen_height: Ratio of screen height for positioning

    Returns:
    - root: The main Tkinter window
    - frame_main: The main frame widget
    """
	root = tk.Tk()
	root.title(title)

	style = ttk.Style()
	style.theme_use('clam')

	x = root.winfo_screenwidth()//screen_width
	y = int(root.winfo_screenheight()*screen_height)
	root.geometry(f'{frame_width}x{frame_height}+' + str(x) + '+' + str(y))

	frame_main = tk.Frame(root, width=frame_width, height=frame_height, bg=bg_color)
	frame_main.grid(row=0, column=0)
	frame_main.pack_propagate(False)
	return root, frame_main


def about():
	# Initializing App
	root, frame_main = main_frame("About", 500, 200, 2, 0.1)
	# root = tk.Tk()
	# root.title('About')
	# # Place our window to the centre of the screen 
	# # root.eval("tk::PlaceWindow . center")
	# x = root.winfo_screenwidth()//2
	# y = int(root.winfo_screenheight()*0.1)
	# root.geometry('500x200+' + str(x) + '+' + str(y))

	# # Creating Frame Widget
	# frame_main = tk.Frame(root, width=500, height=200, bg=bg_color)
	# frame_main.grid(row=0, column=0)
	# frame_main.pack_propagate(False)
	
	# Label Widget
	encodings = ['utf-8', 'latin-1']
	for encoding in encodings:
		with open("assets/about.txt", "rb") as file:
		 file_content = file.read().decode(encoding)
	
	tk.Label(frame_main, text=file_content,
		bg=bg_color,
		fg="black",
		font=("TkMenuFont", 10), wraplength=400).pack()


	root.mainloop()

def license():
	# Initializing App
	root, frame_main = main_frame("License", 500, 600, 4, 0.1)

	# root = tk.Tk()
	# root.title('License')
	# # Place our window to the centre of the screen 
	# # root.eval("tk::PlaceWindow . center")
	# x = root.winfo_screenwidth()//4
	# y = int(root.winfo_screenheight()*0.1)
	# root.geometry('500x600+' + str(x) + '+' + str(y))

	# # Creating Frame Widget
	# frame_main = tk.Frame(root, width=500, height=600, bg=bg_color)
	# frame_main.grid(row=0, column=0)
	# frame_main.pack_propagate(False)


	# Label Widget
	encodings = ['utf-8', 'latin-1']
	for encoding in encodings:
		with open("assets/license.txt", "rb") as file:
		 file_content = file.read().decode(encoding)
	
	tk.Label(frame_main, text=file_content,
		bg=bg_color,
		fg="black",
		font=("TkMenuFont", 10), wraplength=400).pack()

	root.mainloop()

if __name__=="__main__":

	# Initializing App
	root, frame_main = main_frame("currency Converter", 500, 600, 3, 0.1)
	
	# root = tk.Tk()
	# root.title('Currency Extractor')

	# style = ttk.Style()
	# style.theme_use('clam')  # Change the theme here (e.g., 'clam', 'alt', 'default', 'classic')

	# # Place our window to the centre of the screen 
	# # root.eval("tk::PlaceWindow . center")
	# x = root.winfo_screenwidth()//3
	# y = int(root.winfo_screenheight()*0.1)
	# root.geometry('500x600+' + str(x) + '+' + str(y))

	
	# # Creating Frame Widget
	# frame_main = tk.Frame(root, width= 500, height=600, bg=bg_color)
	# frame_main.grid(row=0, column=0)

	equation = StringVar()
	expressionLabel = tk.Entry(master=frame_main, justify=tk.CENTER, width=200,
		textvariable=equation,font=('Arial', 20), fg="black", bg=bg_color)
	expressionLabel.configure(state="disabled")
	expressionLabel.pack()
	equation.trace("w", lambda *args: character_limit(expression))

	load_frame1()

	# Menu Bar
	menu_bar = tk.Menu(root)	

	# Currency Menu
	currency_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Currency", menu=currency_menu)
	currency_menu.add_command(label="Open Market Rates", command=OpenMarket)
	currency_menu.add_command(label="Inter Bank Rates", command=InterBank)
	currency_menu.add_command(label="Foreign Exchange Rates", command=ForeignExchange)
	currency_menu.add_separator()
	currency_menu.add_command(label="Exit", command=root.destroy)

	# Gold Menu
	gold_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Gold", menu=gold_menu)
	gold_menu.add_command(label="Gold Rates", command=GoldRates)
	gold_menu.add_command(label="Gold Rates(PAK)", command=GoldRatesPak)
	gold_menu.add_command(label="Gold Price(Others)", command=GoldRatesOthers)
	
	
	# Help Menu
	help_menu = tk.Menu(menu_bar, tearoff=0)
	menu_bar.add_cascade(label="Help", menu=help_menu)
	help_menu.add_command(label="Setting", command=InterBank)
	help_menu.add_command(label="License", command=license)
	help_menu.add_command(label="About", command=about)

	help_menu.entryconfig("Setting", state="disabled")

	root.config(menu=menu_bar)
	root.mainloop()