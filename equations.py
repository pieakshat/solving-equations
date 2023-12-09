import numpy as np

def user_input():
    no_of_variables = int(input("Number of variables: "))
    #no_of_equations = int(input("Number of equations: ")) 
    D=[]
    for _ in range(no_of_variables): 
        row=list(map(float, input("enter the coefficents: ").split()))
        D.append(row)
    
    constants=list(map(float, input("enter the constants: ").split()))

    return np.array(D), np.array(constants) 

def cramer_solve(coefficents_matrix, constants_vector): 
    num_equations, _= coefficents_matrix.shape

    detA=np.linalg.det(coefficents_matrix)

    if detA==0: 
        raise ValueError("no real solution exists")

    solutions=[]

    for i in range(num_equations): 
        matrix_copy=coefficents_matrix.copy()
        matrix_copy[:, i]=constants_vector

        det_i=np.linalg.det(matrix_copy)

        xi=det_i/detA
        solutions.append(xi)

    return solutions


if __name__=="__main__": 
    coefficents_matrix, constants_vector=user_input()

    try: 
        solutions=cramer_solve(coefficents_matrix, constants_vector)
        print("solutions: ", solutions)
    except ValueError as e:
        print("error:",e)
         
        
  
    

        






      