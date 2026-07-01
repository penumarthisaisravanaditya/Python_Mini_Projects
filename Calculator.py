
# In one line 
# while True: print(eval(input(">>>")))

def calculator():
    
    print("---- Welcome to calcify - Simple Calculator -----")
    print("Supports: ADDITION(+), SUBTRACTION(-), MULTIPLICATION(*), DIVISION(/)")
    print("Type 'exit' to quit.\n")
    
    while True:
        
        expression = input("Enter Expression:")
        
        if expression.lower() == 'exit':
            
            print("Exiting Calculator")
            break
        
        try:
            
            allowed = '0123456789+-*/.()'
            
            if all(char in allowed for char in expression):
                result = eval(expression)
                print(f"Result: {result}")
                
            else:
                print("Error: Invalid characters")
                
        except ZeroDivisionError:
            print("Error : Division by zero")
            
        except Exception as e:
            print("Error: Invalid Expression")
            
calculator()