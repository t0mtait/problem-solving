import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.rename(columns={'id': 'employeeId', 'name': 'Employee', 'salary': 'Salary'})
    ans = employee.merge(department, left_on='departmentId', right_on='id', how='inner')
    ans = ans[ans['Salary'] == ans.groupby('departmentId')['Salary'].transform('max')].reset_index(drop=True)
    ans.drop(columns=['departmentId', 'employeeId', 'id'], inplace=True)
    ans.rename(columns={'name': 'Department'}, inplace=True)
    return ans


data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
print(department_highest_salary(employee, department))