#7zr e -p123 awh.7z

import subprocess

passwords = []
passwordsplain = []
with open('key.txt','r') as keyfile:
    passwords = keyfile.readlines()

print(passwords)

for p in passwords:
    passwordsplain.append(p.strip())

print(passwordsplain)

archive_filename = "awh.7z"
found = False

for pp in passwordsplain: 
    command = ["7zr", "e", f"-p{pp}", archive_filename]

    try:
        print(f'now trying password: {pp}')
        subprocess.run(command, check=True)
        print("Extraction successful")
        break
    except subprocess.CalledProcessError as e:
        print(f"Extraction failed with exit code {e.returncode}")

if not found:
    print('Failed to extract! Need to add more passwords')