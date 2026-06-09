from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

# --------------------------------
# HOME
# --------------------------------
@app.route("/")
def home():

    return "CCIL MarketWatch API Running"


# --------------------------------
# MARKETWATCH API
# --------------------------------
@app.route("/marketwatch")
def marketwatch():

    try:

        # --------------------------------
        # URL
        # --------------------------------
        url = "https://www.ccilindia.com/web/ccil/market-watch"

        # --------------------------------
        # QUERY PARAMETERS
        # --------------------------------
        params = {
            "p_p_id": "com_ccil_ndsom_marketwatch_CcilNDSOMMarketWatchPortlet_INSTANCE_swas",
            "p_p_lifecycle": "2",
            "p_p_state": "normal",
            "p_p_mode": "view",
            "p_p_resource_id": "NDSOMCG",
            "p_p_cacheability": "cacheLevelPage"
        }

        # --------------------------------
        # HEADERS
        # --------------------------------
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/137.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.ccilindia.com/web/ccil/market-watch"
        }

        # --------------------------------
        # SESSION
        # --------------------------------
        session = requests.Session()

        # --------------------------------
        # POST REQUEST
        # --------------------------------
        response = session.post(
            url,
            params=params,
            headers=headers,
            timeout=30
        )

        # --------------------------------
        # STATUS CHECK
        # --------------------------------
        response.raise_for_status()

        # --------------------------------
        # FIRST JSON PARSE
        # --------------------------------
        data = response.json()

        # --------------------------------
        # CHECK RESPONSE
        # --------------------------------
        if "result1" not in data:

            return jsonify({
                "status": "error",
                "message": "result1 not found",
                "response": data
            }), 500

        # --------------------------------
        # SECOND JSON PARSE
        # --------------------------------
        parsed_data = json.loads(data["result1"])

        # --------------------------------
        # RETURN FINAL JSON
        # --------------------------------
        return jsonify(parsed_data)

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e),
            "response_text": response.text[:1000] if 'response' in locals() else None
        }), 500


# --------------------------------
# MAIN
# --------------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )