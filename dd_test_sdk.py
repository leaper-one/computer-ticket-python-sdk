from ct_api import CT_API
import ct_config
ct = CT_API(ct_config)

# a = ct.creatUser()
# print(a)

b = ct.pub('blue')
print(b)