from flask import Flask, make_response, jsonify, request
from quote import getQuote
#from model import tierOneModel

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return app.send_static_file('main.html')

@app.route('/<filename>', methods=['GET'])
def static_files(filename):
    return app.send_static_file(filename)

# getting the quote by providing the symbol as a query parameter
# http://localhost:8080/get_quote_query_param?symbol=AMZN
@app.route('/get_quote_query_param', methods=['GET'])
def get_quote_query_param():
    symbol = request.args.get('symbol')
    quote = getQuote(symbol)
    company = quote.quote["name"]
    date = quote.quote['datetime']
    price = quote.quote['close']
    volume = quote.quote['volume']
    return jsonify({"Company":company, "Date": date, "Price": price, "Volume": volume})
    
app.run(debug=True, port="8080")



### FYI only
# # getting the quote by providing the symbol as the URL
# # http://localhost:8080/get_quote_url/AMZN
# @app.route('/get_quote_url/<symbol>', methods=['GET'])
# def get_quote_url(symbol):
#     quote = getQuote(symbol)
#     company = quote.quote["name"]
#     date = quote.quote['datetime']
#     closing_price = float(quote.quote['close'])
#     volume = quote.quote['volume']
#     return jsonify({"Company":company, "Date": date, "Closing Price": closing_price, "Volume": volume})

# # getting the quote using payload
# @app.route('/get_quote_payload', methods=['GET'])
# def get_quote_query_payload():
#     try:
#         print("Trying to get payload")
#         payload = request.get_json
#         symbol = payload['symbol']
#     except Exception as e:
#         print(f'Faced an error while trying to load payload: {e}')

#     quote = getQuote(symbol)
#     print(quote.error)
#     if quote.error is not None:
#         return jsonify({"error": quote.error}), 404
    
#     company = quote.company()
#     date = quote.date()
#     closing_price = quote.closing_price()
#     volume = quote.volume()
#     return jsonify({"Company":company, "Date": date, "Closing Price": closing_price, "Volume": volume})