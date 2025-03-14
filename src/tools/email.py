import pandas as pd
from langchain.tools import tool

from src.data_generation.data_generation_utils import HARDCODED_CURRENT_TIME

# Data is hard-coded so that the agent can call them without passing the dataframe as an argument.
# We cannot use a class because LangChain does not support tools inside classes.
EMAILS = pd.read_csv("/data/sxs7285/Porjects_code/WorkBench-test-/data/processed/emails.csv", dtype=str)


def reset_state():
    """
    Resets the emails to the original state.
    """
    global EMAILS
    EMAILS = pd.read_csv("data/processed/emails.csv", dtype=str)


@tool("email.get_email_information_by_id", return_direct=False)
def get_email_information_by_id(email_id=None, field=None):
    """
    Retrieves specific details of an email by its ID.

    Parameters
    ----------
    email_id : str, optional
        Unique ID of the email.
    field : str, optional
        Specific field to return. Available fields: "email_id", "sender", "subject", "sent_date", "body", "inbox/outbox".

    Returns
    -------
    email_information : dict
        Information of the specified email for the given ID and field.

    Examples
    --------
    >>> email.get_email_information_by_id("12345678", "subject")
    {{"subject": "Project Update"}}

    >>> email.get_email_information_by_id("12345678", "sent_date")
    {{"sent_date": "2024-01-10 09:30:00"}}
    """
    if not email_id:
        return "Email ID not provided."
    if not field:
        return "Field not provided."
    email = EMAILS[EMAILS["email_id"] == email_id].to_dict(orient="records")
    if email:
        if field in email[0]:
            return {field: email[0][field]}
        else:
            return "Field not found."
    else:
        return "Email not found."


@tool("email.search_emails", return_direct=False)
def search_emails(query="", date_min=None, date_max=None):
    """
    Searches for emails matching the given query across subject, body, or sender fields.
    The function matches an email if all words in the query appear in any of these fields.

    Parameters
    ----------
    query : str, optional
        Search query, matching terms in subject, body, or sender fields.
    date_min : str, optional
        Lower date limit for the email's sent date (inclusive). Format: "YYYY-MM-DD"
    date_max : str, optional
        Upper date limit for the email's sent date (inclusive). Format: "YYYY-MM-DD"

    Returns
    -------
    emails : list
        List of emails matching the query criteria.

    Examples
    --------
    >>> email.search_emails("Project Update")
    [{{"email_id": "12345678", "inbox/outbox": "inbox", "subject": "Project Update", "sender/recipient": "jane@example.com", "sent_datetime": "2024-01-10 09:30:00", "body": "Please find the project update attached."}}]
    """

    query_words = query.lower().split()

    # Filter function to check if all query words are in any of the specified fields
    def filter_emails(row):
        combined_fields = f"{row['subject']} {row['body']} {row['sender/recipient']}".lower()
        return all(word in combined_fields for word in query_words)

    # Apply filter function across all rows
    filtered_emails = EMAILS.apply(filter_emails, axis=1)
    emails = EMAILS[filtered_emails].sort_values("sent_datetime", ascending=False).to_dict(orient="records")
    if date_min:
        emails = [
            email for email in emails if pd.Timestamp(email["sent_datetime"]).date() >= pd.Timestamp(date_min).date()
        ]
    if date_max:
        # inclusive, remove time from timestamp
        emails = [
            email for email in emails if pd.Timestamp(email["sent_datetime"]).date() <= pd.Timestamp(date_max).date()
        ]
    if len(emails):
        return emails[:5]
    else:
        return "No emails found."


@tool("email.send_email", return_direct=False)
def send_email(recipient=None, subject=None, body=None):
    """
    Sends an email to the specified recipient.

    Parameters
    ----------
    recipient : str, optional
        Email address of the recipient.
    subject : str, optional
        Subject line of the email.
    body : str, optional
        Body content of the email.

    Returns
    -------
    message : str
        Confirmation message of the email being sent.

    Examples
    --------
    >>> email.send_email("jane@example.com", "Meeting Reminder", "Don't forget our meeting at 10am tomorrow.")
    "Email sent successfully."
    """
    global EMAILS
    if not recipient or not subject or not body:
        return "Recipient, subject, or body not provided."
    if "@" not in recipient or "." not in recipient:
        return "Invalid recipient email address."
    recipient = recipient.lower()

    email_id = str(int(EMAILS["email_id"].max()) + 1)
    sent_datetime = HARDCODED_CURRENT_TIME
    EMAILS.loc[len(EMAILS)] = [
        email_id,
        "outbox",
        recipient,
        subject,
        sent_datetime,
        body,
    ]

    return "Email sent successfully."


@tool("email.delete_email", return_direct=False)
def delete_email(email_id=None):
    """
    Deletes an email by its ID.

    Parameters
    ----------
    email_id : str, optional
        Unique ID of the email to be deleted.

    Returns
    -------
    message : str
        Message indicating whether the deletion was successful.

    Examples
    --------
    >>> email.delete_email("12345678")
    "Email deleted successfully."
    """
    global EMAILS

    if not email_id:
        return "Email ID not provided."

    if email_id in EMAILS["email_id"].values:
        EMAILS = EMAILS[EMAILS["email_id"] != email_id]
        return "Email deleted successfully."
    else:
        return "Email not found."


@tool("email.forward_email", return_direct=False)
def forward_email(email_id=None, recipient=None):
    """
    Forwards an email to the specified recipient.

    Parameters
    ----------
    email_id : str, optional
        Unique ID of the email to be forwarded.
    recipient : str, optional
        Email address of the recipient.

    Returns
    -------
    message : str
        Message indicating whether the email was forwarded successfully.

    Examples
    --------
    >>> email.forward_email("12345678", "jane@example.com")
    "Email forwarded successfully."
    """
    global EMAILS
    if not email_id or not recipient:
        return "Email ID or recipient not provided."
    if email_id not in EMAILS["email_id"].values:
        return "Email not found."
    if "@" not in recipient or "." not in recipient:
        return "Invalid recipient email address."
    recipient = recipient.lower()
    email = EMAILS[EMAILS["email_id"] == email_id].to_dict(orient="records")[0]
    result = send_email.func(recipient, f"FW: {email['subject']}", email["body"])
    return "Email forwarded successfully." if result == "Email sent successfully." else result


@tool("email.reply_email", return_direct=False)
def reply_email(email_id=None, body=None):
    """
    Replies to an email by its ID.

    Parameters
    ----------
    email_id : str, optional
        Unique ID of the email to be replied.
    body : str, optional
        Body content of the email.

    Returns
    -------
    message : str
        Confirmation message of the email being replied.

    Examples
    --------
    >>> email.reply_email("12345678", "Thank you for the update.")
    "Email replied successfully."
    """
    global EMAILS
    if not email_id or not body:
        return "Email ID or body not provided."
    if email_id not in EMAILS["email_id"].values:
        return "Email not found."
    email = EMAILS[EMAILS["email_id"] == email_id].to_dict(orient="records")[0]
    result = send_email.func(email["sender/recipient"], f"{email['subject']}", body)
    return "Email replied successfully." if result == "Email sent successfully." else result
