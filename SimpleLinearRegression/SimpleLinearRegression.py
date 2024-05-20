import numpy as np

def find_slope_intercept(xi , yi):
    """
    Compute the slope and intercept value in a simple linear equation for xi and yi data. 

    Parameters
    ------
    xi (array_like): The 1D array of data for which to calculate the slope and intercept. 
    yi (array_like): The 1D array of data for which to calculate the slope and intercept. 

    Returns
    ------
    slope, intercept: Return the slope and intercept of a simple linear equation. 

    Raises 
    ------
    ValueError: If the number of elements of xi and yi are not equal. 
    ZeroDivisionError: If the denominator of the slope is zero. 

    Examples
    ------
    >>> xi = np.array([1, 2, 3])
    >>> yi = np.array([4, 5, 6])
    >>> find_slope_intercept(xi , yi)
    The slope is: 1.0 and the intercept is: 3.0. 
    Your simple linear equation is y = 1.0 x + 3.0

    ------

    >>> xi = np.array([1])
    >>> yi = np.array([2])
    >>> find_slope_intercept(xi , yi)
    Traceback (most recent call last):
        raise ZeroDivisionError("The denominator of the slope can not be zero.")

    ------

    >>> xi = np.array([1, 2])
    >>> yi = np.array([4, 5, 6])
    >>> find_slope_intercept(xi , yi)
    Traceback (most recent call last):
        raise ValueError("The number of elements of xi and yi must be equal.")

    """
    if len(xi) != len(yi):
        raise ValueError("The number of elements of xi and yi must be equal.")
    
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