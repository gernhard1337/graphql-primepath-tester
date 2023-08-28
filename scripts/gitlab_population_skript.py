import requests
import random
import string

# Setzen Sie Ihren persönlichen Zugangstoken und die GitLab-URL hier
TOKEN = "3Yzwxep5AQwjXrff7bPE"
GITLAB_URL = "http://localhost"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


NAMES = ["Alice", "Bob", "Charlie", "David"]
EMAIL_DOMAINS = ["example.com", "mail.com", "demo.net"]
PROJECT_LANGUAGES = ["Python", "JavaScript", "Java", "Ruby"]
ISSUE_LABELS = ["bug", "feature", "documentation"]


LANGUAGE_FILES = {
    "Python": "main.py",
    "JavaScript": "app.js",
    "Java": "Main.java",
    "Ruby": "main.rb"
}


def create_group(group_name):
    data = {
        "name": group_name,
        "path": group_name.lower(),
        "visibility": "public"
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/groups', headers=HEADERS, json=data)
    return response.json()["id"]


def add_user_to_group(group_id, user_id):
    data = {
        "user_id": user_id,
        "access_level": 30  # Developer level
    }
    requests.post(f'{GITLAB_URL}/api/v4/groups/{group_id}/members', headers=HEADERS, json=data)


def create_namespace_project(namespace_id, project_name, language):
    data = {
        "name": project_name,
        "namespace_id": namespace_id,
        "description": f"A sample {language} project.",
        "visibility": "public"
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/projects', headers=HEADERS, json=data)
    return response.json()["id"]


def create_file(project_id, filename, content):
    data = {
        "branch": "master",
        "commit_message": f"Add {filename}",
        "actions": [
            {
                "action": "create",
                "file_path": filename,
                "content": content
            }
        ]
    }
    requests.post(f'{GITLAB_URL}/api/v4/projects/{project_id}/repository/commits', headers=HEADERS, json=data)


def create_issue_comment(project_id, issue_id, comment):
    data = {
        "body": comment
    }
    requests.post(f'{GITLAB_URL}/api/v4/projects/{project_id}/issues/{issue_id}/notes', headers=HEADERS, json=data)


def create_user(username):
    email = f"{username}@{random.choice(EMAIL_DOMAINS)}"
    data = {
        "email": email,
        "password": "securepassword123",
        "username": username,
        "name": username,
        "avatar_url": "https://example.com/avatar.png",
        "bio": "This is a sample bio."
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/users', headers=HEADERS, json=data)
    return response.json()["id"]


def create_project(user_id, project_name):
    data = {
        "name": project_name,
        "namespace_id": user_id,
        "description": f"A sample {random.choice(PROJECT_LANGUAGES)} project.",
        "visibility": random.choice(["public", "private"])
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/projects', headers=HEADERS, json=data)
    return response.json()["id"]


def create_issue(project_id, title):
    data = {
        "title": title,
        "description": f"This is a sample issue for {title}",
        "labels": random.choice(ISSUE_LABELS)
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/projects/{project_id}/issues', headers=HEADERS, json=data)
    return response.json()["id"]


def assign_project_to_user(project_id, user_id):
    data = {
        "user_id": user_id,
        "access_level": 30  # Developer level
    }
    requests.post(f'{GITLAB_URL}/api/v4/projects/{project_id}/members', headers=HEADERS, json=data)


def create_snippet(user_id, title):
    data = {
        "title": title,
        "file_name": f"{title}.txt",
        "content": "This is a sample snippet content.",
        "visibility": "public",
        "author_id": user_id
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/snippets', headers=HEADERS, json=data)
    return response.json()["id"]


def create_branch(project_id, branch_name):
    data = {
        "branch": branch_name,
        "ref": "master"  # Erstelle den neuen Branch von 'master'
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/projects/{project_id}/repository/branches', headers=HEADERS, json=data)
    return response.status_code == 201  # Erfolg bei 201


def create_merge_request(project_id, source_branch, target_branch, title):
    data = {
        "source_branch": source_branch,
        "target_branch": target_branch,
        "title": title
    }
    response = requests.post(f'{GITLAB_URL}/api/v4/projects/{project_id}/merge_requests', headers=HEADERS, json=data)
    return response.json()["id"]


def main():
    # Gruppen erstellen
    groups = [f"GroupX_{i}" for i in range(5)]
    group_ids = [create_group(group_name) for group_name in groups]
    user_ids = []

    for i in range(50):
        username = f"{random.choice(NAMES)}_{i}"
        user_id = create_user(username)

        # Füge Benutzer zu Gruppen hinzu
        for group_id in random.sample(group_ids, random.randint(1, len(group_ids))):
            add_user_to_group(group_id, user_id)

        project_count = random.randint(1, 10)
        for j in range(project_count):
            language = random.choice(PROJECT_LANGUAGES)
            project_name = f"projectX_{i}_{j}"
            namespace_id = random.choice(group_ids)
            project_id = create_namespace_project(namespace_id, project_name, language)

            # Projekt einem Benutzer zuweisen
            assign_project_to_user(project_id, user_id)

            create_file(project_id, "README.md", f"# {project_name}\nThis is a sample README for {project_name}.")
            create_file(project_id, LANGUAGE_FILES[language], "")  # Leere Datei entsprechend der Programmiersprache
            # Merge Request
            if random.choice([True, False]):
                branch_name = f"featureX_{i}_{j}"
                if create_branch(project_id, branch_name):
                    # Ändern Sie eine Datei in diesem Branch (z.B. die README.md)
                    create_file(project_id, "README.md",
                                f"# {project_name}\nThis README was updated in the {branch_name} branch.")

                    # Erstelle den Merge Request
                    create_merge_request(project_id, branch_name, "master", f"Merge {branch_name} to master")

            # Issues und Kommentare erstellen
            if random.choice([True, False]):
                issue_title = f"Issue for {project_name}"
                issue_id = create_issue(project_id, issue_title)
                create_issue_comment(project_id, issue_id, "This is a sample comment.")

        # Snippet erstellen
        snippet_title = f"Snippet_{i}"
        create_snippet(user_id, snippet_title)



if __name__ == "__main__":
    main()