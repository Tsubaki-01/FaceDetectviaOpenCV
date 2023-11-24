import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(smtp_server, sender_email, sender_password, receiver_email, subject, body):
    try:
        #   create msg object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        #   msg content
        msg.attach(MIMEText(body, 'plain'))

        #   smtp server login
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.login(sender_email, sender_password)

        #   send email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        #   quit the connection
        server.quit()
        print(f"邮件已成功发送给 {receiver_email}")
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")


if __name__ == '__main__':
    # 发送邮件 示例
    smtp_server = 'smtp.qq.com'  # 例如：'smtp.gmail.com'
    sender_email = '1552129782@qq.com'  # 你的发送邮箱
    sender_password = 'dprarrglxvaciffb'  # 你的发送邮箱密码
    receiver_email = '919845780@qq.com'  # 收件人邮箱

    subject = '邮件主题'
    body = '这是邮件正文。'

    send_email(smtp_server, sender_email, sender_password, receiver_email, subject, body)
