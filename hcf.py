def calculate_hcf(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b
    for i in range(1,smaller+1):
        if((a%i==0)and(b%i==0)):
            hcf=i
    return hcf
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print("The hcf of two numbers is",calculate_hcf(n1,n2))