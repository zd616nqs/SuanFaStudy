from absl import app
import os
import sys

# 添加父文件夹到模块搜索路径
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  
sys.path.append(root_dir)

from StudyEntry import main_study

app.run(main_study)


