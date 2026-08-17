from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_mail import Message
from app import mail
from app.models.forms import ContactForm


contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():

    form = ContactForm()

    if form.validate_on_submit():

        sender_name = form.name.data
        sender_email = form.email.data
        message_text = form.message.data

        msg = Message(
            subject="Portfolio Contact Message",
            recipients=[current_app.config["MAIL_USERNAME"]],
            body=f"""
New message from your portfolio.

Sender Name:
{sender_name}

Sender Email:
{sender_email}

Message:
{message_text}
"""
        )

        msg.html = render_template(
            "emails/contact_message.html",
            sender_name=sender_name,
            sender_email=sender_email,
            message_text=message_text,
        )

        # Allow you to reply directly to the visitor
        msg.reply_to = sender_email

        try:
            mail.send(msg)

            flash("Message sent successfully!", "success")

        except Exception as e:

            print("MAIL ERROR:", e)

            flash("Failed to send message. Please try again.", "danger")

        return redirect(url_for("contact.contact"))

    return render_template("contact.html", form=form)
