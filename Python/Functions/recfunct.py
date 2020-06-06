#repeats its own functin(recursive) until an argument is meant (Recursive function)
def calc_sum(n):
   if n == 1: #ends the loop once arg is met
      return 1 
   else:
      return n + calc_sum(n-1) #calls 'n' and 'n' rounds

sum = calc_sum(3) #makes 1st call with 3 which n
print(sum) #prints sum where n is 3 (call else loop)
