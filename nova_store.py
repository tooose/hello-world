class Employee:
    """
    Klasa za vraboteni.
    """
    def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=int):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary
        


class Company:
    employee_list = []
    odmori = []
    def __init__(self, name: str, company_id: int, address=None):

        self.name = name
        self.company_id = company_id
        self.address = address
    
    def hire(self, employee:Employee, position:str, salary:int):
        
        print(f'{self.name} go vrabotuva {employee.first_name}')

        employee.position = position
        employee.salary = salary
        self.employee_list.append(employee)

    def average_salary(self):
        num_employee = len(self.employee_list)
        tot_pay = 0
        for employee in self.employee_list:
            tot_pay += employee.salary
        average_pay = tot_pay / num_employee
        return average_pay
    
    def day_off(self, employee:Employee, type_off: str, days : int):
        postoe = False
        for emploiter in self.employee_list:
            if employee.email == emploiter.email:
                self.odmori.append([employee, type_off, days])
                print(self.odmori)
            

           
    

semos_mk = Company("Semos Makedonija", 1234)

vraboten = Employee("Tose", "Davitkov", "ime1@ime1.com", "developer", "semos_mk")

# print(ime1.position, ime1.salary)
# semos_mk.hire(ime1, 'support', 10000000)
# print(ime1.position, ime1.salary)

# Instanci od klasata kompanii
neptun = Company('Neptun', 123, 'Mepso br2' )
posta = Company( 'Makedonski Posti', 321, 'makedonija br3' )

# Instanca od klasata Employe
rab1 = Employee('pero', 'perev','mocam@pod.terasa', 'shef', 'Sofra', 120000)
rab2 = Employee('risto', 'ristov','pristo@risov.com', 'prodavac', 'setek', 30000)
rab3 = Employee('toshe', 'toshev','medika@va.com', 'postar', 'Promedika', 42000)

neptun.hire(rab1, 'rabotnik', 40000)
neptun.hire(rab2, 'rabotnik', 40000)
posta.hire(rab3, 'rabotnik', 40000)

neptun.day_off(rab3, 'annual', 20)