import os
from os import stat_result
path = 'c:/users/pc/desktop/courses/'
file_stats: stat_result = os.stat(path)
print(file_stats)


