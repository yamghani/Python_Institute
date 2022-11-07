import csv
import pandas as pd
import pprint

class UnderTest:
    def __init__(self,
                 attack1_metric1, attack1_metric2,
                 attack2_metric1, attack2_metric2,
                 attack3_metric1,
                 attack4_metric1, attack4_metric2):
        self.attack1_metric1 = attack1_metric1
        self.attack1_metric2 = attack1_metric2
        self.attack2_metric1 = attack2_metric1
        self.attack2_metric2 = attack2_metric2
        self.attack3_metric1 = attack3_metric1
        self.attack4_metric1 = attack4_metric1
        self.attack4_metric2 = attack4_metric2
        
    def attack(self):
        result = []
        max_items = 101
        data = [(x1, x2, x3, x4)
                for x1 in range(1, max_items)
                for x2 in range(1, max_items)
                for x3 in range(1, max_items)
                for x4 in range(1, max_items)]
        item_counter = 0
        for row in data:
            item_counter += 1
            print("item number is : {}", item_counter)
            # data_dict = {"throughput": "", "cpu": "", "ram": "", "cc": "", "status": "GREEN"}
            data_dict = {'throughput': row[0], 'cpu': row[1], 'ram': row[2], 'cc': row[3], "status": "GREEN"}
            # condition-1
            condition_1 = row[3] - row[0]
            if row[3] >= self.attack1_metric1 and condition_1 >= self.attack1_metric2:
                data_dict['status'] = 'RED'
            # condition-2
            if self.attack2_metric1 <= row[0] <= self.attack2_metric2 or \
                    self.attack2_metric1 <= row[1] <= self.attack2_metric2 or \
                    self.attack2_metric1 <= row[2] <= self.attack2_metric2 or \
                    self.attack2_metric1 <= row[3] <= self.attack2_metric2:
                if data_dict['status'] != 'RED':
                    data_dict['status'] = 'YELLOW'
            # condition-3
            if row[0] > self.attack3_metric1 or \
                    row[1] > self.attack3_metric1 or \
                    row[2] > self.attack3_metric1 or \
                    row[3] > self.attack3_metric1:
                data_dict['status'] = 'RED'
            # condition-4
            condition_3 = row[0] - row[3]
            if row[0] >= self.attack4_metric1 and condition_3 <= self.attack4_metric2:
                data_dict['status'] = 'RED'
            result.append(data_dict)
        return result

   
dummyData = UnderTest(30, 30, 60, 75, 75, 50, 40)
result = dummyData.attack()
# pprint(result)

fields = ['cc', 'cpu', 'ram', 'status', 'throughput']
with open('training_data.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)

    write.writerow(fields)
    # write.writerows(rows)

df = pd.DataFrame(result)

# saving the dataframe
df.to_csv('training_data.csv')
