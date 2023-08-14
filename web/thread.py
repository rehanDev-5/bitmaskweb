import threading

class SendMailClass(threading.Thread):
    def __init__(self, mail):
        threading.Thread.__init__(self)
        self.mail = mail

    def run(self):
        try:
            self.mail.send()
        except Exception as e:
            print(e)