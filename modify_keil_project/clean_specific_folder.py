#目录为"keil"或者"Keil"下
#只保留".uvoptx"和".uvprojx"文件
import os
import shutil


def clean_keil_folders(root_dir):
    # 遍历root_dir中的所有文件和目录
    for dirpath, dirnames, filenames in os.walk(root_dir):

        # 检查当前目录是否为"keil"
        if os.path.basename(dirpath) == "keil" or os.path.basename(dirpath) == "Keil":

            # 遍历该目录下的所有文件
            for file in filenames:

                # 获取文件的完整路径
                file_path = os.path.join(dirpath, file)

                # 如果文件的后缀不是.uvoptx或.uvprojx，删除它
                if not (file.endswith(".uvoptx") or file.endswith(".uvprojx")):
                    try:
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")
                    except Exception as e:
                        print(f"Error deleting file {file_path}: {str(e)}")

            # 删除所有子文件夹
            for subdir in dirnames:
                subdir_path = os.path.join(dirpath, subdir)
                try:
                    shutil.rmtree(subdir_path)
                    print(f"Deleted directory: {subdir_path}")
                except Exception as e:
                    print(f"Error deleting directory {subdir_path}: {str(e)}")


if __name__ == "__main__":
    folder_A = r"D:\_Pro2023\Git\panchip\panplat\pan1070\_hal_release\mcu_samples"
    # folder_A = input("Enter the path to folder A: ")
    clean_keil_folders(folder_A)
    print("Done!")
