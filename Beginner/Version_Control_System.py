t = int(input())

for i in range(t):
    total_file, ignored_file, tracked_file = map(int, input().split())
    ignored_seq = set(map(int, input().split()))
    tracked_seq = set(map(int, input().split()))

    files = set(range(1, total_file + 1))
    tracked_ignored = ignored_seq.intersection(tracked_seq)
    untracked_files = files.difference(tracked_seq)
    unignored_file = files.difference(ignored_seq)

    untracked_unignored = untracked_files.intersection(unignored_file)
    print(len(tracked_ignored), len(untracked_unignored))
