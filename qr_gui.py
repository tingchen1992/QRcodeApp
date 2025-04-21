import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("QR Code 產生器")
root.geometry("400x500")

label = tk.Label(root, text="請輸入網址：", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=20)


def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showwarning("警告", "請輸入網址！")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_output.png")

    img_display = Image.open("qr_output.png")
    img_display = img_display.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_display)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  

    messagebox.showinfo("完成", "QR Code 已產生並儲存為 qr_output.png")


button = tk.Button(root, text="產生 QR Code", command=generate_qr, font=("Arial", 12))
button.pack(pady=10)

root.mainloop()
