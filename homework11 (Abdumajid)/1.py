def clean_and_format_emails(emails: list[str]) -> list[str]:
    return sorted(set(email.strip().lower() for email in emails))

if __name__ == "__main__":
	emails = [" USER@gmail.com", "admin@mail.uz ", "User@gmail.com", " test@site.com"]
	print(clean_and_format_emails(emails))
