# Repository-Generator

Repository generator for ICS4U.

## HOW TO USE:

### GET AN AUTH KEY:
1. Go to your Github account settings, select developer settings, select personal access tokens, then select Tokens (classic).
2. Hit generate new token and select classic.
3. Set the expiration to 'no expiration'
4. Check the 'repo' box
5. Hit generate new token and COPY the key. **Make sure you do not lose it**.

### SETUP:
1. Clone this repository into your codespace.
2. Open a terminal window in the repository's folder and paste this command in: `pip install PyGithub pyperclip`
4. Run the program using the command `python main.py`.
5. Follow the instructions.

### USE:
1. Run main.py
2. Choose the language you want to clone for.
3. Enter the name of the repository as is from the google doc (e.g "ICS4U-Testrepo-Java")
4. Enter the name of the actual program file (do not enter file formats like .java or .swift)
5. The repositories will be generated and it will print a command for you to copy and paste.
6. This command is to clone the github repositories, so paste it in the right codespaces folder.
