import numpy as np
store = np.array(["X", "X", "Y", "Z", "Z"])
z = [1,2,3,4,5]
a = (store == "Z")
b = z[a]

print(z[a])