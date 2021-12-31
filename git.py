import datetime
import os

x = datetime.datetime(2020, 5, 17)
def make_commit(days: int):
    if days < 1:
        return os.system('git push')
    else:
        dates = f'{days} 10 days ago'

        with open('data.txt', 'a') as file:
            file.write(f'{dates}\n')

        os.system('git add data.txt')

        os.system('git commit --date="'+dates+'" -m "First Commit"')

        return days*make_commit(days-10)

make_commit(10)