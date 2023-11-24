from send_email import send_email


def warning():
    #
    smtp_server = 'smtp.qq.com'  # 例如：'smtp.gmail.com'
    sender_email = '1552129782@qq.com'  # 你的发送邮箱
    sender_password = 'dprarrglxvaciffb'  # 你的发送邮箱密码
    receiver_email = '919845780@qq.com'  # 收件人邮箱

    subject = '邮件主题'
    body = '这是邮件正文。'

    #   email warning
    send_email(smtp_server, sender_email, sender_password, receiver_email, subject, body)
