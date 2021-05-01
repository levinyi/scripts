# coding: utf-8
import sys
import re
import pandas as pd
import time


class MyClass(object):
    def add(self, df):
        print(df)
        q_gender = input("add Female or Male: [F/M]: ")
        while q_gender.upper() not in ['F',"FEMALE",'MALE','M']:
            q_gender = input("just type F or M : ")

        q_type = input("add type :")
        q_id = input("add new id :")
        
        print("you are going to add a new category: \n   {}\t{}\t{}".format(q_gender, q_type, q_id))
        asure = input("are you sure to add this new category? [Yes/No]")
        if asure.lower() in ["yes","y", ""]:
            print("adding a new type...")
            f2 = df.append([{'gender':q_gender,'type':q_type,'number':q_id}], ignore_index=True)
            f2.to_csv("current.queuing.txt", index=False, sep="\t")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            action = 'add'
            write_log([timestamp,action,q_gender,q_type,q_id])
            print(f2)
            print("Added a record Successfully.")
        else:
            print("Nothing has changed in the database")
            sys.exit()

    def delete(self, df):
        print(df)
        print("just type the index number to delete.")
        delete_index = int(input("Which index do you want to delete: "))
        print("index list: {}".format(df.index.tolist()))
        print(delete_index)
        while delete_index not in df.index.tolist():
            delete_index = int(input("Not found. please retype a index: "))
        
        gender = df.loc[delete_index,'gender']
        category = df.loc[delete_index, 'type']
        number = df.loc[delete_index, 'number']
        print("delete: {} {} {} {}".format(delete_index,gender,category,number))

        asure = input("are you sure to delete this record: {} : ".format(delete_index))
        if asure.lower() in ['yes','y', ""]:
            print("deleting record...")
            f2 = df.drop(index = delete_index)
            f2.to_csv("current.queuing.txt", index=False, sep="\t")
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            action = 'delete'
            write_log([timestamp,action,gender,category,number])
            print(f2)
            print("delete a record Successfully.")
        else:
            print("Nothing has changed in the database")
            sys.exit()

    def update(self, df):
        print(df)
        updated_index = int(input("which item do you want update? type number: "))
        print("index list: {}".format(df.index.tolist()))
        while updated_index not in df.index.tolist():
            updated_index = int(input("Not found. please retype a index number: "))
        asure = input("are you sure to update this record: {}... {} : ".format(updated_index,df.loc[updated_index,'number']))
        if asure.lower() in ['yes','y',""]:
            print("updating record...")
            updated_id = df.loc[updated_index,'number']
            prog = re.compile(r'([A-Z]+)([0-9]+)')
            result = prog.match(updated_id)
            print(result)
            if result:
                a, b = result.groups() # ('F', '001')
            new_id = a + str(int(b) +1).zfill(len(b))
            print("the suggestion number is : {}".format(new_id))

            asure = input("are you sure to update {} to {} :".format(updated_id,new_id))
            if asure.lower() in ['yes','y',""]:
                df['number'][updated_index] = new_id
                df.to_csv("current.queuing.txt", index=False, sep="\t")
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
                action = 'update'
                gender = df.loc[updated_index,'gender']
                category = df.loc[updated_index, 'type']
                number = df.loc[updated_index, 'number']
                tonumber = new_id
                write_log([timestamp,action,gender,category,updated_id,tonumber])
                print(df)
                print("updated a record Successfully.")
            else:
                print("Nothing has changed in the database")
                sys.exit()
        else:
            print("Nothing has changed in the database")
            sys.exit()


def write_log(con):
    with open('current.queuing.log.txt', 'a+') as f:
        f.write("{}\n".format("\t".join(con)))

def main():
    f1 = pd.read_table("current.queuing.txt")
    func = ['add','delete','update']
    print(f1)
    print("""you can select a function to manipulate this table:['add','del','update','q']
       add : if you want create a new category.  type  "add".
    delete : if you want delete a category.      type  "delete".
    update : if you want updata one category.    type  "update".
         q : type "q" to exit.
    """)
    method_name = input("please select a method from above to continue,or type 'q' to exit.\n :")
    my_cls = MyClass()
    
    if method_name == "q":
        sys.exit()
    method = None
    try:
        method = getattr(my_cls, method_name)
    except AttributeError:
        raise NotImplementedError("Class `{}` does not implement `{}`".format(my_cls.__class__.__name__, method_name))
    
    method(f1)


if __name__ == '__main__':
    main()
