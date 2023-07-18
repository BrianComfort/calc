import json
import re

class HandleEvent():
    def __init__(self, raw, var):
        self.problem = raw
        self.answer = ''
        self.variables = var
        self.return_string = ''
        self.allowed_operands = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', ',', '.', '/', '+', '=', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', '{', '}', '*', '(', ')', "@"]


    def handle_variables(self):
        for vari in self.variables:
            self.problem = self.problem.replace(fr'@var({vari["letter"]})', vari['val'])        
        
        new_problem = self.problem
        print(new_problem)
        
        pattern = r'\@var\([a-zA-Z]\)'
        match = re.search(pattern, new_problem)

        if (match != None):
            return True, f'VARIABLE ERROR: No value is assigned to variable {match[0]}'
        else:
            pass

        return False, new_problem
    
    def find_illegal_operands(self):
        for char in self.problem:
            if char not in self.allowed_operands:
                print('error')
                return True, f'OPERAND ERROR: The operand {char} is not allowed.'


        return False, ''

    def solve(self):
        is_error, response = self.find_illegal_operands()

        if is_error == True:
            return response

        is_error, response = self.handle_variables()

        if is_error != True:
            try:
                final = eval(response)
                return final
            except:
                return f"An unknown error has occurred. Original string: {self.problem}, eval string: {response}."
        else:
            return response

def lambda_handler(event, context):


    handler = HandleEvent(event['queryStringParameters']['eq'], var=event['queryStringParameters']['var'])
    return {
        'statusCode': 200,
        'body': json.dumps(handler.solve())
    }


if __name__ == '__main__':
    event = r'4+3@var(x)+@var(y)%'
    var = [{'letter': 'x', 'val': '29'}, {'letter': 'y', 'val': '29'}]
    handler = HandleEvent(event, var)
    print(handler.solve())
