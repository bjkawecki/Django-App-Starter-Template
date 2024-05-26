from allauth.account.signals import email_confirmed


def handle_user_email_confirmation(signal, sender, **kwargs):
    return


email_confirmed.connect(handle_user_email_confirmation)
