import subprocess
import requests

def start_server(server_path:str):
    process = subprocess.Popen(
        ["node", server_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return process	

def check_server_status():
    try:
        response = requests.get('http://localhost:8000')
        return response.status_code == 200
    except requests.ConnectionError:
        return False

print(check_server_status())