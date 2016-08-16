
import os
from subprocess import run, PIPE


git_path = r'C:\Users\jf\AppData\Local\Atlassian\SourceTree\git_local\bin'



s = b'------------------------------------------------------------------------\r\nr550 | lvfangfang | 2016-07-29 10:26:24 +0800 (\xd6\xdc\xce\xe5, 29 \xc6\xdf\xd4\xc2 2016) | 1 line\r\n\r\n\xd4\xf6\xbc\xd3HIF_SPI\xd0\xad\xd2\xe92 (\xce\xb4\xcd\xea\xb4\xfd\xd0\xf8\xa3\xa9\r\n------------------------------------------------------------------------\r\n'
log = s.decode('gbk')

os.environ['PATH'] += ';' + git_path
run('git add -A', shell=True)
print("git commit -m '%s'" % log)
run("git commit -m '%s'" % log, shell=True)
run('git push', shell=True)

