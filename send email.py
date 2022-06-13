import win32com.client as win32

def send_email():
    body = """Testing thank you"""
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = "testemailhere@gmail.com"
	mail.CC = "youremailaddressed@gmail.com"
    mail.Subject = "Test Email"
    mail.Body = body
    mail.Send()