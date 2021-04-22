def sendfunc(receiver_name,receiver_email):
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    subject = "Your RARE AIR Quote"
    body = "Dear "+str(receiver_name)+", \n \n Thanks for contacting RARE AIR. Here's a copy of your bespoke quote. \n \n"
    sender_email = "aviation@rare-air.co.uk"
    password ="9k59u0w4c2o8"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "../Outputs/Finished_quote.pdf" 

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        "attachment; filename=Your_Quote.pdf",
    )

    # Add attachment to message and convert message to string
    message.attach(MIMEText("Kind Regards,\n The RARE Commercial Team","plain"))
    message.attach(part)
    text = message.as_string()
    
    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("mail.rare-air.co.uk", 587) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

















