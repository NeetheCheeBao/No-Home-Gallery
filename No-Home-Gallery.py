import tkinter as tk
from tkinter import ttk, messagebox, Menu
import winreg
import os
import ctypes
import webbrowser

REG_PATH_TEMPLATE = r"Software\Classes\CLSID\{}"

TARGETS = {
    "主文件夹 (Home)": "{f874310e-b6b7-47dc-bc84-b9e6b38f5903}",
    "图库 (Gallery)": "{e88865ea-0e1c-4e20-9aa6-edcd0212c87c}"
}

def set_dpi_awareness():
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

class ExplorerCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("主文件夹和图库隐藏工具1.0.0")
        
        self.root.geometry("500x480")
        self.root.minsize(450, 400)
        self.root.resizable(True, True)

        self.create_menu()

        main_frame = ttk.Frame(root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_controls(main_frame)

        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        restart_btn = ttk.Button(bottom_frame, text="重启资源管理器 (立即生效)", command=self.restart_explorer)
        restart_btn.pack(fill=tk.X, pady=5)

        self.status_var = tk.StringVar()
        self.status_var.set("准备就绪")
        
        status_bar = tk.Label(root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        menubar.add_command(label="项目地址", command=self.open_github)

    def open_github(self):
        url = "https://github.com/NeetheCheeBao/No-Home-Gallery"
        webbrowser.open(url)

    def create_controls(self, parent):
        for name, clsid in TARGETS.items():
            frame = ttk.LabelFrame(parent, text=name, padding=15)
            frame.pack(fill=tk.X, pady=8)

            btn_hide = ttk.Button(frame, text="隐藏 (Delete)", command=lambda c=clsid, n=name: self.set_visibility(c, 0, n))
            btn_hide.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=8)

            btn_show = ttk.Button(frame, text="显示 (Restore)", command=lambda c=clsid, n=name: self.set_visibility(c, 1, n))
            btn_show.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=8)

    def set_visibility(self, clsid, value, name):
        try:
            reg_path = REG_PATH_TEMPLATE.format(clsid)
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, reg_path)
            winreg.SetValueEx(key, "System.IsPinnedToNameSpaceTree", 0, winreg.REG_DWORD, value)
            winreg.CloseKey(key)
            action = "已显示" if value == 1 else "已隐藏"
            self.status_var.set(f"成功: {name} {action}")
            self.notify_shell_change()
            
        except Exception as e:
            messagebox.showerror("错误", f"修改注册表失败:\n{str(e)}")
            self.status_var.set("操作失败")

    def notify_shell_change(self):
        try:
            ctypes.windll.user32.PostMessageW(0xFFFF, 0x0111, 41504, 0) 
        except:
            pass

    def restart_explorer(self):
        confirm = messagebox.askyesno("确认", "这将短暂关闭并重启桌面和文件夹窗口。\n是否继续？")
        if confirm:
            self.status_var.set("正在重启资源管理器...")
            self.root.update()
            os.system("taskkill /f /im explorer.exe & start explorer.exe")
            self.status_var.set("资源管理器已重启")

if __name__ == "__main__":
    set_dpi_awareness()
    
    root = tk.Tk()
    app = ExplorerCleanerApp(root)
    root.mainloop()