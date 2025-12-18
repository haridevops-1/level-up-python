
# ### 1.
# class Shipping:
#     def __init__(self,order_id,amount,shipping_days):
#         self.order_id = order_id
#         self.amount = amount
#         self.shipping_days = shipping_days
#     def estimate_delivery(self):
#         return self.shipping_days
#     def update_amount(self, value):
#         value += self.amount
# class ExpressShipping(Shipping):
#     def __init__(self, order_id,amount,shipping_days,extra_charge):
#         self.extra_charge = extra_charge
#         super(). __init(order_id, amount,shipping_days,extra_charge):
#     def calculate_total(self,amount,extra_charge):
#         self.amount += self.extra_charge
#     def faster_charge(self, shipping_days):
#         shipping_days - 2
#         return shipping_days

# #### 2.
# class User:
#     current_user = {"username": "", "password": "", "login_status":"", "active":"" }
#     def add_user(self,username, password):
#         self.current_user["username"] = username
#         self.current_user["password"] = password
#         self.current_user["login_status"] = False
#         self.current_user["active"] = True

#     def login_user(self,username,password):
#         if self.current_user["username"] == username and self.current_user["password"] == password and self.current_user["active"] == True:
#             return "Login successful"
#         elif self.current_user["username"] == username and self.current_user["password"] == password and self.current_user["active"] == False:
#             return "User Inactive"
#         else:
#             return "Invalid  credentials"
#     def logout_user(self,username):
#         if self.current_user["username"] == username and self.current_user["login_status"]== True:
#             self.current_user["login_status"] == False
#             return "User logged out"
#         else:
#             return "User not found"
#     def deactivate_user(self,username):
#         if self.current_user["username"] == username:
#             self.current_user["active"] = False
#         else:
#             return "User not found"