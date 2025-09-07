# Importing libraries
import os

# Change to your Dropbox folder path (where x is your user)
dropbox_dir = r"C:\Users\x\Dropbox" 

# List of files to back up (In my case, files are in "projekty" folder, and then in their respective subfolders, but you can change it to whatever you want)
FILES_TO_BACKUP = [
    r"C:\projekty\math-philosophy-password-generator\password.txt",
    r"C:\projekty\mecze-ics\matches.ics",
    r"C:\projekty\User Registration and Login System\audit.log.txt",
    r"C:\projekty\User Registration and Login System\users.txt"
]

# Function to back up files
def backup_files():
    for local_file in FILES_TO_BACKUP:
        fname = os.path.basename(local_file)
        dropbox_file = os.path.join(dropbox_dir, fname)

        print(f"🔍 Copying from: {local_file}")
        print(f"   To: {dropbox_file}")

        if os.path.exists(local_file):
            with open(local_file, "r", encoding="utf-8") as f_in:
                content = f_in.read()
            with open(dropbox_file, "w", encoding="utf-8") as f_out:
                f_out.write(content)

            print(f"✅ Copied {fname} → {dropbox_file}")
        else:
            print(f"⚠️ File not found {local_file}, skipping")

if __name__ == "__main__":
    backup_files()