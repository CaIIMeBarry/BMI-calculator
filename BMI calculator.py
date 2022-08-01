height=float(input('height :'))
weight=float(input('weight :'))

BMI=weight/height**2
if BMI <18.5:
    print('Underweight ')

elif 18.5<=BMI<25:
    print('Normal')    
    
elif 25<=BMI<30:
     print('Overweight')   
     
else:
    print('Obesity')     