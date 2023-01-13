import pandas as pd
data={
    "apples":[3,4,6,9],
    "oranges":[1,5,2,6]
}
index=["Aaron","Lee","Steve","Shaun"]
purchase=pd.DataFrame(data,index=index)
print(purchase,type(purchase))
# print(purchase["apples"])
print(purchase.loc["Aaron"])
print(purchase["apples"])

