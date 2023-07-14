import requests
import random
import string

# Setzen Sie Ihren persönlichen Zugangstoken und die GitLab-URL hier
TOKEN = "your_personal_access_token"
GITLAB_URL = "https://gitlab.example.com"


# Funktion, um zufällige Zeichenfolgen für die Erstellung von Benutzern, Gruppen und Projekten zu generieren
def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


# Funktionen zum Erstellen von Benutzern, Gruppen und Projekten
def create_user(username, email, name, password):
    url = f"{GITLAB_URL}/api/v4/users"
    headers = {'PRIVATE-TOKEN': TOKEN}
    data = {
        "username": username,
        "email": email,
        "name": name,
        "password": password
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()["id"]


def create_group(name):
    url = f"{GITLAB_URL}/api/v4/groups"
    headers = {'PRIVATE-TOKEN': TOKEN}
    data = {
        "name": name,
        "path": name.lower()
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()["id"]


def create_project(name, group_id):
    url = f"{GITLAB_URL}/api/v4/projects"
    headers = {'PRIVATE-TOKEN': TOKEN}
    data = {
        "name": name,
        "namespace_id": group_id
    }
    requests.post(url, headers=headers, data=data)


# Erstellen von 10 Benutzern, Gruppen und Projekten
for i in range(10):
    username = random_string()
    email = f"{username}@example.com"
    name = username
    password = "password123"

    user_id = create_user(username, email, name, password)
    print(f"Created user {user_id}")

    group_name = random_string()
    group_id = create_group(group_name)
    print(f"Created group {group_id}")

    project_name = random_string()
    create_project(project_name, group_id)
    print(f"Created project in group {group_id}")

