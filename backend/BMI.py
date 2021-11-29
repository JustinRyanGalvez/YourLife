import hug

@hug.get('/BMI/')
def get_BMI(request, response):
    results = {}
    if(request.params["gender"] == "male"):
        result = (10 * int(request.params["weight"])) + (6.25 * int(request.params["height"])) - (5 * int(request.params["age"])) + 5 
        results["maintenance"] = result
        results["bulking"] = result * 120 / 100
        results["cutting"] = result * 80 / 100
    elif (request.params["gender"] == "female"):
        result = (10 * int(request.params["weight"])) + (6.25 * int(request.params["height"])) - (5 * int(request.params["age"])) - 161
        results["maintenance"] = result
        results["bulking"] = result * 120 / 100
        results["cutting"] = result * 80 / 100
    else:
        response.status = hug.falcon.HTTP_400
        return response.status
    return results
