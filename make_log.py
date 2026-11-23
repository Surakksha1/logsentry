import random

users = ["alice", "bob", "carol", "dave", "eve", "frank"]
statuses = ["SUCCESS", "FAILED"]

with open("sample_auth.log", "w") as f:
    for i in range(55):
        minute = i // 2
        second = random.randint(0, 59)
        user = random.choice(users)
        ip = "192.168.1." + str(random.randint(2, 60))
        status = random.choice(statuses)
        f.write(f"2026-11-22 08:{minute:02d}:{second:02d} LOGIN user={user} ip={ip} status={status}\n")

    # broken lines for testing
    f.write("this is a broken line\n")
    f.write("2026-11-22 09:00:00 LOGIN user=bob\n")
    # one good line with a dot in the username
    f.write("2026-11-22 09:10:00 LOGIN user=john.doe ip=192.168.1.99 status=FAILED\n")