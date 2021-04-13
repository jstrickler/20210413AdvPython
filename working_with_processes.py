import psutil

all_pids = psutil.pids()
print(all_pids)
print()

pid = 51975
if psutil.pid_exists(pid):
    proc = psutil.Process(pid)
    print(proc.name())
print('-' * 60)

for pid in psutil.pids():
    try:
        print(pid, psutil.Process(pid).name())
    except Exception:
        pass
