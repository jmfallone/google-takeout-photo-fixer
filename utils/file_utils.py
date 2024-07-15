from datetime import datetime
import time
import platform

def update_file_creation_date(file_path: str, creation_date: datetime) -> None:
    pass


def is_wsl() -> bool:
    try:
        with open('/proc/version', 'r') as f:
            return 'microsoft' in f.read().lower()
    except:
        return False

if platform.system() == 'Windows':
    import pywintypes
    import win32file

    def update_file_creation_date(file_path: str, creation_date: datetime):
        wintime = pywintypes.Time(creation_date)
        handle = win32file.CreateFile(
            file_path, win32file.GENERIC_WRITE, 0, None,
            win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None
        )
        win32file.SetFileTime(handle, wintime, None, None)
        handle.close()

elif is_wsl():
    def update_file_creation_date(file_path: str, creation_date: datetime):
        import subprocess
        # Convert the file path to Windows format
        win_path = subprocess.check_output(['wslpath', '-w', file_path]).decode('utf-8').strip()
        
        # Format the date for PowerShell
        formatted_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")
        
        # Construct the PowerShell command
        ps_command = f'(Get-Item "{win_path}").CreationTime = "{formatted_date}"'
        
        # Execute the PowerShell command
        full_command = ['powershell.exe', '-Command', ps_command]
        
        try:
            subprocess.run(full_command, check=True)
            print(f"Successfully updated creation date for {file_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to update creation date: {e}")

else:
    import xattr

    def update_file_creation_date(file_path: str, creation_date: datetime):
        timespec = time.gmtime(creation_date.timestamp())
        formatted_time = time.strftime('%Y-%m-%dT%H:%M:%S', timespec)
        xattr.setxattr(file_path, 'user.creation_time', formatted_time.encode('utf-8'))