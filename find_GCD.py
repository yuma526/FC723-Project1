#Initialize a class to implement the Euclidean Algorithm for finding GCD of number a and b.

class EuclideanAlgorithm:
    #Define a function to calculate GCD using the Euclidean Algorithm
    """
    parameters:
        a: A positive integer
        b: A positive integer
        
    returns:
        A integer. The GCD of a and b.
    """
    @staticmethod
    def find_GCD(a,b):
        #Ensure a and b are integer
        if a<=0 or b<=0:
            print("Input positive numbers.")
            #return none if the input is invalid
            return None 
        #Inpliment the Euclidean Algorithm
        while b!=0:
            reminder=a%b
            a,b=b,reminder
        return a
    
    @staticmethod
    def get_input(prompt):
        """
        get positive integers from users
        
        parameter:
            prompt: string. The input prompt.
            
        returns:
            A positive integer.
       """
        while True:
            try:
                value=int(input(prompt))
                if value>0:
                    return value
                else:
                    print("Please enter a positive integer.")
                    
            except ValueError:
                print("Please enter an integer.")

if __name__=="__main__":
    #start the program
    print("Start the program.")
    #get input from users
    n1=EuclideanAlgorithm.get_input("Enter the first positive integer:")
    n2=EuclideanAlgorithm.get_input("Enter the second positive integer:")
    
    #calculate GCD
    result=EuclideanAlgorithm.find_GCD(n1,n2)
    #display GCD
    print(f"The GCD of {n1} and {n2} is {result}")
