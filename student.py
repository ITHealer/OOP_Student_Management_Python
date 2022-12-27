'''
class Student:
    // count = 0 // thuộc tính có sẵn vd1:
    // hàm init
    // các thuộc tính
    
    pass 
-> như này đã là 1 đối tượng.
sv = Student()
print(sv) // hiển thị vị trí của đối tượng được khởi tạo trong bộ nhớ.

----------------------------------------------------------------------
vd1: 
class Student:
    count = 0

    pass 

sv = Student()
print(sv.count) // hiển thị số lần đối tượng (class) Student được tạo.
----------------------------------------------------------------------

Giống như trong Java khi khởi tạo một đối tượng (tạo class) thì phải khởi tạo constructor
thì trong python đó là hàm init
class Student:
    count = 0

    def __init__(self , id , name):
        print('bắt đầu) //thì dòng này sẽ được in trước khi print(sv.count) được in. 
        // vì khi khởi tạo đối tượng sv thì nó thực hiện trong hàm init trước.
        self.id = None (KDL là rỗng) thuộc tính id
        //self tượng trưng cho đối tượng bạn đang khởi tạo

    pass 
sv = Student()
print(sv.count) 
'''

class Student:
    
    count = 0 # vd2: xem dưới

    def __init__(self , id , name):
        self.id = id
        self.name = name
        Student.count += 1

    # chỉ nhưng instance thể hiện của class mới được sd các thuộc tính của class vd: sv = Student(...)
    # sv là một instance (có thể hiểu self tương đương đt sv)
    # còn trong class Student thì thuộc tính của nó chỉ có count = 1 ở trên thôi. 
    # còn lại init hay set..get.. là các phương thức.

    # def set_id(self , id): // thay đổi giá trị hay là đặt một giá trị nào đó cho id. lấy giá trị truyền vào để thay
    #     self.id = id // self tương tự this trong java

    def get_id(self): # lấy giá trị của id ra.
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def show_info(self):
        print(f"\nThông tin Sinh Viên :  \n")
        print(f"Id :  { self.get_id() }")
        print(f"Tên Sinh Viên :  { self.name }")

'''

vd2:
sv = Student(...)
sv1 = Student(...)
print(sv1.count) // cta khởi tạo 2 lần đt nhưng count lại = 0 
// để nó tăng lên thì ta tăng count trong hàm init như trên. Student.count += 1.
// vì mỗi khi tạo đt thì nó đều phải gọi hàm init

'''