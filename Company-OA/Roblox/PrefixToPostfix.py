

s = "*-A/BC-/AKL"

def prefix_to_postfix(s):
    operators = set(['+', '-', '*', '/', '^']) 

    # Stack for storing operands 
    stack = []                

    # Reversing the order 
    s = s[::-1]  

    # iterating through individual tokens 
    for i in s:               

        # if token is operator 
        if i in operators:    

            # pop 2 elements from stack 
            a = stack.pop() 
            b = stack.pop() 

            # concatenate them as operand1 +  
            # operand2 + operator 
            temp = a+b+i          
            stack.append(temp)  

        # else if operand 
        else:                 
            stack.append(i) 

    # printing final output 
    return stack[0]  