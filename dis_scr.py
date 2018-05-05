
import ctypes
from tkinter import *

ES_AWAYMODE_REQUIRED = 0x40
ES_CONTINUOUS = 0x80000000
ES_DISPLAY_REQUIRED = 0x2
ES_SYSTEM_REQUIRED = 0x1

set_scr = ctypes.windll.kernel32.SetThreadExecutionState

class App(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self,parent)
		self.parent = parent
		self.pack()
		self.winfo_toplevel().title("SCR:ON")
		self.chkbox = IntVar()
		btn = Checkbutton(self, text="Disable SCR", variable=self.chkbox, width=22, command=self.toggle)
		btn.pack()
		
	def toggle(self):
		if self.chkbox.get():
			set_scr(ES_CONTINUOUS | ES_AWAYMODE_REQUIRED | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED)
			self.winfo_toplevel().title("SCR:OFF")
		else:
			set_scr(ES_CONTINUOUS)
			self.winfo_toplevel().title("SCR:ON")
			
def _main():
	root = Tk()
	app = App(root)
	root.mainloop()
	set_scr(ES_CONTINUOUS)

if __name__ == "__main__":
	_main()
else:
	print("excute \"_main()\" ")
