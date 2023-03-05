import test as pd
print(pd.display_message())
import astor
from Modtest.Sub_folder.pack1 import classimpo_pack as  pcd
from Modtest.Sub_folder.pack2 import classimpo_pack2
pcd.sum()
classimpo_pack2.sum()

from Modtest.test import classimpo
classimpo.sum(2)
from Modtest.test_1 import classimpo_1
classimpo_1.sum_1(7,2)

from test_1 import classimpo_1
classimpo_1.sum_1(2,333)



from Modtest.Sub_folder import pack2
from Modtest.Sub_folder import pack1
pack2.classimpo_pack2.sum(7)
pack1.classimpo_pack.sum(77777777777777777777)


from Modtest.Sub_folder.sub_folder_lvl_2 import Sub_pack1
from Modtest.Sub_folder.sub_folder_lvl_2 import  Sub_pack2 as tt
Sub_pack1.classimpo_sub_pack.sums()
tt.classimpo_sub_pack_as.sums_as()

Sub_pack1.display_message_sub_pack()
tt.display_message_sub_pack_as()

# from Modtest.Sub_folder.sub_folder_lvl_2.Sub_pack2 import classimpo_sub_pack_as

def neon(x):
    return "i have a light"

neon(98787)

class argon1():
    def argon(p):
        p=4+p
        return p


argon1.argon(6)
