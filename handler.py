import json

def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response

def arbol_navidad(event, context):
    pisos = 10  
    arbol = ""  
    
    for piso in range(1, pisos + 1):
        arbol += ' ' * (pisos - piso) + '*' * (2 * piso - 1) + "\n"

    
    for _ in range(2): 
        arbol += ' ' * (pisos - 1) + '*\n'

    
    return {'statusCode': 200, 'body': json.dumps(arbol)}

    
            
    
        


    
    
