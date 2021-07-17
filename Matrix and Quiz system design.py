# question 1
class Quiz:
  def __init__(self,title,correctoptions_list):
    self.title=title
    self._correctoptions_list=correctoptions_list.copy()
    self._studentans = [] #we define an empty list to record student's answers
  
  def att_helper(self,attemptedAnswers,entrynum):
    #stores the student's entry number and marked answers in a the list defined by us in the quiz object
    s = [a for a,b in self._studentans]
    if entrynum not in s :
      self._studentans.append((entrynum,attemptedAnswers))
  
  def unattempt_help(self,coursecode,entrynum):
      #checks if the the studentans list has student entry number in it.if it is found we return an empty list 
      # if we do not find that entry number in that list we return a tuple of the coursecode and the quiz title
      a = []
      m = [a for a,b in self._studentans]
      if entrynum not in m :
           a.append((coursecode,self.title)) 
           return a
      else:
        return [] 
  def Avg_help(self,entrynum):
        # if the entry number is present in studentans list then it checks each answer of the student with
        # the correct answers list and then returns a tuple of the marks in that quiz and the number of quiz attempted
        # if the quiz is unattempted we just return (0,0) which signifies that the quiz has not been attempted yet
        l = [a for a,b in self._studentans]
        if entrynum in l:
         i = l.index(entrynum)
         x,y = self._studentans[i]
         correctans=0
         for p in range(len(self._correctoptions_list)):
          if y[p] == self._correctoptions_list[p]:
            correctans+=1
         return (correctans,1)
        else:
          return (0,0)      
          
class Course:
  def __init__(self,courseCode,ListOfQuizzes):
    self.courseCode=courseCode
    self._ListOfQuizzes = ListOfQuizzes.copy()
  
  def attempt_course(self,quizTitle,attemptedAnswers,entrynum) :
    # if quiz title is there in list of quizzes then we break the loop
    # and then use the att_helper method of the Quiz class to just store the attempted answers
    for item in (self._ListOfQuizzes):
         if item.title==quizTitle:
          break 
    item.att_helper(attemptedAnswers,entrynum)   
  
  def Unattempt_course(self,entrynum):
    # we use the unattempt_help method to get a list of unattempted quizzes in that course 
    e = []
    for elem1 in (self._ListOfQuizzes): 
      e = e + (elem1.unattempt_help(self.courseCode,entrynum))
    return e  

  def Average_course(self,entrynum):
    # This is used for calculating the average score of the student 
    # we use the Avg_help method and for each quiz we add the scores 
    # and store it in score variable and the number of quizzes in the num_quizzes variable
    score = 0
    num_quizzes = 0
    for elem2 in (self._ListOfQuizzes):
      (a,b) = elem2.Avg_help(entrynum) 
      score += a 
      num_quizzes +=b
    if num_quizzes == 0: # if the student has unattempted no quiz then display the following message
        return 'ERROR: Please attempt a quiz in order to get average '
    else :
        return (score/num_quizzes) #otherwise return the average which is sum of scores/number of quizzes
class Student:
  def __init__(self,entryNo,ListOfCourses):
    self.entryNo=entryNo
    self._ListOfCourses=ListOfCourses.copy()
   
  def attempt(self, courseCode, quizTitle, attemptedAnswers):
     #if coursecode is there in list of courses then we break the loop
     # next we use the attempt_course method to store the student's answers
     for elem in (self._ListOfCourses):
       if elem.courseCode==courseCode:
        break
     elem.attempt_course(quizTitle,attemptedAnswers,self.entryNo)
  def getUnattemptedQuizzes(self):
    # we check in the list of courses and then use the Unattempt_course method to
    # get a list of tuples of all the unattempted quizzes
    r = []
    for elem3 in (self._ListOfCourses):
     r = r + (elem3.Unattempt_course(self.entryNo))
    return r  

  def getAverageScore(self,courseCode):
    # we use the Average_course method to get the average of that course 
    for elem4 in (self._ListOfCourses):
       if elem4.courseCode==courseCode:
        break
    return(elem4.Average_course(self.entryNo))

