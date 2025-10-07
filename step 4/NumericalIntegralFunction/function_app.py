import logging
import azure.functions as func
import math

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def numerical_integration(func, lower, upper, n):
    step = (upper - lower) / n
    total_area = 0.0

    for i in range(n):
        x = lower + i * step
        total_area += func(x) * step

    return total_area

def abs_sin(x):
    return abs(math.sin(x))

@app.route(route="NumericalIntegralFunction")
def NumericalIntegralFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Get query parameters
        lower = req.params.get('lower')
        upper = req.params.get('upper')
        n = req.params.get('n')

        # Check if parameters are missing
        if lower is None or upper is None or n is None:
            return func.HttpResponse(
                "Please provide 'lower', 'upper', and 'n' as query parameters.",
                status_code=400
            )

        # Convert parameters to appropriate types
        lower = float(lower)
        upper = float(upper)
        n = int(n)

        # Validate 'n'
        if n <= 0:
            return func.HttpResponse("'n' must be a positive integer.", status_code=400)

        # Compute the integral
        result = numerical_integration(abs_sin, lower, upper, n)

        # Return the result
        return func.HttpResponse(f"Integral result: {result}", status_code=200)

    except ValueError as e:
        return func.HttpResponse(f"Invalid input: {str(e)}", status_code=400)
    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)