#Ques 7
import pickle
def countrec():
    count = 0
    with open("PATIENTS.dat","rb") as file:
        try:
            while 1:
                record = pickle.load(file)
                    if record[2] == 'COVID-19':
                        count+=1
                        print(f"PID: {record[0]}  NAME: {record[1]}  DISEASE: {record[2]}")
        except EOFError:
            print("TOTAL COVID-19 PATIENTS: ",count)


#Ques 8
# (i)
import pickle
def CreateFile():
    with open("Book.dat","ab") as file:
        b_no = int(input("Enter the book number: "))
        b_name = input("Enter the book name: ")
        b_author = input("Enter the author name: ")
        b_price = int(input("Enter the book price: "))
        record = [b_no,b_name,b_author,b_price]
        pickle.dump(record,file)
        print("RECORD SUCCESSFULLY INSERTED .......")

# (ii)
import pickle
def CountRec(Author):
    count = 0
    with open("Book.dat","rb") as file:
        try:
            while True:
                record = pickle.load(file)
                if record[2] == Author:
                    count+=1
                
        except EOFError:
            return count


#Ques 9
import pickle
def 
