1.)	
  A.)	
    Using the Bisection Method with initial guesses as xl = 0 and xu = 2 for the equation 
    0 = e^(x/2) – 5(1 - x), I found that the root with a relative error less than 1% was 0.714844.
  B.)	
    Using Newton’s Method with an initial guess of xi = 0.7 for the equation 
    0 = e^(x/2) – 5(1 - x), I found that the root with a relative error less than 1% was 0.71417.
  C.)	
    Using the Secant Method with initial guesses as xi-1 = 0 and xi = 2 for the equation 
    0 = e^(x/2) – 5(1 - x), I found that the root with a relative error less than 1% was 0.714170.
    
For parts A and C, I implemented a function labeled relative_error that takes in an old x and a 
new x and returns a boolean representing whether or not the relative error is less than 1%. 
Additionally, I used a while loop so that it will only stop iterating when the relative error is less than 1%.

2.)	
  After implementing a program in python that finds the closest value to the vertex of the function f(x) = 4x – 1.8x^2 + 1.2x^3 – 0.3x^4 
  using parabolic interpolation with 10 maximum iterations, starting with x1 = 1.75, x2 = 2, and x3 = 2.5, I found that the global max 
  is y = 5.8853392 located at x = 2.326857

3.)	
  After implementing a python program that uses a variation of the golden-section search method to find the inflection point for the 
  normal distribution function y = e^-x^2 for positive x, I was displayed with the answer: x = 0.70711. To create a golden-section search 
  that finds the POI instead of the max/min, I had to create a function that represents the second derivative. Using calculus, we know 
  that POIs occur where f’’ = 0.
