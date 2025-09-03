import praw

# Configurações do Reddit
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    username='',
    password='',
    user_agent='Crossposting'
)

entry_path = r""
exit_path = r""


subs_crosspostable = []

with open(entry_path, "r", encoding='utf-8') as f:
    list_subs = [linha.strip() for linha in f if linha.strip()]

print(f"Analyzing a list of {len(list_subs)} subreddits...\n")


for name_sub in list_subs:
    try:
        sub = reddit.subreddit(name_sub)
        if sub.is_crosspostable_subreddit:
            print(f"[✔] {name_sub} allows crossposting")
            subs_crosspostable.append(name_sub)
        else:
            print(f"[✘] {name_sub} does NOT allow crossposting")
    except Exception as e:
        print(f"[ERROR] Could not analyze {name_sub}: {e}")


with open(exit_path, "w", encoding='utf-8') as f:
    for sub in subs_crosspostable:
        f.write(sub + "\n")

print(f"\n✅ Analysis completed. Result saved in: {exit_path}")
