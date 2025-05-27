# Import các thư viện cần thiết
from mnemonic import Mnemonic  # Thư viện để tạo cụm từ ghi nhớ
from eth_account import Account  # Thư viện để tạo ví Ethereum

def tao_vi_ethereum():
    try:
        # Bước 1: Tạo cụm từ ghi nhớ (mnemonic) ngẫu nhiên
        # Sử dụng tiếng Anh và tạo 12 từ (độ dài 128 bit)
        mnemo = Mnemonic("english")
        cum_tu_ghi_nho = mnemo.generate(strength=128)
        
        # Bước 2: Kích hoạt tính năng tạo ví từ mnemonic
        Account.enable_unaudited_hdwallet_features()
        
        # Bước 3: Tạo tài khoản từ cụm từ ghi nhớ
        tai_khoan = Account.from_mnemonic(cum_tu_ghi_nho)
        
        # Bước 4: Lấy khóa bí mật và chuyển sang dạng hex
        khoa_bi_mat = tai_khoan.key.hex()
        
        # Bước 5: Lấy địa chỉ ví
        dia_chi_vi = tai_khoan.address
        
        # Bước 6: Lưu thông tin vào file
        with open('wallet.txt', 'w', encoding='utf-8') as f:
            f.write("=== THÔNG TIN VÍ ETHEREUM ===\n\n")
            f.write(f"Cụm từ ghi nhớ (12 từ):\n{cum_tu_ghi_nho}\n\n")
            f.write(f"Khóa bí mật:\n{khoa_bi_mat}\n\n")
            f.write("Lưu ý: Giữ bí mật thông tin trên!")
        
        # Bước 7: Hiển thị thông tin
        print("\n=== THÔNG TIN VÍ ETHEREUM ===\n")
        print(f"Địa chỉ ví của bạn:\n{dia_chi_vi}\n")
        print("Đã lưu cụm từ ghi nhớ và khóa bí mật vào file 'wallet.txt'")
        print("\nLƯU Ý QUAN TRỌNG:")
        print("1. Giữ bí mật file wallet.txt")
        print("2. Sao lưu file wallet.txt vào nơi an toàn")
        print("3. Không chia sẻ cụm từ ghi nhớ và khóa bí mật với ai")
        
    except Exception as loi:
        print(f"\nĐã xảy ra lỗi: {str(loi)}")
        print("Vui lòng kiểm tra lại việc cài đặt thư viện và thử lại.")

# Chạy chương trình
if __name__ == "__main__":
    tao_vi_ethereum()