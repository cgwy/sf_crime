#Insert all of the following fields to mysql: Dates,Category,Descript,DayOfWeek,PdDistrict,Resolution,Address,X,Y
def _train_to_mysql(cnx):
    cursor = cnx.cursor()
    import csv
    counter = 0
    with open('../sf/train.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            add_record = "INSERT INTO train (Dates,Category,Descript,DayOfWeek,PdDistrict,Resolution,Address,X,Y) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data_record = row['Dates'], row['Category'], row['Descript'], row['DayOfWeek'], row['PdDistrict'], row['Resolution'], row['Address'], row['X'], row['Y']
            cursor.execute(add_record, data_record)

            counter += 1
            if counter % 10000 == 0:
                print 'finished inserting ', counter, ' lines'
    cnx.commit()
    cursor.close()
    return

def _fix_PdDistrict():

if __name__ == "__main__":
    import mysql.connector
    from mysql.connector import errorcode
    try:
        cnx = mysql.connector.connect(user='wk', password='wk', host='127.0.0.1', database='sf')
        #_train_to_mysql(cnx)
        cnx.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist"
        else:
            print err
