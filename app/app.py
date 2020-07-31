from flask import Flask, request, Response
import xmltodict
import translation


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['DEBUG'] = True


def validate_request(request):
    error_message = ''
    status = 1
    if request.headers.get('Content-Type') == 'application/xml':
        request_dict = xmltodict.parse(request.get_data())
        if 'request' in request_dict:
            if 'text' in request_dict['request']:
                status = 0
                return request_dict, status, error_message
            else:
                error_message = '<text>がない'
        else:
            error_message = '<request>がない'
    else:
        error_message = 'xmlじゃない'
    return None, status, error_message


@app.route('/translate/to_jp', methods=['GET', 'POST'])
def translate_to_jp():
    request_dict, status, error_message = validate_request(request)
    if status == 0:
        text = request_dict['request']['text']
        translated = translator_to_jp.translate(text)
        app.logger.info(text)
        app.logger.info(translated)
    else:
        translated = ''

    response = Response(response=xmltodict.unparse({'response':
                                                    {'text': translated,
                                                     'error_message': error_message,
                                                     'status': status}}),
                        status=200, mimetype='application/xml')
    response.headers['Content-Type'] = 'application/xml; charset=utf-8'
    return response


if __name__ == '__main__':
    translator_to_en = translation.Google_Translator('en')
    translator_to_jp = translation.Google_Translator('ja')
    app.secret_key = 'Ilikecakes'
    app.run(host='0.0.0.0')
