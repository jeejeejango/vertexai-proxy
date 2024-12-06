import os

from flask import Flask, jsonify, request
from google.cloud import aiplatform

app = Flask(__name__)

aiplatform.init(project=f'{os.environ["PROJECT_ID"]}', location=f'{os.environ["ENDPOINT_REGION"]}')
endpoint_name = f'projects/{os.environ["PROJECT_ID"]}/locations/{os.environ["ENDPOINT_REGION"]}/endpoints/{os.environ["ENDPOINT_ID"]}'
endpoint = aiplatform.Endpoint(endpoint_name)

def get_prediction(instance):
    app.logger.info('Sending prediction request to AI Platform ' + endpoint_name)
    app.logger.info(instance)

    try:
        instance_list = [instance]
        response = endpoint.predict(instance_list)
        app.logger.info(response)

        return response.predictions[0]
    except Exception as err:
        app.logger.error(f'Prediction request failed: {type(err)}: {err}')
        return None

@app.route("/", methods=['POST'])
def predict():
    request_json = request.get_json(silent=True)

    prediction = get_prediction(request_json)
    if not prediction:
        return 'Error getting prediction', 500

    app.logger.info(prediction)

    return jsonify(prediction), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
