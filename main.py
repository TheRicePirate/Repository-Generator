from github import Github
from repository_generator import RepoGenerator
from datetime import datetime
import os
import json

def main():

    reset_setup = input("Hit ENTER to generate repositories. Hit 1 to restart the setup wizard.\n>> ")
    if reset_setup != "":
        setup_wizard()

    print("Generate for:\n1. Java\n2. Swift\n3. Both")
    generate_choice = input("Enter the list number: ")

    repository_name = input("Enter the name of the repository: ").replace(" ", "-")
    date = datetime.today().strftime('%Y-%m-%d')
    file_name = input("Enter the name of the program (don't add file formats): ")

    repo_gen = initialize_repo_generator(repository_name, file_name, date=date)


    if generate_choice == "1":
        repo_gen.generate_java_repository()

    elif generate_choice == "2":
        repo_gen.generate_swift_repository()
    
    elif generate_choice == "3":
        repo_gen.generate_java_repository()
        repo_gen.generate_swift_repository()

    repo_gen.retrieve_ssh_keys()

def initialize_repo_generator(repository_name, file_name, date):
    data_file_path = os.path.join(os.path.dirname(__file__), "base_info.json")
    if os.path.exists(data_file_path):
        setup_data = retrieve_base_info()
        repo_gen = RepoGenerator(repository_name, file_name, username=setup_data["username"], authkey=setup_data["authkey"], org_name=setup_data["organization_name"], full_name=setup_data["full_name"], date=date)
    else:
        print("Running the setup wizard")
        setup_wizard()
        setup_data = retrieve_base_info()
        repo_gen = RepoGenerator(repository_name, file_name, username=setup_data["username"], authkey=setup_data["authkey"], org_name=setup_data["organization_name"], full_name=setup_data["full_name"], date=date)

    return repo_gen

def setup_wizard():
    organization_name = input("Enter your name with initials (e.g: EricB): ")
    full_name = input("Enter your full name (e.g: Eric Barker): ")
    username = input("Enter your github username: ")
    authkey = input("Enter your authkey: ")

    setup_data = {
        "organization_name": organization_name,
        "full_name": full_name,
        "username": username,
        "authkey": authkey
    }

    with open("base_info.json", "w") as json_file:
        json.dump(setup_data, json_file)
    print("\n\n\n\n\n\n\n\n\n\n\n")

def retrieve_base_info():
    with open("base_info.json", "r") as json_file:
        setup_data = json.load(json_file)

    return setup_data


if __name__ == "__main__":
    main()
