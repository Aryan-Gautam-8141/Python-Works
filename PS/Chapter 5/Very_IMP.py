# Can you change the values inside a list which is contained in set S?  
s = {8, 7, 12, "Harry", [1,2]}

"""

string          :   immutable(cannot be changed)        :       
list            :   mutable(can be changed)             :
tuple           :   immutable(cannot be changed)        :
dictionary      :   mutable(can be changed)             :       
set             :   mutable(can be changed)             :

| Case                           | Example            | Allowed?  | Reason                 |    Gareebo explanation lelo        |
| ------------------------------ | ------------------ | --------  | ---------------------- |    ------------------------------- |
| **Mutable inside Immutable**   | `{[1,2], 3}`       | ❌ No     | Mutable → unhashable   |    list me tuple nahi daal sakte   |
| **Immutable inside Mutable**   | `[1, (2,3), "hi"]` | ✅ Yes    | List can hold any type |    tuple me list daal sakte hain   |
| **Mutable inside Mutable**     | `[[1,2], [3,4]]`   | ✅ Yes    | Lists can hold lists   |    list me list daal sakte hain    |
| **Immutable inside Immutable** | `(1, (2,3))`       | ✅ Yes    | Both are immutable     |    tuple me tuple daal sakte hain  |


"""

print(s)