col100q1 = Quiz('Quiz1', ['a','b','b'])
col100q2 = Quiz('Quiz2', ['b','d','c'])
col100 = Course('COL100', [col100q1, col100q2])
mtl100q1 = Quiz('Quiz1', ['a','b','d'])
mtl100q2 = Quiz('Quiz2', ['d','c','a'])
mtl100 = Course('MTL100', [mtl100q1, mtl100q2])
s1 = Student('2019MCS2562', [col100, mtl100])
s2 = Student('2017CS10377', [col100])
s2.attempt('COL100', 'Quiz1', ['a','b','c'])
print (s1.getUnattemptedQuizzes())  
print (s2.getAverageScore('COL100'))

        
# question 2
class Matrix:
    def __init__(self,l):
        self.row = len(l)
        self.columns = len(l[0])
        self.l = l 
    
    def __str__(self):
        s = '' # we define an empty string and then keep on adding each element of the matrix 
        for elem in self.l:
          for i in elem :
            s = s + '{} '.format(i)
          s = s + '\n'
        return s
    
    def __add__(self,m):
        assert self.row == m.row 
        assert self.columns == m.columns 
        # we define a 2-D array containing only zeroes
        # and then we add the (i,j)th element of both the matrices and store it in the array
        result =  [[0 for i in range(self.columns)] for i in range(self.row)]
        for i in range(self.row):    
            for j in range(self.columns): 
              result[i][j] = self.l[i][j] + m.l[i][j] 
        return Matrix(result)
    
    def __sub__(self,m):
        assert self.row == m.row 
        assert self.columns == m.columns 
        # similar to the add method we define a 2-d array and 
        # subtract the (i,j)th element of the matrices and store it in the 2-D array
        result =  [[0 for i in range(self.columns)] for i in range(self.row)]
        for i in range(self.row):    
            for j in range(self.columns): 
              result[i][j] = self.l[i][j] - m.l[i][j] 
        return Matrix(result)
    
    def __mul__(self,m):
        # if m is an integer or a floating number then we just 
        # multiply each element of the matrix by m
        if (isinstance(m,int)) or (isinstance(m,float)):
            for i in range(self.row):
              for j in range(self.columns): 
                  self.l[i][j] = self.l[i][j] * m  
            return Matrix(self.l)
        # if m is another matrix then we multiply the (i,k)th element of matrix1
        # and (k,j)th element of m and then store it in the result matrix
        elif isinstance(m,Matrix):
            assert self.columns == m.row 
            result = [[0 for i in range(m.columns)]for i in range(self.row)]
            for i in range(self.row): 
                for j in range(m.columns): 
                   for k in range(m.row): 
                      result[i][j] += self.l[i][k] * m.l[k][j] 
            return Matrix(result)
    
    def toSparse(self):
      e = [] # we initialise an empty list
      for i in range(self.row):
        p = []
        for j in range(self.columns):
          if self.l[i][j] != 0: # if (i,j)th element of the matrix is non-zero 
            p.append((j,self.l[i][j])) # we append the tuple of column number and the value at that position
        e.append(p)
      return e

