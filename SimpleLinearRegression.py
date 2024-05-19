import numpy as np

def find_slope_intercept(xi , yi):
    
    if len(xi) != len(yi):
        raise ValueError("The number of xi and yi elements must be equal.")
    
    for i in xi , yi:
        """
        This loop calculate the slope and the intercept of a simple linear equation (y = θx + c). 
        It calculates the θ using the formula: Σ (x' * y') / Σ (x' ** 2)   
        Finally, θ replaces in this formula: c = ȳ - θx̄  and it computes the c after replacement. 
        θ is slope and c is intercept of a simple linear equation. 
        """
        mean_x = np.mean(xi)
        mean_y = np.mean(yi)
        xp = xi - mean_x
        yp = yi - mean_y
        slope = np.sum(xp * yp) / np.sum(xp ** 2)
        if np.sum(xp ** 2) == 0:
            raise ZeroDivisionError("The denominator of the slope can not be zero.")
        
        intercept = mean_y - (slope * mean_x)
    return f"The slope is: {slope} and the intercept is: {intercept}. \nYour simple linear equation is y = {slope} x + {intercept}"