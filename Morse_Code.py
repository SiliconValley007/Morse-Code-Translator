##VARIABLE KEY  
##'cipher' -> 'stores the morse translated form of the english string'  
##'decipher' -> 'stores the english translated form of the morse string'  
##'citext' -> 'stores morse code of a single character'  
##'i' -> 'keeps count of the spaces between morse characters'  
##'message' -> 'stores the string to be encoded or decoded'

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip


root = Tk() 
#create global variables   
variable1 = StringVar(root)  
variable2 = StringVar(root)
    
#Dictionary represlanguage2_fielding the morse code chart  
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',  
                    'C':'-.-.', 'D':'-..', 'E':'.',  
                    'F':'..-.', 'G':'--.', 'H':'....',  
                    'I':'..', 'J':'.---', 'K':'-.-',  
                    'L':'.-..', 'M':'--', 'N':'-.',  
                    'O':'---', 'P':'.--.', 'Q':'--.-',  
                    'R':'.-.', 'S':'...', 'T':'-',  
                    'U':'..-', 'V':'...-', 'W':'.--',  
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',  
                    '1':'.----', '2':'..---', '3':'...--',  
                    '4':'....-', '5':'.....', '6':'-....',  
                    '7':'--...', '8':'---..', '9':'----.',  
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',  
                    '?':'..--..', '/':'-..-.', '-':'-....-',  
                    '(':'-.--.', ')':'-.--.-'}

def copy_text():
    pyperclip.copy(language2_field.get("1.0", "end")[:-1])
  
#Function to clear both the text areas 
def clearAll(): 
    language1_field.delete(1.0, END) 
    language2_field.delete(1.0, END)
  
#Function to perform coversion form one language to another 
def convert():
    #get the whole contlanguage2_field from the text box ignoring \n from the text box contlanguage2_field
    message = language1_field.get("1.0", "end")[:-1]
  
    #get the contlanguage2_field from varibale1 and variable2, check their values 
    if variable1.get() == variable2.get():  
        messagebox.showerror("Error", "Can't Be same Language") 
        return
  
    elif variable1.get() == "Eng" and variable2.get() == "Morse":
        rslt = encrypt(message.upper()) 
  
    elif variable1.get() == "Morse" and variable2.get() == "Eng":
        rslt = decrypt(message) 
  
    else:  
        messagebox.showerror("Error", "please choose valid language code..") 
        return

    language2_field.delete(1.0, END)
    language2_field.insert('end -1 chars', rslt) 
      
          
#Function to encrypt the string according to the morse code chart  
def encrypt(message):
    cipher = ''  
    for letter in message:  
        if letter != ' ': 
    
            #Looks up the dictionary and adds the  correspponding morse code along with a space to separate morse codes for differlanguage2_field characters.
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:  
            #1 space indicates differ language2_field characters and 2 indicates differ language2_field words.
            cipher += ' '
    
    return cipher  
    
#Function to decrypt the string from morse to english  
def decrypt(message):  
    
    #extra space added at the end to access the last morse code  
    message += ' '
    
    decipher = ''  
    citext = ''  
    for letter in message:  
    
        #checks for space  
        if (letter != ' '):  
    
            #counter to keep track of space  
            i = 0
    
            #storing morse code of a single character  
            citext += letter  
    
        #in case of space  
        else:  
            #if i = 1 that indicates a new character  
            i += 1
    
            #if i = 2 that indicates a new word  
            if i == 2 :  
    
                 #adding space to separate words  
                decipher += ' '
            else:  
    
                #accessing the keys using their values (reverse of encryption)  
                decipher += list(MORSE_CODE_DICT.keys())[ 
                             list(MORSE_CODE_DICT .values()).index(citext)]  
                citext = ''  
    
    return decipher  
  
  
# Driver code  
if __name__ == "__main__" :

    s = ttk.Style()
    s.configure('TLabel', background='#ffffff')
    
    root.configure(bg="#ffffff") 
    root.geometry("330x380")
    root.title("Morse Code Translator") 

    ttk.Label(root, text = 'Morse Code Translator', style="TLabel").grid(row = 0, column = 1)   
     
    ttk.Label(root, text = "Text", style="TLabel").grid(row = 1, column = 0)
          
    ttk.Label(root, text = "From", style="TLabel").grid(row = 2, column = 0)
        
    ttk.Label(root, text = "To", style="TLabel").grid(row = 3, column = 0)
    
    ttk.Label(root, text = "Translation", style="TLabel").grid(row = 5, column = 0, padx = 10) 
      
    language1_field = Text(root, height = 5, width = 25,  
                                     font = "lucida 13", bd=2)  
    language2_field = Text(root, height = 5, width = 25,  
                                     font = "lucida 13", bd=2)

    #Disable copying from the second text box, copying can be done through the dedicated button
    language2_field.bind('<Control-a>', lambda e: 'break')
    language2_field.bind('<Control-x>', lambda e: 'break')
    language2_field.bind('<Control-c>', lambda e: 'break')
    language2_field.bind('<Control-v>', lambda e: 'break')
    language2_field.bind('<Button-3>', lambda e: 'break')
           
    language1_field.grid(row = 1, column = 1, padx = (0,10))   
    language2_field.grid(row = 5, column = 1, padx = (0,10))  
    
    languageCode_list = ["Eng", "Morse", "Eng"]  
    
     
    FromLanguage_option = ttk.OptionMenu(root, variable1, *languageCode_list)  
    ToLanguage_option = ttk.OptionMenu(root, variable2, *languageCode_list)  
        
    FromLanguage_option.grid(row = 2, column = 1, ipadx = 10,pady=10)  
    ToLanguage_option.grid(row = 3, column = 1, ipadx = 10, pady=(0,10))  
        
      
    ttk.Button(root, text = "Convert", command = convert).grid(row = 4, column = 1, pady=(0,10))

    ttk.Button(root, text = "Copy", command = copy_text).grid(row = 6, column = 1, pady=10, sticky=W, padx=(10,0))
    
    ttk.Button(root, text = "Clear", command = clearAll).grid(row = 6, column = 1, pady=10, sticky=E, padx=(0,10))
    
    root.mainloop()
