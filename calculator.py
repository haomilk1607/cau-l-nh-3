import tkinter as tk
from tkinter import messagebox

def kiem_tra_so(value):
    """Kiểm tra xem giá trị nhập vào có phải là số tự nhiên không"""
    try:
        if value == "":
            return True
        num = int(value)
        return num >= 0
    except ValueError:
        return False

def tinh_toan(phep_tinh):
    """Thực hiện phép tính dựa trên hai số đã nhập"""
    try:
        # Lấy giá trị từ ô nhập liệu và chuyển thành số
        so_thu_nhat = int(o_nhap_so_1.get())
        so_thu_hai = int(o_nhap_so_2.get())
        
        # Thực hiện phép tính tương ứng
        if phep_tinh == '+':
            ket_qua = so_thu_nhat + so_thu_hai
        elif phep_tinh == '-':
            ket_qua = so_thu_nhat - so_thu_hai
        elif phep_tinh == 'x':
            ket_qua = so_thu_nhat * so_thu_hai
        elif phep_tinh == '÷':
            # Kiểm tra chia cho 0
            if so_thu_hai == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0!")
                return
            ket_qua = so_thu_nhat / so_thu_hai
            
        # Hiển thị kết quả
        nhan_ket_qua.config(text=f"Kết quả: {ket_qua}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số tự nhiên hợp lệ!")

# Tạo cửa sổ chính
cua_so = tk.Tk()
cua_so.title("Máy Tính Đơn Giản")
cua_so.geometry("400x500")
cua_so.configure(bg='#f0f0f0')

# Tạo và cấu hình style
style_nut = {'font': ('Arial', 12), 'width': 5, 'height': 1, 'bg': '#4CAF50', 'fg': 'white'}
style_nhan = {'font': ('Arial', 12), 'bg': '#f0f0f0'}

# Tạo tiêu đề
tieu_de = tk.Label(cua_so, 
                  text="MÁY TÍNH ĐƠN GIẢN", 
                  font=('Arial', 16, 'bold'), 
                  bg='#f0f0f0')
tieu_de.pack(pady=20)

# Tạo hướng dẫn
huong_dan = tk.Label(cua_so, 
                    text="Nhập hai số tự nhiên và chọn phép tính:", 
                    **style_nhan)
huong_dan.pack(pady=10)

# Khung chứa số thứ nhất
khung_so_1 = tk.Frame(cua_so, bg='#f0f0f0')
khung_so_1.pack(pady=10)
tk.Label(khung_so_1, text="Số thứ nhất:", **style_nhan).pack(side=tk.LEFT, padx=5)
o_nhap_so_1 = tk.Entry(khung_so_1, font=('Arial', 12), validate='key')
o_nhap_so_1['validatecommand'] = (o_nhap_so_1.register(kiem_tra_so), '%P')
o_nhap_so_1.pack(side=tk.LEFT)

# Khung chứa số thứ hai
khung_so_2 = tk.Frame(cua_so, bg='#f0f0f0')
khung_so_2.pack(pady=10)
tk.Label(khung_so_2, text="Số thứ hai:  ", **style_nhan).pack(side=tk.LEFT, padx=5)
o_nhap_so_2 = tk.Entry(khung_so_2, font=('Arial', 12), validate='key')
o_nhap_so_2['validatecommand'] = (o_nhap_so_2.register(kiem_tra_so), '%P')
o_nhap_so_2.pack(side=tk.LEFT)

# Khung chứa các nút phép tính
khung_nut = tk.Frame(cua_so, bg='#f0f0f0')
khung_nut.pack(pady=20)

# Tạo các nút phép tính
tk.Button(khung_nut, text="+", command=lambda: tinh_toan('+'), **style_nut).pack(side=tk.LEFT, padx=5)
tk.Button(khung_nut, text="-", command=lambda: tinh_toan('-'), **style_nut).pack(side=tk.LEFT, padx=5)
tk.Button(khung_nut, text="x", command=lambda: tinh_toan('x'), **style_nut).pack(side=tk.LEFT, padx=5)
tk.Button(khung_nut, text="÷", command=lambda: tinh_toan('÷'), **style_nut).pack(side=tk.LEFT, padx=5)

# Nhãn hiển thị kết quả
nhan_ket_qua = tk.Label(cua_so, 
                       text="Kết quả: ", 
                       font=('Arial', 14, 'bold'), 
                       bg='#f0f0f0')
nhan_ket_qua.pack(pady=20)

# Chạy chương trình
cua_so.mainloop()