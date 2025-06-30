def lambda_handler(event, context):
    # Expecting input as: { "a": 5, "b": 3 }
    a = event.get("a")
    b = event.get("b")
 
    if a is None or b is None:
        return {
            "statusCode": 400,
            "body": "Missing 'a' or 'b' in input."
        }
 
    result = a + b
 
    return {
        "statusCode": 200,
        "body": {
            "sum": result
        }
    }