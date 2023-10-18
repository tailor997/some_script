import os
import subprocess

def compile_keil_project(project_path):
    # 使用uv4命令行工具编译工程
    command = f"C:\\Keil_v5\\UV4\\uv4.exe -b {project_path} -o compile_output.log"

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if process.returncode == 0:
        print(f"编译成功: {project_path}")
    else:
        print(f"编译失败: {project_path}")
        if error:
            print(f"错误信息: {error.decode('utf-8')}")
        if output:
            print(f"输出信息: {output.decode('utf-8')}")

    # # Check if the compile_output.log file exists before trying to open it
    # if os.path.exists("compile_output.log"):
    #     with open("compile_output.log", "r") as f:
    #         log_content = f.read()
    #         print(f"LOG for {project_path}:\n{log_content}")
    # else:
    #     print(f"警告: 未找到 compile_output.log 文件为 {project_path}")


def main():
    #base_dir = "."  # 当前目录，你可以更改为其他目录
    # base_dir = r"D:\_Pro2023\Py\pythonProject\Modify_keil_xml\KeilProject0"  # 当前目录，你可以更改为其他目录
    base_dir = r"C:\Doc\pan1080-dk-internal\03_MCU\mcu_samples_hal"  # 当前目录，你可以更改为其他目录

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".uvproj") or file.endswith(".uvprojx"):  # Keil 工程的扩展名通常为 .uvproj 或 .uvprojx
                full_path = os.path.join(root, file)
                compile_keil_project(full_path)


if __name__ == "__main__":
    main()
