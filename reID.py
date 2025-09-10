
"""УТИЛИТА ДЛЯ ПОЛУЧЕНИЯ ID КОНФЕРЕНЦИИ"""

import re

def extract_meet_id(url):
    match = re.search(r"meet\.google\.com/([a-z]{3}-[a-z]{4}-[a-z]{3})", url)
    if match:
        return match.group(1)
    return None

if __name__ == "__main__":
    while True:
        meet_id = extract_meet_id(input(": "))
        print("ID конференции:", meet_id)