import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

def send_email():
    # 取得環境變量
    sendgrid_api_key = os.getenv('SENDGRID_API_KEY')
    recipient_email = os.getenv('RECIPIENT_EMAIL')

    if not sendgrid_api_key or not recipient_email:
        print("缺少 API 金鑰或收件人郵件地址")
        return

    # 初始化 SendGrid 客戶端
    sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)

    # 設置郵件內容
    from_email = Email("your-email@example.com")  # 這是發件人的電子郵件地址，應該是 SendGrid 驗證過的郵箱
    to_email = To(recipient_email)  # 收件人
    subject = "GitHub Actions Email Notification"
    content = Content("text/plain", "Hello, this is an automated email sent from GitHub Actions!")

    # 創建郵件
    mail = Mail(from_email, to_email, subject, content)

    try:
        # 發送郵件
        response = sg.send(mail)
        print(f"郵件發送成功！狀態碼：{response.status_code}")
    except Exception as e:
        print(f"發送郵件時發生錯誤：{e}")

if __name__ == "__main__":
    send_email()
