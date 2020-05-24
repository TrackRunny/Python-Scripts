# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Spam-Mail - Send mail to someone                                          #
# Copyright (C) 2019-2020 TrackRunny                                        #
#                                                                           #
# This program is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program. If not, see <https://www.gnu.org/licenses/>.     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os

import smtplib
from email.message import EmailMessage


class SendMail:
    def __init__(self):
        super().__init__()
        self.email = os.environ.get("email")
        self.email_password = os.environ.get("email_password")
        self.amount = 20
        self.counter = 1

    def send_mail(self, emailto, subject):
        msg = EmailMessage()

        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = emailto

        msg.set_content("""\
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <title>Document</title>
                <link href="https://fonts.googleapis.com/css?family=Ubuntu&display=swap" rel="stylesheet">
            </head>
            <style>
                * {
                    font-family: 'Ubuntu', sans-serif;
                    box-sizing: border-box;
                }
            </style>
    
            <style>
                .linebreak {
                    width: 50%;
                    size: 10;
                }
            </style>
            <body>
                <footer>
                    <div class="info">
                        <h1 style="text-align: center; margin-bottom: 10px; color: #013879;">Hello!</h1>
                        <hr class="linebreak">
                    </div>
                </footer>
            </body>
        </html>
            """, subtype='html')

        while self.amount >= self.counter:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt:
                smpt.login(self.email, self.email_password)
                smpt.send_message(msg)

                if self.counter <= 1:
                    print(f"[INFO] Sent {self.counter} email.")
                else:
                    print(f"[INFO] Sent {self.counter} emails.")

                self.counter += 1


if __name__ == '__main__':
    mail = SendMail()
    mail.send_mail("EmailToSendTo", "Read me :)")
