import json
import os
from sendgrid.helpers.mail import *
from sendgrid import *

# NOTE: you will need move this file to the root directory of this project to execute properly.

def build_hello_email():
    """Minimum required to send an email"""
    from_email = Email("dx@sendgrid.com")
    subject = "Hello World from the SendGrid Python Library"
    to_email = Email("elmer.thomas@sendgrid.com")
    content = Content("text/plain", "some text here")
    mail = Mail(from_email, subject, to_email, content)
    mail.personalizations[0].add_to(Email("elmer.thomas+add_second_email@sendgrid.com"))

    return mail.get()

def build_kitchen_sink():
    """All settings set"""
    mail = Mail()

    mail.set_from(Email("dx@sendgrid.com", "Elmer Thomas"))

    mail.set_subject("Hello World from the SendGrid Python Library")

    personalization = Personalization()
    personalization.add_to(Email("elmer.thomas@sendgrid.com", "Elmer Thomas"))
    personalization.add_to(Email("elmer.thomas@gmail.com", "Elmer Thomas Alias"))
    personalization.add_cc(Email("matt.bernier@sendgrid.com", "Matt Bernier"))
    personalization.add_cc(Email("eric.shallock@sendgrid.com", "Eric Shallock"))
    personalization.add_bcc(Email("matt.bernier+dx@sendgrid.com"))
    personalization.add_bcc(Email("eric.shallock+dx@sendgrid.com"))
    personalization.set_subject("Hello World from the Personalized SendGrid Python Library")
    personalization.add_header(Header("X-Test", "test"))
    personalization.add_header(Header("X-Mock", "true"))
    personalization.add_substitution(Substitution("%name%", "Tim"))
    personalization.add_substitution(Substitution("%city%", "Riverside"))
    personalization.add_custom_arg(CustomArg("user_id", "343"))
    personalization.add_custom_arg(CustomArg("type", "marketing"))
    personalization.set_send_at(1443636843)
    mail.add_personalization(personalization)

    personalization2 = Personalization()
    personalization2.add_to(Email("elmer.thomas@sendgrid.com", "Elmer Thomas"))
    personalization2.add_to(Email("elmer.thomas@gmail.com", "Elmer Thomas Alias"))
    personalization2.add_cc(Email("matt.bernier@sendgrid.com", "Matt Bernier"))
    personalization2.add_cc(Email("eric.shallock@sendgrid.com", "Eric Shallock"))
    personalization2.add_bcc(Email("matt.bernier+dx@sendgrid.com"))
    personalization2.add_bcc(Email("eric.shallock+dx@sendgrid.com"))
    personalization2.set_subject("Hello World from the Personalized SendGrid Python Library")
    personalization2.add_header(Header("X-Test", "test"))
    personalization2.add_header(Header("X-Mock", "true"))
    personalization2.add_substitution(Substitution("%name%", "Tim"))
    personalization2.add_substitution(Substitution("%city%", "Riverside"))
    personalization2.add_custom_arg(CustomArg("user_id", "343"))
    personalization2.add_custom_arg(CustomArg("type", "marketing"))
    personalization2.set_send_at(1443636843)
    mail.add_personalization(personalization2)

    mail.add_content(Content("text/plain", "some text here"))
    mail.add_content(Content("text/html", "<html><body>some text here</body></html>"))

    attachment = Attachment()
    attachment.set_content("TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gQ3JhcyBwdW12")
    attachment.set_type("application/pdf")
    attachment.set_filename("balance_001.pdf")
    attachment.set_disposition("attachment")
    attachment.set_content_id("Balance Sheet")
    mail.add_attachment(attachment)

    attachment2 = Attachment()
    attachment2.set_content("BwdW")
    attachment2.set_type("image/png")
    attachment2.set_filename("banner.png")
    attachment2.set_disposition("inline")
    attachment2.set_content_id("Banner")
    mail.add_attachment(attachment2)

    mail.set_template_id("13b8f94f-bcae-4ec6-b752-70d6cb59f932")

    mail.add_section(Section("%section1%", "Substitution Text for Section 1"))
    mail.add_section(Section("%section2%", "Substitution Text for Section 2"))

    mail.add_header(Header("X-Test1", "test1"))
    mail.add_header(Header("X-Test3", "test2"))

    mail.add_category(Category("May"))
    mail.add_category(Category("2016"))

    mail.add_custom_arg(CustomArg("campaign", "welcome"))
    mail.add_custom_arg(CustomArg("weekday", "morning"))

    mail.set_send_at(1443636842)

    mail.set_batch_id("sendgrid_batch_id")

    mail.set_asm(ASM(99, [4, 5, 6, 7, 8]))

    mail.set_ip_pool_name("24")

    mail_settings = MailSettings()
    mail_settings.set_bcc_settings(BCCSettings(True, Email("dx+reply@sendgrid.com")))
    mail_settings.set_bypass_list_management(BypassListManagement(True))
    mail_settings.set_footer_settings(FooterSettings(True, "Footer Text", "<html><body>Footer Text</body></html>"))
    mail_settings.set_sandbox_mode(SandBoxMode(True))
    mail_settings.set_spam_check(SpamCheck(True, 1, "https://spamcatcher.sendgrid.com"))
    mail.set_mail_settings(mail_settings)

    tracking_settings = TrackingSettings()
    tracking_settings.set_click_tracking(ClickTracking(True, True))
    tracking_settings.set_open_tracking(OpenTracking(True, "Optional tag to replace with the open image in the body of the message"))
    tracking_settings.set_subscription_tracking(SubscriptionTracking(True, "text to insert into the text/plain portion of the message", "<html><body>html to insert into the text/html portion of the message</body></html>", "Optional tag to replace with the open image in the body of the message"))
    tracking_settings.set_ganalytics(Ganalytics(True, "some source", "some medium", "some term", "some_content", "some_campaign"))
    mail.set_tracking_settings(tracking_settings)

    mail.set_reply_to(Email("dx+reply@sendgrid.com"))

    return mail.get()

def send_hello_email():
    sg = SendGridAPIClient()
    data = build_hello_email()
    response = sg.client.mail.send.beta.post(request_body=data)
    print(response.response_headers)
    print(response.status_code)
    print(response.response_body)

def send_kitchen_sink():
    sg = SendGridAPIClient()
    data = build_kitchen_sink()
    response = sg.client.mail.send.beta.post(request_body=data)
    print(response.response_headers)
    print(response.status_code)
    print(response.response_body)

send_hello_email() # this will actually send an email
send_kitchen_sink() # this will only send an email if you set SandBox Mode to False
