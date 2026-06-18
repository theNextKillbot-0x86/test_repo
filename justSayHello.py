import ctypes

def Popup(Owner=0, Text="Sample text", Title="Title", Flags=None):
   if Flags == None: Flags = [0x1, 0x40]
   return ctypes.windll.user32.MessageBoxW(Owner, Text, Title, Flags[0] | Flags[1])

if __name__ == "__main__":
   Popup(0, "Hi", "Title here", [0x1, 0x40])
else:
   print("No")