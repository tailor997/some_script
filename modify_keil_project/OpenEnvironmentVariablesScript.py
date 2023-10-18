#打开环境变量编辑器的命令


# 导入os模块，用于与操作系统交互
import os

# 使用os.system函数运行Windows环境变量编辑器的命令
# "rundll32 sysdm.cpl,EditEnvironmentVariables"是打开环境变量编辑器的命令
os.system("rundll32 sysdm.cpl,EditEnvironmentVariables")