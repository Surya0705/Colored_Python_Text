import colorama # Importing the Required Module.
from colorama import Fore # Calling the Fore function from Colorama to print Colored Text.
from colorama import Style # Calling the Style function from Colorama.

print(Fore.MAGENTA + "Colored Text Printed using Colorama Module"+ Style.RESET_ALL) # Printing the Colored Text. This is Way 1 I have RESET the Style at the End so that we can compare Normal Text in the Next Line with this Colored Text.
print("Normal Text for Comparision Purpose.") # Printing Normal Text. Note that this text would also have been Magenta Colored if I wouldn't have put 'Style.RESET_ALL' at the End.
print(f"{Fore.RED}Colored Text Printed using Colorama Module") # Printing the Colored Text. This is Way 2 using f.