pro = {
    "pen" : 10,
    "bottle": 50,
    "note": 50
}                                                                 #obtain the available stocks

# created a class of exception handeling


class ProductNotFound(Exception):
    pass

class OutOfStock(Exception):
    pass

try:
    pr = input("select the product you want to order\n1.pen,\n2.bottle,\n3note \n Enter here!: ")  #to get product
    qyt = int(input("Enter the quantity of the product: "))                                        #to get Quantity of product

    if pr not in pro.keys():
        raise ProductNotFound(" Product not found")
    if qyt > pro[pr]:
        raise OutOfStock("Out-of-stock")
except (ProductNotFound,OutOfStock) as e:
    print(e)
else:
    print("Order was successful")
    pro[pr] -= qyt                                              # to reduce the ordered quantity from the available stock

finally:
    print("Thank you for order")


print( "Available products:",pro)                                # to show the available stocks


