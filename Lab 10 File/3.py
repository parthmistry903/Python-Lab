# Accept contact details from the user and create a vcard that we can directly store in our mobile.
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

vcard = f"""BEGIN:VCARD
FN:{name}
EMAIL:{email}
END:VCARD
"""

with open(f"{name}.vcf", 'w') as f:
    f.write(vcard)