age=int(input('Enter Your Age : '))
gender= input("Choose Your Gender (M/F) : ")
#p_amount = Principle Amount

if age>=60:

   if gender=='F':

       p_amount=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       interest= p_amount*0.08*Time

       print("Simple interest of the give Capital : ", p_amount, "and Time in Years : ", Time, "is", interest)

   else:

       p_amount=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       interest= p_amount*0.07*Time

       print("Simple interest of the give Capital : ", p_amount, "and Time in Years : ", Time, "is", interest)

else:

   if gender=='F':

       p_amount=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       SimInt= p_amount*0.06*Time

       print("Simple interest of the give Capital : ", p_amount, "and Time in Years : ", Time, "is", SimInt)

   else:

       p_amount=int(input("Enter Capital Amount : "))

       Time= int(input("Enter Time In Years : "))

       SimInt= p_amount*0.05*Time

       print("Simple interest of the given Principle : ", p_amount, "and Time in Years : ", Time, "is", SimInt)