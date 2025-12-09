'''
This py file will be called by main.py and implement any user inputs necessary for
    execution of file and will implement input validation as a security measure.
'''

'''
Import necessary Libraries
'''
import re

class UserInputs():
    '''
    OpenAI API Key with security input validation
    '''
    def OpenAI_key(self):
        checks_passed_or_exit = False
        while not checks_passed_or_exit:
            # Ensure OpenAI API key starts with "sk-" and accepts any displayable characters afterwards
            API_KEY_PATTERN = r"^sk-.{10,}$"
            # Characters commonly used in SQL or XML injection attacks
            DISALLOWED_CHARS = [";", "/*", "*/", "'", "\"", "<", ">", "&", "%", "\\"]
            # Establish regex for input validation of OpenAI API Key
            OpenAI_key = input('What is your OpenAI API Key?\n')
            # Detect any disallowed characters
            disallowed = ''.join([char if char in OpenAI_key else '' for char in DISALLOWED_CHARS])
            # Check is user has chosen to exit the system
            if OpenAI_key.lower() == 'exit':
                print('You have chosen to exit the system')
                checks_passed_or_exit = True
            # Validate user entered OpenAI API key against regex expected pattern
            elif not re.match(API_KEY_PATTERN, OpenAI_key):
                print('This is an invalid OpenAI API Key, please re-enter or type "exit" to exit program')
            # Check for any disallowed characters to prevent common injection attacks
            elif len(disallowed) >0:
                print(f'The following disallowed characters were found in your key: {disallowed}\n')
                print('Please enter a key using only the appropriate characters or type "exit" to exit program:')
            # User entered key has passed validations and can be used in system
            else:
                print(OpenAI_key)
                checks_passed_or_exit = True

    '''
    Log Analytics workspace ID with security validation
    '''

# Temporary call to check class execution
this_user = UserInputs()
this_user.OpenAI_key()
this_user.