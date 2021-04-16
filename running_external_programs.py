from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob

files = glob('DATA/*.csv')

raw_cmd = "netstat -an"


cmd_words = shlex.split(raw_cmd)

program, *argv = cmd_words

all_words = cmd_words + files
print("all_words:", all_words)

print("cmd_words:", cmd_words, '\n')

run(cmd_words)  # same as os.system(....)  more or less
print('-' * 60)

try:
    proc = run(cmd_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err)
else:
    output = proc.stdout
    errors = proc.stderr
    cmd_lines = output.decode().splitlines()
    for line in cmd_lines:
        if 'ESTAB' in line:
            fields = line.split()
            if len(fields) == 6:
                proto, recq, sendq, local, remote, state = line.split()
                *local_bytes, local_port = local.split('.')
                *remote_bytes, remote_port = remote.split('.')
                print('.'.join(local_bytes), local_port)



