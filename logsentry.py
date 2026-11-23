import re

pattern = re.compile(
    r"(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"LOGIN user=(?P<user>\S+) "
    r"ip=(?P<ip>\d+\.\d+\.\d+\.\d+) "
    r"status=(?P<status>SUCCESS|FAILED)"
)

entries = []
skipped = 0
total_lines = 0

with open("sample_auth.log", "r") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        print("Reading: ",line)
        total_lines += 1
        match = pattern.search(line)
        if match:
            entries.append(match.groupdict())
        else:
            skipped += 1

success_count = 0
failed_count = 0

for entry in entries:
    if entry["status"] == "SUCCESS":
        success_count += 1
    else:
        failed_count += 1

print("Total lines:", total_lines)
print("Parsed lines:", len(entries))
print("Successful logins:", success_count)
print("Failed logins:", failed_count)
print("Skipped (bad) lines:", skipped)