import csv
 
#----------------------------------------------------------------------
def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    data0 = ["prodId,prodName,avgRating,review,reviewRating".split(",")]
    data1 =[
            "Tyrese,Hirthe,Strackeport,blah,blahha,blhahaha".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
   # Give the Field Names, the column names if I may
    fieldnames = data0[0] 
   # The values inside the columns, they go row wise, as can be seen above. 
    for values in data1[0:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
   # print my_list
    path = "mod_output.csv"
    csv_dict_writer(path, fieldnames, my_list)
