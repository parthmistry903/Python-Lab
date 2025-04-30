# Accept contact details from the user and create a vcard that we can directly store in our mobile.
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")
vcard = f"""BEGIN:VCARD {{\n}}VERSION:3.0 {{\n}}FN:{name} {{\n}}TEL:{phone} {{\n}}EMAIL:{email} {{\n}}END:VCARD"""
with open(f"{name}.vcf", 'w') as f:
    f.write(vcard)