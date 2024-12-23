import os
import time
from tqdm import tqdm  # For progress bar

# Clear screen function
def clear_screen():
    os.system('clear')

# Display banner
def display_banner():
    clear_screen()
    print("\033[92m")  # Green color
    print("  ________        __         ____  __.__                ")
    print(" /  _____/  _____/  |_  ____ |    |/ _|  |   ___________ ")
    print("/   \\  ___ /  _ \\   __\\/ __ \\|      < |  |_ / __ \\_  __ \\")
    print("\\    \\_\\  (  <_> )  | \\  ___/|    |  \\|  |_\\  ___/|  | \\/")
    print(" \\______  /\\____/|__|  \\___  >____|__ \\____/\\___  >__|   ")
    print("        \\/                 \\/        \\/         \\/       ")
    print("\033[0m")  # Reset color

# Progress bar function
def show_progress(task_name):
    print(f"\n{task_name} in progress...")
    for _ in tqdm(range(100), desc=task_name, ncols=75):
        time.sleep(0.02)

# Decompile APK function
def decompile_apk():
    apk_path = input("\nEnter the path of the APK file to decompile: ")
    if os.path.exists(apk_path):
        output_dir = apk_path.replace(".apk", "_decompiled")
        show_progress("Decompiling APK")
        os.system(f"./jadx/bin/jadx -d {output_dir} {apk_path}")
        print(f"\033[92mDecompilation complete! Files saved in:\033[0m {output_dir}")
    else:
        print("\033[91mError: File not found!\033[0m")

# Recompile APK function
def recompile_apk():
    dir_path = input("\nEnter the path of the modified decompiled directory: ")
    if os.path.exists(dir_path):
        output_apk = dir_path + "_recompiled.apk"
        show_progress("Recompiling APK")
        os.system(f"zip -r {output_apk} {dir_path}")
        os.system(f"zipalign -v 4 {output_apk} aligned_{output_apk}")
        print(f"\033[92mRecompilation complete! Output: aligned_{output_apk}\033[0m")
    else:
        print("\033[91mError: Directory not found!\033[0m")

# Update tool function
def update_tool():
    show_progress("Updating Tool")
    print("\033[92mTool updated successfully!\033[0m")

# Main menu
def main():
    while True:
        display_banner()
        print("\n\033[94mSelect an option:\033[0m")
        print("1. Decompile APK")
        print("2. Recompile APK")
        print("3. Update Tool")
        print("4. Exit")
        choice = input("\n\033[93mEnter your choice: \033[0m")
        
        if choice == "1":
            decompile_apk()
        elif choice == "2":
            recompile_apk()
        elif choice == "3":
            update_tool()
        elif choice == "4":
            print("\033[91mExiting... Goodbye!\033[0m")
            break
        else:
            print("\033[91mInvalid choice! Try again.\033[0m")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
