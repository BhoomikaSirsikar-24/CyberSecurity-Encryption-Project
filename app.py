from flask import Flask, render_template, request
from cipher import encrypt_text, decrypt_text

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    encrypted_text = ""
    decrypted_text = ""
    original_text = ""
    shift = 3
    error = ""

    if request.method == "POST":
        original_text = request.form.get("message", "")
        shift_value = request.form.get("shift", "3")
        action = request.form.get("action", "encrypt")

        try:
            shift = int(shift_value)

            if not 0 <= shift <= 25:
                error = "Please enter a shift key between 0 and 25."

            elif not original_text:
                error = "Please enter a message first."

            elif action == "encrypt":
                encrypted_text = encrypt_text(original_text, shift)
                decrypted_text = decrypt_text(encrypted_text, shift)

            elif action == "decrypt":
                decrypted_text = decrypt_text(original_text, shift)
                encrypted_text = original_text

        except ValueError:
            error = "The shift key must be a whole number."

    return render_template(
        "index.html",
        original_text=original_text,
        encrypted_text=encrypted_text,
        decrypted_text=decrypted_text,
        shift=shift,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)