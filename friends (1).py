
# coding: utf-8

# In[ ]:


def mean_num_friends(x):
    totalVal = 0
    totalNum = 0
    for val in x:
        totalVal += val
        totalNum += 1
    return round(totalVal / totalNum, 1)

def median_num_friends(x):
    x.sort()
    size = len(x)
    if len(x) % 2 == 1:
        return x[size // 2]
    else:
        return (x[size // 2] + x[size // 2 - 1]) / 2

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20]
print("mean={}".format(mean_num_friends(num_friends)))

print("median={}".format(median_num_friends(num_friends)))

