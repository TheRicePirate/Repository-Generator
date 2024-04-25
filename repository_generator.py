from github import Github

class RepoGenerator:
    def __init__(self, repo_name, file_name, username, authkey, org_name, full_name, date):
        self.org_name = org_name
        self.repo_name = repo_name
        self.full_name = full_name
        self.date = date
        self.file_name = file_name
        self.username = username
        self.authkey = authkey
        self.github = Github(username, authkey)
        self.java_ssh_key = ""
        self.swift_ssh_key = ""
        self.java_file_contents = f"""
package com.example;

/**
 * Change me.
 *
 * @author {self.full_name}
 * @version 1.0
 * @since {self.date}
 */

// {self.file_name} class
public final class {self.file_name} {{

    /** Private constructor to prevent instantiation. */
    private {self.file_name}() {{
        throw new UnsupportedOperationException("Cannot instantiate");
    }}

    /**
     * This is the main method.
     *
     * @param args Unused
     */
    public static void main(final String[] args) {{
        System.out.println("Hello, world");
    }}
}}
"""
        self.swift_file_contents = f"""
//  {self.file_name}.swift
//
//  Created by {self.full_name}
//  Created on {self.date}
//  Version 1.0
//  Copyright (c) {self.full_name}. All rights reserved.
//
//  Change me.
"""

    def generate_java_repository(self):
        # Get the organization
        organization = self.github.get_organization(f"ICS4U-Programming-{self.org_name}")

        repo_name = self.repo_name.replace("Swift", "Java")

        # Create repository in the organization
        repository = organization.create_repo(repo_name, private=False)

        read_me_java = "# " + repo_name + "\n\n" + f"[![Mr Coxall's Super Linter](https://github.com/ICS4U-Programming-{self.org_name}/{repo_name}/workflows/Mr%20Coxall's%20Super%20Linter/badge.svg)](https://github.com/ICS4U-Programming-{self.org_name}/{repo_name}/actions/)"

        # repository = self.github.get_user().create_repo(self.repo_name, private=False)
        repository.create_file("README.md", "Initial commit", read_me_java)

        with open("Java Config/workflow_content.txt", "r") as file:
            workflow_content = file.read()
        with open("Java Config/java_gitignore_content.txt", "r") as file:
            gitignore_content = file.read()
        with open("Java Config/package-info.txt", "r") as file:
            pkg_info = file.read()

        repository.create_file(".github/workflows/main.yml", "Initial commit", workflow_content)
        repository.create_file(".gitignore", "Initial commit", gitignore_content)
        repository.create_file("com/example/package-info.java", "Initial commit", pkg_info)
        repository.create_file(f"com/example/{self.file_name}.java", "Initial commit", self.java_file_contents)
        repository.create_file(("com/example/input.txt"), "Initial commit", "")
        repository.create_file(("com/example/output.txt"), "Initial commit", "")

        self.java_ssh_key = repository.ssh_url

        print(f"JAVA - Repository key: {repository.ssh_url}")

    def generate_swift_repository(self):
        # Get the organization
        organization = self.github.get_organization(f"ICS4U-Programming-{self.org_name}")

        repo_name = self.repo_name.replace("Java", "Swift")

        # Create repository in the organization
        repository = organization.create_repo(repo_name, private=False)

        read_me_swift = "# " + repo_name + "\n\n" + f"[![SwiftLint](https://github.com/ICS4U-Programming-{self.org_name}/{repo_name}/workflows/SwiftLint/badge.svg)](https://github.com/ICS4U-Programming-{self.org_name}/{repo_name}/actions/)"

        # repository = self.github.get_user().create_repo(self.repo_name, private=False)
        repository.create_file("README.md", "Initial commit", read_me_swift)

        with open("Swift Config/workflow_content.txt", "r") as file:
            workflow_content = file.read()
        with open("Swift Config/swift_gitignore_content.txt", "r") as file:
            gitignore_content = file.read()

        repository.create_file(".github/workflows/main.yml", "Initial commit", workflow_content)
        repository.create_file(".gitignore", "Initial commit", gitignore_content)
        repository.create_file(f"{self.file_name}.swift", "Initial commit", self.swift_file_contents)
        repository.create_file("input.txt"), "Initial commit", ""
        repository.create_file("output.txt"), "Initial commit", ""
        self.swift_ssh_key = repository.ssh_url
        print(f"SWIFT - Repository key: {repository.ssh_url}")

    def retrieve_ssh_keys(self):
        print(f"\n\n\n\n\n\n\n\ngit clone {self.java_ssh_key}; git clone {self.swift_ssh_key}")
        print("COPY ABOVE GIT CLONE COMMAND TO CLIPBOARD. OPEN TARGET FOLDER IN TERMINAL AND PASTE.")
