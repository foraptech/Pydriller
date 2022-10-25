# # import datetime
# # import mysql.connector
# #
# # name = input("Please Enter Your Name :")
# # english =int(input("Enter your marks : "))
# # urdu = int(input("Enter your marks : "))
# # maths = int(input("Enter your marks : "))
# # totalmarks = urdu+maths+english
# # percentage = (totalmarks*100) /300
# # current_time = datetime.datetime.now()
# # print(f"Your totalmarks is{totalmarks} and percenta is {percentage}")
# # f = open("Studentmarks.txt","a")
# # f.write(f"{name} Your English marks is, {english}\nYour Urdu marks is, {urdu}\nYour maths marks is, {maths}\nYour total is {totalmarks}Your percentage is{percentage}")
# # f.close()
# #
# # DbCon = mysql.connector.connect(
# #     host = "localhost",
# #     user = "root",
# #     password = "",
# #     database = "studentdb"
# # )
# #
# # cursor = DbCon.cursor()
# # insert_query = "INSERT INTO `studentdata` (`Name`, `English`, `Urdu`, `Maths`, `Total`, `Percentage`, `Currentdate`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
# # myvalue = [name, english, urdu, maths, totalmarks, percentage, current_time]
# # cursor.execute(insert_query,myvalue)
# # DbCon.commit()
# # DbCon.close()
#
# import pandas
# from openpyxl.workbook import Workbook
# import lxml
# khaadi = {
#     "name": ["3 Piece Suit","Shirts","Shoes","Socks","Accessories","Dupatta"],
#     "price": ["3,500","5000","6000","7000","8000","9000"]
# }]
# convert_table = pandas.DataFrame(khaadi)
# print(convert_table)
#
# convert_table.to_excel("mahad.xlsx")
# convert_table.to_csv("mahad.csv")
# convert_table.to_xml("mahad.xml")
# convert_table.to_json("mahad.js")


from pydriller import Repository
import pandas
import lxml
Name, Date, Msg = [] , [] , []

for m in Repository(path_to_repo="https://github.com/Kaggle/kaggle-api").traverse_commits():
    Name.append(m.committer.name)
    Date.append(m.committer_date)
    Msg.append(m.msg)

Github_Dict = {
    "CommiterName" : Name,
    "CommitDate" : Date,
    "Message" : Msg,
}

Convert_to_Table = pandas.DataFrame(Github_Dict)
Convert_to_Table.to_csv("Repositorydata.csv",index= False)
Convert_to_Table.to_xml("RepositoryData.xml")

print("Data saved successfully")