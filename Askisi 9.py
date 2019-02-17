def CrossSum(arr, l, m, h):
    sm = 0;
    left_sum = -10000
    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if (sm > left_sum):
            left_sum = sm
    sm = 0;
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm
    return left_sum + right_sum;

def ArraySum(arr, l, h):
    # Base Case: Only one element
    if (l == h):
        return arr[l]
    m = (l + h) // 2
    return max(ArraySum(arr, l, m),
               ArraySum(arr, m + 1, h),
               CrossSum(arr, l, m, h))


arr = map(int, raw_input('Enter numbers: ').split(','))
n = len(arr)
ListaTest = ArraySum(arr, 0, n - 1)
count = 0
MAX=-9999999999999999
FINALY=[]
for i in range(0,arr.__len__()):
    count+= arr[i]
    if count> MAX:
        MAX= count
    if count >0 :
        FINALY.append(arr[i])
    if count< 0 :
        count = 0
        FINALY=[]
    if count== ListaTest:
        break

if FINALY==[]:
    FINALY.append(max(arr))
print  ListaTest,':',FINALY

