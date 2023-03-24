import json
import requests


class APIMng:
    def __init__(self, melexID):
        self.Melex_ID = melexID
        self.Requests_endpoint = {
            'url_recived': 'http://213.97.17.253:9000/requests/state/recived',
            'url_put': 'http://213.97.17.253:9000/request',
            'url_progress': 'http://213.97.17.253:9000/requests/state/progress',
            'json': None,
            'id': None
        }
        self.ParametersCCAA_endpoint = {
            'url': 'http://213.97.17.253:9000/parametersCA/',
            'json': None
        }
        self.estate = None

    def __del__(self):
        pass

    # Pedir tareas REQUESTS/GET
    def get_requests_api(self):
        r = requests.get(url=self.Requests_endpoint['url_recived'])
        self.Requests_endpoint['json'] = json.loads(r.text)
        return self.Requests_endpoint['json']

    def task_progress(self):
        r = requests.get(url=self.Requests_endpoint['url_progress'])
        print(r.text)
        if isinstance(json.loads(r.text), dict):
            return None, False
        else:
            return json.loads(r.text), True

    # Mandar actualización tareas (progreso o acabada) REQUESTS/PUT
    def put_requests_api(self):
        print(self.Requests_endpoint['url_put'] + '/' + str(self.Requests_endpoint['id']), self.Requests_endpoint['json'])
        r = requests.put(self.Requests_endpoint['url_put'] + '/' + str(self.Requests_endpoint['id']), json=self.Requests_endpoint['json'])
        print(r)

    # Mandar parámetros del vehículo (PARAMETERScar/PUT)
    def put_ParametersCCAA_api(self):
        r = requests.put(self.ParametersCCAA_endpoint['url'] + self.Melex_ID, json=self.ParametersCCAA_endpoint['json'])

    # Crear JSON para hacer el put al endpoint Requests
    def requests_put_json(self, data, id):
        self.Requests_endpoint["json"] = data
        self.Requests_endpoint["id"] = id

    def create_ParametersCCAA_json(self, data):
        self.ParametersCCAA_endpoint["json"] = data

