# avengerlist=["Ironman","Captain America","Thor"]
# print(avengerlist)
# print(type(avengerlist))
# print(avengerlist[1])
# ratinglist=[10,9,6]
# ral=[avengerlist[0],ratinglist[0],avengerlist[1],ratinglist[1],avengerlist[2],ratinglist[2]]
# ral=[]
# for i in range(0,len(ratinglist)):
#    ral.append(avengerlist[i])
#    ral.append(ratinglist[i])
#    print(ral)
   #Extract superhero Ironman and its score
#    print(ral[0:2])
#    print(ral[2:4])
#    print(ral[4:6])
#    print(ral[-4:-2])

# avengertuple=("Ironman","Captain America","Thor")
# avengerlist[0]="Batman"
# print(avengerlist)
# # avengertuple[0]="Batman"
# print(avengertuple[1],avengertuple[2])
# ral=[["Spiderman",8],["Groot",7],["Black Widow",8]]
# for i in range(0,len(ral)):
#     for j in range(0,len(ral[i])):
#          print(ral[i][j])
         
    
# #last hero
# print(ral[-1][0:])
# for ele in ral:
#     for innerele in ele:
#         print(innerele)


#dictionary
#key -value pair

# avengerdictionary={"Ironman":10,"Captain America":9,"Thor":8}
# print(avengerdictionary)
# print("Ironman's score:",avengerdictionary["Ironman"])
employee_list=[
{"name":"Tony Stark",
   "emp_id":3,
  "address":
  [
        {
            "line1":"Brooklyn",
            "line2":"Newyork",
            "state":"USA",
            "pincode":"800345"
        },
        {
            "line1":"Brklyn",
            "line2":"Neork",
            "state":"UA",
            "pincode":"230345"
        }
    ]
},
{
    "name":"Captain America",
   "emp_id":3,
  "address":
  [
        {
            "line1":"Brooklyn",
            "line2":"Newyork",
            "state":"USA",
            "pincode":"800345"
        },
        {
            "line1":"Brklyn",
            "line2":"Neork",
            "state":"UA",
            "pincode":"230345"
        }
    ]
}

]
# print("Avenger name is :",employee["name"])
# print("Avenger address is :",employee["address"])
emp_pin_list=[]
for emp in employee_list:
    # print("Name:",emp["name"])
    # print("ID :",emp["emp_id"])
    emp_pin_list.append({"name":emp["name"]})
    print(emp_pin_list)
     emp_pin_list[employee_list.index(emp)]["pincode"]=[]
    for address in emp["address"]:
        print(employee_list.index(emp))
       
        emp_pin_list[employee_list.index(emp)]["pincode"].append(address["pincode"])
        print("Pincode is:",address["pincode"])
        # print("address:",address["line1"])

       print(emp_pin_list)


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

emp_pin_list=[]
for emp in employee_list:
    emp_pin_list.append({"name":emp["name"]})
    print(emp_pin_list)
    print(employee_list.index(emp))
    emp_pin_list[employee_list.index(emp)]["Pincode"]=[]
    for address in emp["address"]:
         emp_pin_list[employee_list.index(emp)]["Pincode"].append(address["Pincode"])
         print("Pindcode: ", address["Pincode"])







