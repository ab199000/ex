# a = int(input("Введи 1 сторону треугольника:"))
# b = int(input("Введи 2 сторону треугольника:"))
# c = int(input("Введи 3 сторону треугольника:"))
def check_positive_side(a,b,c):
    if a <=0 or b <=0 or c <=0:
        print("одна из сторон меньше или равна 0")
        return False
    else:
        return True

def two_side_sum(a,b,c):
    if a+b<=c:
        print("сумма двух сторон меньше одной стороны")
    elif a+c<=b:
        print("сумма двух сторон меньше одной стороны")
    elif b+c<=a:
        print("сумма двух сторон меньше одной стороны")
    else:
        return True
    return False
def squaer(a,b,c):
    p= (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**(0.5)
    s = round(s,2)
    print(f'Площадь треугольника:{s}')
    return s   
def type_triangle(a,b,c):
    type_triangle = "";
    if a==b==c:
        type_triangle = "Равносторонний треугольник"
    elif a==b or b==c or a==c:
        type_triangle = "Равнобедренный треугольник"
    else:
        type_triangle = "Обычный треугольник"
    print(type_triangle)
    return type_triangle
        
        
        
def max_side( a,  b,  c):
    if (a >= b and a>=c):return a;
    elif (c >= b and c>=a):return c;
    else: return b;
     
def type_triangle_v2(a,b,c) :
    type_triangle = "";
    second = "";
    third ="";
    max_s = max_side(a, b, c)
    if (a == max_s):
        second = b;
        third = c;
  
    elif (b == max_s):
        second = a;
        third = c;
    
    elif (c == max_s):
        second = a;
        third = b;
    
    else: print("error")
        
   
    if (pow(max_s, 2) == (pow(second, 2) + pow(third, 2))):
        type_triangle = "Прямоугольный треугольник";
    
    elif (pow(max_s, 2) > pow(second, 2) + pow(third, 2)):
        type_triangle = "Тупоугольный треугольник";
    
    elif (pow(max_s, 2) < pow(second, 2) + pow(third, 2)):
        type_triangle = "Остроугольный треугольник";
    
    else:
        print("error")
        return
    print(type_triangle)
    return type_triangle;

def main(a,b,c):
    if check_positive_side(a,b,c)==True and two_side_sum(a,b,c)==True:
        type = type_triangle(a,b,c)
        type_v2 = type_triangle_v2(a,b,c)
        s = squaer(a,b,c)
        return type,type_v2,s
    


    

    
