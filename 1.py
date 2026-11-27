def clean_and_format_emails(emails: list[str]) -> list[str]:
    cleaned = []
    for email in emails:
        email = email.strip()
        email = email.lower()
        cleaned.append(email)
    unique = []
    for email in cleaned:
        if email not in unique:
            unique.append(email)
    unique.sort()
    return unique
if __name__ == "__main__":
    emails = ["  USER@gmail.com", "admin@mail.uz ", "User@gmail.com", " test@site.com"]
    print(clean_and_format_emails(emails))
