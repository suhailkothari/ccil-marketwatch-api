from flask import Flask, jsonify
import requests
import json
import pandas as pd

app = Flask(__name__)

@app.route("/marketwatch")
def marketwatch():

    url = "https://www.ccilindia.com/web/ccil/market-watch"

    params = {
        "p_p_id": "com_ccil_ndsom_marketwatch_CcilNDSOMMarketWatchPortlet_INSTANCE_swas",
        "p_p_lifecycle": "2",
        "p_p_state": "normal",
        "p_p_mode": "view",
        "p_p_resource_id": "NDSOMCG",
        "p_p_cacheability": "cacheLevelPage"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.ccilindia.com/web/ccil/market-watch"
    }

    session = requests.Session()

    response = session.post(
        url,
        params=params,
        headers=headers
    )

    # First JSON parse
    data = response.json()

    # Second JSON parse
    parsed_data = json.loads(data["result1"])

    return jsonify(parsed_data)

if __name__ == "__main__":
    app.run(debug=True)