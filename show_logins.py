import re

pattern = re.compile(
    r"(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"LOGIN user=(?P<user>\S+) "
    r"ip=(?P<ip>\d+\.\d+\.\d+\.\d+) "
    r"status=(?P<status>SUCCESS|FAILED)"
)

entries = []

with open("sample_auth.log", "r") as f:
    for line in f:
        match = pattern.search(line.strip())
        if match:
            entries.append(match.groupdict())

print("SUCCESSFUL LOGINS:")
for entry in entries:
    if entry["status"] == "SUCCESS":
        print(entry["time"], entry["user"], entry["ip"])

print()
print("FAILED LOGINS:")
for entry in entries:
    if entry["status"] == "FAILED":
        print(entry["time"], entry["user"], entry["ip"])