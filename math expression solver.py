def expt(x,n):
    p = 1
    c = 0
    '''The termination condition is when c becomes equal to n
       The invariant here is that the next value of p is always the
       product of previous value of p and x'''
    while c !=n:
        p = p*x
        c +=1
    return p

def elem_list(l,d):
    l[d]
    return l[d]

def sum_list(f,l,a,b):
    c=0
    '''The invariant is that the next value of c is the sum of the 
       previous value and the sum of the corresponding element of list
       We keep on storing the sum in the variable "c" '''
    while(a<=b):
         c = c + f(l,a)
         a = a + 1
    # After the loop ends, we return c which stores the sum
    return c 

def eval_main(s):
    if len(s) == 0:
        return 0
    store_list = []
    sign = "+"
    n = 0
    '''In this what we do is we keep popping out the first element of the list and then
       if a certain element comes out to be an operator then we apply the conditions as below
       The termination condition is when length of list becomes equal to 0'''
    while len(s) > 0:
        a = s.pop(0)
        if a=="0" or a=="1" or  a=="2" or  a=="3" or  a=="4" \
         or  a=="5" or  a=="6" or  a=="7" or  a=="8" or  a=="9":
             n = (n*10)+int(a)
        if a == "(":
            n = eval_main(s)
        if len(s) == 0 or (a == "." or a == "+" or a == "-" or a == "*" or a == "/" or a == ")"):
            if sign == "+":
                    store_list.append(n)
            elif sign == "-":
                    store_list.append(-n)
            elif sign == "." and store_list[-1] >= 0:
                    store_list[-1] = store_list[-1]+(n/expt(10,len(str(n))))
            elif sign == "." and store_list[-1] < 0:
                    store_list[-1] = store_list[-1]-(n/expt(10,len(str(n))))
            elif sign == "*":
                    store_list[-1] = store_list[-1]*n
            elif sign == "/":
                    store_list[-1] = float(store_list[-1]/float(n))
            sign = a
            n = 0
            if sign == ")":
                    break
    # After the loop ends, we sum up all the elements of the list and return that
    return sum_list(elem_list,store_list,0,len(store_list)-1)

def evaluate(s):
        A = []
        '''this loop is used to create a list of the characters of a string
           so we iterate over the string and keep on appending 
           each character to the empty list'''
        for i in s:
            A.append(i)
        # after the loop ends we return the appended list A
        return float(eval_main(A))
