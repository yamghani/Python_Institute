import pprint


class UnderTest:
    throughput = []
    cc = []
    cpu = []
    ram = []
    for i in range(1, 101):
        throughput.append(i)
    for i in range(1, 101):
        cc.append(i)
    for i in range(1, 101):
        cpu.append(i)
    for i in range(1, 101):
        ram.append(i)
    data = [(x1, x2, x3, x4)
            for x1 in throughput
            for x2 in cpu
            for x3 in ram
            for x4 in cc]

    def __init__(self, attack1_metric1, attack1_metric2, attack2_metric1,
                 attack2_metric2, attack3_metric1, attack4_metric1, attack4_metric2):
        self.attack1_metric1 = attack1_metric1
        self.attack1_metric2 = attack1_metric2
        self.attack2_metric1 = attack2_metric1
        self.attack2_metric2 = attack2_metric2
        self.attack3_metric1 = attack3_metric1
        self.attack4_metric1 = attack4_metric1
        self.attack4_metric2 = attack4_metric2
        
    def attack1(self):
        result = []
        # i = 1
        for row in self.data:
            data_dict = {'throughput': row[0], 'cpu': row[1], 'ram': row[2], 'cc': row[3], "status": "GREEN"}
            # condition-1
            condition_1 = row[3] - row[0]
            if int(row[3]) >= self.attack1_metric1 and condition_1 >= self.attack1_metric2:
                data_dict['status'] = 'RED'
            result.append(data_dict)
        return result
    
    def attack2(self):
        result = []
        for row in self.data:
            data_dict = {'throughput': row[0], 'cpu': row[1], 'ram': row[2], 'cc': row[3], "status": "GREEN"}
            # condition-2
            if (row[0] >= self.attack2_metric1 or row[0] <= self.attack2_metric2) or \
                    (row[1] >= self.attack2_metric1 or row[1] <= self.attack2_metric2) or \
                    (row[2] >= self.attack2_metric1 or row[2] <= self.attack2_metric2) or \
                    (row[3] >= self.attack2_metric1 or row[3] <= self.attack2_metric2):
                data_dict['status'] = 'YELLOW'
            result.append(data_dict)
        return result
    
    def attack3(self):
        result = []
        for row in self.data:
            data_dict = {'throughput': row[0], 'cpu': row[1], 'ram': row[2], 'cc': row[3], "status": "GREEN"}
            # condition-3
            if row[0] > self.attack3_metric1 or \
                    row[1] > self.attack3_metric1 or \
                    row[2] > self.attack3_metric1 or \
                    row[3] > self.attack3_metric1:
                data_dict['status'] = 'RED'
            result.append(data_dict)
        return result
    
    def attack4(self):
        result = []
        for row in self.data:
            data_dict = {'throughput': row[0], 'cpu': row[1], 'ram': row[2], 'cc': row[3], "status": "GREEN"}
            # # condition-4
            condition_3 = row[0] - row[3]
            if row[0] >= self.attack4_metric1 and condition_3 <= self.attack4_metric2:
                data_dict['status'] = 'RED'
            result.append(data_dict)
        return result


dummyData = UnderTest(30, 30, 60, 75, 75, 50, 40)
pprint.pprint(dummyData.attack1())
pprint.pprint(dummyData.attack2())
pprint.pprint(dummyData.attack3())
pprint.pprint(dummyData.attack4())
