import subprocess

git_reflog = subprocess.check_output(["git", "reflog"], encoding = "utf-8")
git_hashes = list(map(lambda s : s[0:7], git_reflog.split("\n")))[0:-1]

for hash in git_hashes :
    git_show = subprocess.check_output(["git", "show"], encoding = "utf-8")
    if "flag{" in git_show :
        print(f"Processing with git commit {hash}:")
        print(git_show + "\n")
