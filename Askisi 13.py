def function(arr,ListaTest):
    count = 0
    MAX = -9999999999999999
    FINALY = []
    for i in range(0, arr.__len__()):
        count += arr[i]
        if count > MAX:
            MAX = count
        if count > 0:
            FINALY.append(arr[i])
        if count < 0:
            count = 0
            FINALY = []
        if count == ListaTest:
            break

    if FINALY == []:
        FINALY.append(max(arr))
    print  int(ListaTest), ':', FINALY
def CrossSum(arr, l, m, h,IntMax):
    sm = 0;
    left_sum = -10000
    Allsum=0
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
    Allsum=left_sum + right_sum
    if (Allsum > IntMax):
        CrossSum(arr, l, m, h, IntMax)
    if (Allsum <IntMax):
        return Allsum



def ArraySum(arr, l, h,IntMax):
    # Base Case: Only one element
    if (l == h):
        return arr[l]
    m = (l + h) // 2
    return max(ArraySum(arr, l, m,IntMax),
               ArraySum(arr, m + 1, h,IntMax),
               CrossSum(arr, l, m, h,IntMax))


Choice=''
while Choice!='X':
    Choice=raw_input("To Run the programm Press [R], for exit Press[X] ")
    if Choice=='R':
        arr =  map(float,raw_input('Enter numbers: ').split(','))
        IntMAX= input("Insert the Max int number you want:  ")
        FloatMax= float(IntMAX)

        print "TEST",arr, "IntMAx User", FloatMax
        n = len(arr)
        ListaTest = ArraySum(arr, 0, n - 1,FloatMax)
        function(arr,ListaTest)

