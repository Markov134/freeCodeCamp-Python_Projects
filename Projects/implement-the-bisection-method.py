def square_root_bisection(number, tolerance=0.01, max_iteration=100):
       if number < 0:
           raise ValueError("Square root of negative number is not defined in real numbers")
       if number == 0 or number == 1:
           print(f"The square root of {number} is {number}")
           return number
       
       low = 0.0
       high = max(1.0, number)
       
       for _ in range(max_iteration):
           mid = (low + high) / 2.0
           print(f"{_} {mid}")
           square_target = mid * mid 
           if abs(high - low) <= tolerance:
               print(f"square_target {square_target}")
               print(f"The square root of {number} is approximately {mid}")
               return mid
           if square_target > number:
               high = mid
           else:
               low = mid
       
       print(f"Failed to converge within {max_iteration} iterations")
       return None
   
print(square_root_bisection(0.001, 1e-7, 50))
