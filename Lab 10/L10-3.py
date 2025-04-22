name = input("Enter full name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

with open('contact.vcf', 'w') as file:
    file.write(vcard)
print("vCard created.")
