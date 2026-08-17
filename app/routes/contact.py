from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
import resend
from app.models.forms import ContactForm


contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():

    form = ContactForm()

    if form.validate_on_submit():

        sender_name = form.name.data
        sender_email = form.email.data
        message_text = form.message.data

        text_body = f"""New message from your portfolio.

Sender Name:
{sender_name}

Sender Email:
{sender_email}

Message:
{message_text}
"""

        html_body = render_template(
            "emails/contact_message.html",
            sender_name=sender_name,
            sender_email=sender_email,
            message_text=message_text,
        )

        try:
            api_key = current_app.config["RESEND_API_KEY"]
            from_email = current_app.config["RESEND_FROM_EMAIL"]
            to_email = current_app.config["RESEND_TO_EMAIL"]

            if not all((api_key, from_email, to_email)):
                raise RuntimeError(
                    "RESEND_API_KEY, RESEND_FROM_EMAIL, and RESEND_TO_EMAIL must be configured."
                )

            resend.api_key = api_key
            resend.Emails.send(
                {
                    "from": from_email,
                    "to": [to_email],
                    "subject": "Portfolio Contact Message",
                    "html": html_body,
                    "text": text_body,
                    "reply_to": sender_email,
                }
            )

            flash("Message sent successfully!", "success")

        except Exception as e:
            current_app.logger.exception("RESEND ERROR: %s", e)
            flash("Failed to send message. Please try again.", "danger")

        return redirect(url_for("contact.contact"))

    return render_template("contact.html", form=form)
