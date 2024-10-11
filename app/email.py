from flask_mail import Message
from flask import current_app, render_template


def confirmacion_compra(mail, usuario, libro) -> None:
    try:
        message = Message('Confirmación de compra',
                        sender=current_app.config['MAIL_USERNAME'],
                        recipients=['666monroy@gmail.com'])
        message.html = render_template('emails/confirmacion_compra.html', usuario=usuario, libro=libro)
        mail.send(message)

    except Exception as e:
        raise Exception(e)
