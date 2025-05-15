def generate_vcard(nom, prenom, email, tel, site, titre, note, filename):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{prenom} {nom}
N:{nom};{prenom};;;
TITLE:{titre}
EMAIL;TYPE=INTERNET:{email}
TEL;TYPE=CELL:{tel}
URL:{site}
NOTE:{note}
END:VCARD
"""
    with open(filename, 'w') as file:
        file.write(vcard)
    print(f"VCard enregistrée sous : {filename}")

# Exemple d'utilisation
generate_vcard(
    nom="Yakoubi",
    prenom="Yamina",
    email="contact@empreintedigitale.club",
    tel="+33 7 68 11 51 38",
    site="https://www.empreintedigitale.club",
    titre="Fondatrice – PrettyhowQ | Club Empreinte Digitale",
    note="One Word, One Visio",
    filename="Yamina_Yakoubi.vcf"
)