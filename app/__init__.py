from flask import Flask
import malaya
from flask import request

app = Flask(__name__)


print("downloading transformer")
malaya_transformer = malaya.translation.ms_en.transformer()


@app.route("/translate", methods=["POST"])
def translate_controller():
    text = request.form.get('text', "")
    print(text)
    if text == "":
        return { 'error': "empty string" }, 500
    translated_text = malaya_transformer.greedy_decoder([text])
    return translated_text[0], 200

