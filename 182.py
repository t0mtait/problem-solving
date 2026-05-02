import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    email_counts = person.groupby('email').size().reset_index(name='email_count')
    return email_counts[email_counts['email_count'] > 1][['email']]
data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

print(duplicate_emails(person))