from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_mail import Message
from app import mail
from app.models.forms import ContactForm



contact_bp = Blueprint('contact', __name__)


@contact_bp.route('/contact', methods=["GET","POST"])
def contact():

    form = ContactForm()

    if form.validate_on_submit():

        sender_name = form.name.data
        sender_email = form.email.data
        message_text = form.message.data

        msg = Message(
            subject="New Portfolio Contact Message",
            recipients=["YOUR_EMAIL@gmail.com"],
            body=f"""
New message from your portfolio.

Sender Email:
{sender_email}

Sender Email:
{sender_name}

Message:
{message_text}
"""
        )

        mail.send(msg)

        flash("Message sent successfully!", "success")

        return redirect(url_for("contact.contact"))

    return render_template("contact.html", form=form)