class SparseMatrix:
    def __init__(self,spars,nrows,ncols):
        self.nrows = nrows 
        self.ncols = ncols
        self.spars = spars 
    
    def __str__(self):
        s = '' # we define a empty string
        for i in range(self.nrows):
           if self.spars[i] == [] : # if the ith element is a null list we append zeroes to s
             for k in range(self.ncols):
              s = s + '{} '.format(0)
             s = s + '\n'
           else :
            j = 0 # first we check with the 1st tuple in a row 
            for k in range(self.ncols):
              # then we take different cases for that element and accordingly append 
              # to string s 
              a,b = self.spars[i][j]
              if a == k and j != (len(self.spars[i]) - 1):
                 s = s + '{} '.format(b)
                 j+=1
              elif j == len(self.spars[i]) - 1 and a== self.ncols - 1 and a == k:
                  s = s + '{} '.format(b)
              elif j == len(self.spars[i]) - 1 and a!= self.ncols and a == k:
                  s = s + '{} '.format(b)
              else :
                  s = s + '{} '.format(0)
            s = s + '\n' 
        return s # finally we return the string s
    
    def toDense(self):
      l = [] #initialize an empty list
      for i in range(self.nrows):
           if self.spars[i] == [] : #if a row is [] then we append a list of zeroes to l
             b = [0]*self.ncols
             l.append(b)
           else :
            j = 0 
            em = []
            # again here also we traverse each and every tuple in a row and 
            # and accordingly make different cases and append to em
            for k in range(self.ncols):
              a,b = self.spars[i][j]
              if a == k and j != (len(self.spars[i]) - 1):
                 em.append(b)
                 j+=1
              elif j == len(self.spars[i]) - 1 and a== self.ncols - 1 and a == k:
                  em.append(b)
              elif j == len(self.spars[i]) - 1 and a!= self.ncols and a == k:
                  em.append(b)
              else :
                  em.append(0)
            l.append(em) #after completion of this for loop we append em to l
      return l # in the end we return l which will be in dense form
    
    def __add__(self,sm):
      assert self.nrows == sm.nrows
      assert self.ncols == sm.ncols
      l = [] # we initialise an empty list
      for i in range(self.nrows):
        if self.spars[i] == []: # if the ith row is null then addition simply means appending the ith row of the other matrix
          l.append(sm.spars[i])
        elif sm.spars[i] == []:
          l.append(self.spars[i])
        else :
          ll = []
          # we start with the 1st tuple of the ith rows of both the matrices
          j = 0 
          x = 0
          # then we apply different cases for the two matrices elements and append them to ll
          for k in range(self.ncols):
            a,b = self.spars[i][j]
            p,q = sm.spars[i][x]
            if a < p and (a,b) != self.spars[i][-1]  :
              ll.append((a,b))
              j +=1
            elif a < p and (a,b) == self.spars[i][-1] and (p,q) == sm.spars[i][-1] :
                if a not in [r for r,s in ll]:
                   ll.append((a,b))
                   ll.append((p,q))
                else :
                  ll.append((p,q))
            elif a < p and (a,b) == self.spars[i][-1] and (p,q) != sm.spars[i][-1] :
              ll.append((p,q))
              x+=1
            elif a == p and (a,b)!=self.spars[i][-1] and (p,q)!=sm.spars[i][-1]:
              ll.append((a,b+q))
              j+=1
              x+=1
            elif a == p and (a,b)==self.spars[i][-1] and (p,q)==sm.spars[i][-1]:
              ll.append((a,b+q))
            elif a == p and (a,b)==self.spars[i][-1] and (p,q)!=sm.spars[i][-1]:
              ll.append((a,b+q))
              x+=1
            elif a == p and (a,b)!=self.spars[i][-1] and (p,q)==sm.spars[i][-1]:
              ll.append((a,b+q))
              j+=1
            elif a > p and (p,q) != sm.spars[i][-1] :
              ll.append((p,q))
              x+=1
            elif a > p and (p,q) == sm.spars[i][-1] and (a,b) == self.spars[i][-1] :
                if p not in [c for c,d in ll]:
                 ll.append((p,q))
                 ll.append((a,b))
                else :
                  ll.append((a,b))
            elif a > p and (p,q) == sm.spars[i][-1] and (a,b) != self.spars[i][-1]:
              ll.append((a,b))
              j+=1
          l.append(ll) #at the end of the for loop we append ll to l
      return SparseMatrix(l,self.nrows,self.ncols) #finally we print the formatted matrix
    
    def __sub__(self,sm):
      # similar like addition 
      assert self.nrows == sm.nrows
      assert self.ncols == sm.ncols
      l = []
      for i in range(self.nrows):
        if self.spars[i] == []:
          l.append(sm.spars[i])
        elif sm.spars[i] == []:
          l.append(self.spars[i])
        else :
          ll = []
          j = 0 
          x = 0
          for k in range(self.ncols):
            a,b = self.spars[i][j]
            p,q = sm.spars[i][x]
            if a < p and (a,b) != self.spars[i][-1]  :
              ll.append((a,b))
              j +=1
            elif a < p and (a,b) == self.spars[i][-1] and (p,q) == sm.spars[i][-1] :
                if a not in [r for r,s in ll]:
                   ll.append((a,b))
                   ll.append((p,-1*q))
                else :
                  ll.append((p,-1*q))
            elif a < p and (a,b) == self.spars[i][-1] and (p,q) != sm.spars[i][-1] :
              ll.append((p,-1*q))
              x+=1
            elif a == p and (a,b)!=self.spars[i][-1] and (p,q)!=sm.spars[i][-1]:
              ll.append((a,b-q))
              j+=1
              x+=1
            elif a == p and (a,b)==self.spars[i][-1] and (p,q)==sm.spars[i][-1]:
              ll.append((a,b-q))
            elif a == p and (a,b)==self.spars[i][-1] and (p,q)!=sm.spars[i][-1]:
              ll.append((a,b-q))
              x+=1
            elif a == p and (a,b)!=self.spars[i][-1] and (p,q)==sm.spars[i][-1]:
              ll.append((a,b-q))
              j+=1
            elif a > p and (p,q) != sm.spars[i][-1] :
              ll.append((p,-1*q))
              x+=1
            elif a > p and (p,q) == sm.spars[i][-1] and (a,b) == self.spars[i][-1] :
                if p not in [c for c,d in ll]:
                 ll.append((p,-1*q))
                 ll.append((a,b))
                else :
                  ll.append((a,b))
            elif a > p and (p,q) == sm.spars[i][-1] and (a,b) != self.spars[i][-1]:
              ll.append((a,b))
              j+=1
          l.append(ll)
      return SparseMatrix(l,self.nrows,self.ncols)
    
    def __mul__(self,sm):
      # if sm is an integer or a floating point number 
      # we multiply each value of the matrix by this number 
      if (isinstance(sm,int)) or (isinstance(sm,float)):
        l = [] #define an empty list
        for i in range(self.nrows):
          if self.spars[i] == [] :#if the ith row is null then multiplication has no effect so we append that emppty list
            l.append(self.spars[i])
          else :
            ll = [] # define an empty list
            #we multiply y by sm and then append it to ll 
            for (x,y) in self.spars[i] :
              y = y * sm
              ll.append((x,y))
            l.append(ll) # after this for loop we append ll to l
        return SparseMatrix(l,self.nrows,self.ncols)










 


    
