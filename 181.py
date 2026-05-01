import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    emp = employee.rename(columns={'id': 'emp_id', 'salary': 'emp_salary'})
    mgr = employee.drop(columns=['managerId']);
    mgr.rename(columns={'id': 'managerId' , 'salary': 'mgr_salary'}, inplace=True)
    ans = emp.merge(mgr,how='inner',on='managerId')
    ans = ans[ans['emp_salary'] > ans['mgr_salary']]
    ans.drop(columns=['emp_id', 'emp_salary', 'managerId', 'name_y', 'mgr_salary'], inplace = True)
    ans.rename(columns={'name_x': 'Employee'}, inplace = True)
    return ans




data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})

print (find_employees(employee))