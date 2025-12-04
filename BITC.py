#Basic earning-tax calculator

earning = float(input("Enter your Taxable earning: "))
tax = 0
Slab1 = 300000
Slab2 = 700000
Slab3 = 1000000
Slab4 = 1200000
Slab5 = 1500000
Slab6 = 5000000
Slab7 = 10000000
Slab8 = 20000000

if earning <= Slab1:
    tax = 0

elif earning <= Slab2:
    tax = (earning-Slab1)*0.05

elif earning <= Slab3:
    tax = ((Slab2-Slab1)*0.05) + ((earning-Slab2)*0.1)

elif earning <= Slab4:
    tax = ((Slab2-Slab1)*0.05) + ((Slab3-Slab2)*0.1) + ((earning-Slab3)*0.15)

elif earning <= Slab5:
    tax = ((Slab2-Slab1)*0.05) + ((Slab3-Slab2)*0.1) + ((Slab4-Slab3)*0.15) + ((earning-Slab4)*0.2)

elif earning <= Slab6:
    tax = ((Slab2-Slab1)*0.05) + ((Slab3-Slab2)*0.1) + ((Slab4-Slab3)*0.15) + ((Slab5-Slab4)*0.2) + ((earning-Slab5)*0.3)

elif earning <= Slab7:
    base = ((Slab2-Slab1)*0.05) + ((Slab3-Slab2)*0.1) + ((Slab4-Slab3)*0.15) + ((Slab5-Slab4)*0.2) + ((Slab6-Slab5)*0.3) + ((Slab7-earning)*0.3)
    tax = base + base*0.1

elif earning <= Slab8:
    base = ((Slab2-Slab1)*0.05) + ((Slab3-Slab2)*0.1) + ((Slab4-Slab3)*0.15) + ((Slab5-Slab4)*0.2) + ((Slab6-Slab5)*0.3) + ((Slab7-Slab6)*0.3) + ((earning-Slab7)*0.3)
    tax = base + base*0.15

else:
     base = ((Slab2-Slab1)*0.05) + ((Slab3-Slab2)*0.1) + ((Slab4-Slab3)*0.15) + ((Slab5-Slab4)*0.2) + ((Slab6-Slab5)*0.3) + ((Slab7-Slab6)*0.3) + ((Slab8-Slab7)*0.3) + ((earning-Slab8)*0.3)
     tax = base + base*0.25

TotalTax = tax + (tax*0.04)

print("Taxable earning: ","₹ ",round(earning))
if tax <= 0:
    print("NO TAX PAYABLE")
else:
    print("Basic Tax: ","₹ ",round(tax))
    print("Total Tax Payable: ","₹ ",round(TotalTax))
