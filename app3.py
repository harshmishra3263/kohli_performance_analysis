# def multiplication(a,b):
#     product=a*b
#     return product


# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# product=multiplication(a,b)
# print(product)

def get_employee_address_details(employee_list,key):
    emp_address_list=[]
    for emp in employee_list:
        emp_address_list.append({"name":emp["name"]})
        emp_address_list[employee_list.index(emp)][key]=[]
        for address in emp["address"]:
            emp_address_list[employee_list.index(emp)][key].append(address[key])
        
    return emp_address_list



employee_list = [
    {
        "name": "Tony Stark",
        "emp_id": 3,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700107"
            }
        ]
    },
    {
        "name": "Steve Rogers",
        "emp_id": 6,
        "address": [
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700117"
            },
            {
                "line1": "fff",
                "line2": "hhh",
                "state": "WB",
                "Pincode": "700127"
            }
        ]
    }
]
