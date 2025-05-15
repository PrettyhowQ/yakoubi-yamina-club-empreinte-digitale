from flask import Flask, request, send_file, render_template_string
import vobject
import os

app = Flask(__name__)

FORM_HTML = '''
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: url('PrettyhowQ_logo.png') no-repeat center center fixed;
  background-size: cover;
  font-family: Arial, sans-serif;
}
</style>
</head>
<body>
<h2>Générateur de vCard - Club Empreinte Digitale</h2>
<form method="post">
  Nom : <input name="name" required><br>
  Email : <input name="email" required><br>
  Métier : <input name="job"><br>
  LinkedIn : <input name="linkedin"><br>
  X (Twitter) : <input name="twitter"><br>
  Club Empreinte Digitale (profil) : <input name="club_profile"><br>
  <button type="submit">Générer ma vCard</button>
</form>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def vcard():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        job = request.form["job"]
        linkedin = request.form["linkedin"]
        twitter = request.form["twitter"]
        club_profile = request.form["club_profile"]

        v = vobject.vCard()
        v.add('fn').value = name
        v.add('email').value = email
        if job:
            v.add('title').value = job

        if linkedin:
            link = v.add('url')
            link.value = linkedin
            link.type_param = "LinkedIn"
        if twitter:
            tw = v.add('url')
            tw.value = twitter
            tw.type_param = "X"
        if club_profile:
            club = v.add('url')
            club.value = club_profile
            club.type_param = "Club Empreinte Digitale"

        filename = f"{name.replace(' ', '_')}.vcf"
        with open(filename, "wb") as f:
            f.write(v.serialize().encode())

        response = send_file(filename, as_attachment=True)
        try:
            os.remove(filename)
        except Exception:
            pass
        return response

    return render_template_string(FORM_HTML)

if __name__ == "__main__":
    app.run(debug=True)