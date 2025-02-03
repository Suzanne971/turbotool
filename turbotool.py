import os
import subprocess
import platform

class TurboTool:
    def __init__(self):
        self.system = platform.system()
        if self.system != "Windows":
            raise EnvironmentError("TurboTool is designed to run on Windows platforms only.")

    def welcome_message(self):
        print("Welcome to TurboTool - Your System Recovery Assistant for Windows!")

    def check_disk_space(self):
        print("\nStep 1: Checking Disk Space...")
        try:
            total, used, free = map(int, os.popen('fsutil volume diskfree c:').read().split()[8:13:2])
            print(f"Total: {total // (1024**2)} MB, Used: {used // (1024**2)} MB, Free: {free // (1024**2)} MB")
        except Exception as e:
            print("Error checking disk space:", e)

    def check_system_files(self):
        print("\nStep 2: Checking System Files...")
        try:
            result = subprocess.run(['sfc', '/scannow'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("System file check failed:", e)

    def create_restore_point(self):
        print("\nStep 3: Creating Restore Point...")
        try:
            result = subprocess.run(['powershell', 'Checkpoint-Computer', '-Description', '"TurboTool Restore Point"'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print("Failed to create restore point:", e)

    def run(self):
        self.welcome_message()
        self.check_disk_space()
        self.check_system_files()
        self.create_restore_point()
        print("\nSystem recovery steps completed. Please restart your computer if necessary.")

if __name__ == "__main__":
    try:
        tool = TurboTool()
        tool.run()
    except EnvironmentError as e:
        print(e)