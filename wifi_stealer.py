import subprocess
import re

def get_wifi_passwords():
    profiles = subprocess.check_output("netsh wlan show profiles").decode()
    profiles = re.findall(r"All User Profile\s+:\s(.*)", profiles)
    passwords = {}
    for profile in profiles:
        profile = profile.strip()
        try:
            password = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear').decode()
            password = re.search(r"Key Content\s+:\s(.*)", password).group(1).strip()
            passwords[profile] = password
        except:
            passwords[profile] = "No password"
    return passwords

if __name__ == "__main__":
    passwords = get_wifi_passwords()
    with open("wifi_passwords.txt", "w") as f:
        for ssid, pwd in passwords.items():
            f.write(f"SSID: {ssid} | Password: {pwd}\n")
