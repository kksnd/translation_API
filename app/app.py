from flask import Flask, request, Response
import xmltodict
import translation


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['DEBUG'] = True


@app.route('/response_test', methods=['GET', 'POST'])
def response_test():
    translated = '翻訳結果'

    response = Response(response=xmltodict.unparse({'text': translated}),
                        status=200, mimetype="application/xml")
    response.headers["Content-Type"] = "text/xml; charset=utf-8"
    return response


@app.route('/request_test', methods=['GET', 'POST'])
def request_test():
    app.logger.info(request.headers)
    app.logger.info(request.get_data())
    
    translated = '翻訳結果'

    response = Response(response=xmltodict.unparse({'text': translated}),
                        status=200, mimetype="application/xml")
    response.headers["Content-Type"] = "text/xml; charset=utf-8"
    return response


@app.route('/translate/to_jp', methods=['GET', 'POST'])
def translate_to_jp():
    translated = '翻訳結果'

    response = Response(response=xmltodict.unparse({'text': translated}),
                        status=200, mimetype="application/xml")
    response.headers["Content-Type"] = "text/xml; charset=utf-8"
    return response


if __name__ == '__main__':
    translator_to_en = translation.Google_Translator('en')
    translator_to_jp = translation.Google_Translator('jp')
    app.secret_key = 'Ilikecakes'
    app.run(host='0.0.0.0')
