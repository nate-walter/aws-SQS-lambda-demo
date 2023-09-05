def handler(event, context):
    print(event)
    return {'statuscode': 200, 'body': 'Success!!'}