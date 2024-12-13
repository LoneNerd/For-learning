import os
import tkinter as tk
from tkinter import messagebox

def rename_files():
    directory = entry_directory.get()
    old_string = entry_old_string.get()
    new_string = entry_new_string.get()
    
    success = True

    try:
        for filename in os.listdir(directory):
            if old_string in filename:
                old_file = os.path.join(directory, filename)
                new_filename = filename.replace(old_string, new_string)
                new_file = os.path.join(directory, new_filename)
                os.rename(old_file, new_file)
    except Exception as e:
        success = False
        messagebox.showerror("Lỗi", f"Đổi tên không thành công: {str(e)}")
    
    if success:
        messagebox.showinfo("Thành công", "Đã hoàn thành đổi tên các tệp!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đổi tên tệp")

# Tạo và bố trí các nhãn và ô nhập liệu
tk.Label(root, text="Đường dẫn đến thư mục:").grid(row=0, column=0, padx=10, pady=5)
entry_directory = tk.Entry(root, width=50)
entry_directory.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Chuỗi cần thay thế:").grid(row=1, column=0, padx=10, pady=5)
entry_old_string = tk.Entry(root, width=50)
entry_old_string.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Chuỗi mới:").grid(row=2, column=0, padx=10, pady=5)
entry_new_string = tk.Entry(root, width=50)
entry_new_string.grid(row=2, column=1, padx=10, pady=5)

# Nút đổi tên
tk.Button(root, text="Đổi tên", command=rename_files).grid(row=3, column=0, columnspan=2, pady=10)

# Chạy vòng lặp chính của giao diện
root.mainloop()
