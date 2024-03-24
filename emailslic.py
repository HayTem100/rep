#-------------------------
#-----Email Slicing-------
#-------------------------
email = input("Welcome... enter your email : ").strip().lower()
user_name = email[:email.index("@")]
email_part = email[email.index("@")+1:]

print(f"####[User name] ==> [{user_name}]######")
print(f"####[emailDomain] ==> [{email_part}]#####")