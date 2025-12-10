'''
This py file will be called by main.py and implement any user inputs necessary for
    execution of file and will implement input validation as a security measure.
'''

'''
Import necessary Libraries
'''
import re

# Function to check for characters that are frequently used for injection
def bad_char_inp_val(inp):
    # Characters commonly used in SQL or XML injection attacks
    DISALLOWED_CHARS = [";", "/*", "*/", "'", "\"", "<", ">", "&", "%", "\\"]
    # Collect any bad characters that are present in input
    disallowed = ''.join([char if char in inp else '' for char in DISALLOWED_CHARS])
    # return true if there are any bad characters
    return disallowed

# Function to check whether the user input matches the expected pattern
def pattern_match(inp, regex_pattern):
    return re.match(regex_pattern, inp)

# Class for validated user input
class UserInputs():
    '''
    OpenAI API Key with security input validation
    '''
    def __init__(self, platform, pattern):
        self.platform = platform
        self.pattern = pattern
    # Method to validate input
    def validate_inp(self):
        # Establish passed or exit status
        checks_passed_or_exit = False
        # Establish number of login attempts
        count = 0
        # Enter prompt loop
        while not checks_passed_or_exit and count<5:
            # Prompt user for input
            self.inp = input(f'What is your {self.platform}?\n (Input cannot contain any of the following characters ;*/\'"<>&%\)')
            # Detect any disallowed characters
            bad_chars = bad_char_inp_val(self.inp)
            # Exit system if user enters "exit"
            if self.inp.lower() == 'exit':
                print('You have chosen to exit the system')
                self.inp = None
                count += 1
                checks_passed_or_exit = True
            # Notify user if any bad characters were found in input and prompt to re-enter
            elif len(bad_chars) > 0:
                print(f'The following disallowed characters were found in your input: {bad_chars}\n')
                print('Please enter an input using only the appropriate characters or type "exit" to exit program:')
                count += 1
            # Validate user input against expected pattern
            elif not pattern_match(self.inp, self.pattern):
                print(f'This is an invalid {self.platform} input, please re-enter or type "exit" to exit program')
                count += 1
            # exit loop if validations have passed
            else:
                checks_passed_or_exit = True
        # Print validated input
        return None if count>=5 else self.inp



