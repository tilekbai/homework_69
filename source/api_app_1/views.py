
import json
from datetime import datetime
from django.http import HttpResponse, HttpResponseNotAllowed, response
from django.views.decorators.csrf import ensure_csrf_cookie

def json_echo_view(request, *args, **kwargs):
    answer = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'method': request.method,
    }    
    if request.body:
        answer['content'] = json.loads(request.body)
    answer_as_json = json.dumps(answer)
    response = HttpResponse(answer_as_json)
    response['Content-Type'] = 'application/json'
    return response


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


#######################################################
numdict = {
     "A": 1234,
     "B": 4567
}

err_dict = {
            "error": "TypeError: must be int!"
        }

def add_view(request, *args, **kwargs):
    if type(numdict["A"]) == int and type(numdict["B"]) == int:
        sumres = numdict["A"] + numdict["B"]
        sumres_as_json = json.dumps(sumres)
        response = HttpResponse(sumres_as_json)
        response['Content-Type'] = 'application/json'
        return response
    else:
        error = json.dumps(err_dict)
        response = HttpResponse(error)
        response.status_code = 400
        return response

def subtract_view(request, *args, **kwargs):
    if type(numdict["A"]) == int and type(numdict["B"]) == int:
        subres = numdict["A"] - numdict["B"]
        subres_as_json = json.dumps(subres)
        response = HttpResponse(subres_as_json)
        response['Content-Type'] = 'application/json'
        return response
    else:
        error = json.dumps(err_dict)
        response = HttpResponse(error)
        response.status_code = 400
        return response

def multiply_view(request, *args, **kwargs):
    if type(numdict["A"]) == int and type(numdict["B"]) == int:
        sumres = numdict["A"] * numdict["B"]
        sumres_as_json = json.dumps(sumres)
        response = HttpResponse(sumres_as_json)
        response['Content-Type'] = 'application/json'
        return response
    else:
        error = json.dumps(err_dict)
        response = HttpResponse(error)
        response.status_code = 400
        return response

def divide_view(request, *args, **kwargs):
    if type(numdict["A"]) == int and type(numdict["B"]) == int:
        if numdict["B"] != 0:
            sumres = numdict["A"] / numdict["B"]
            sumres_as_json = json.dumps(sumres)
            response = HttpResponse(sumres_as_json)
            response['Content-Type'] = 'application/json'
            return response
        else:
            err_dict["error"] = "Division by zero!"
            error = json.dumps(err_dict)
            response = HttpResponse(error)
            response.status_code = 400
            return response

    else:
        error = json.dumps(err_dict)
        response = HttpResponse(error)
        response.status_code = 400
        return response

