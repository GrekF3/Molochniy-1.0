import json

class Donuts:

    donuts = {
        'Розовые': 0,
        'Ванильные': 0,
        'Карамельные': 0,
        'Шоколадные': 0,
    }

    def StartNew(self):
        with open('items.json', 'r', encoding='utf-8') as file:
            donuts = json.load(file)
            all_donuts = []
            try:
                for values in donuts[0].values():
                    all_donuts.append(values)
            except:
                for values in donuts.values():
                    all_donuts.append(values)
            all_donuts = sum(all_donuts)

            return donuts, all_donuts

    def StartEnd(self, name, new_donuts):

        with open('items.json', 'r', encoding='utf-8') as file:
            donutsloader = json.load(file)

        self.donuts = donutsloader
        new_donuts = int(new_donuts)
        name = name
        donutsloader[name] = new_donuts + donutsloader[name]

        with open('items.json', 'w', encoding='utf-8') as file:
            json.dump(donutsloader, file, indent=4, ensure_ascii=False)

    def Info(self, donutscorner):
        donuts = []
        all_donuts = 'Всего пончиков: ' + str(sum(donutscorner[0].values()))

        for d, v in donutscorner[0].items():
            donuts.append((str(d) + ': ' + str(v)))

        msg = '\n'.join(donuts) + '\n' + all_donuts

        return msg

    def NewDonuts(self, new_donuts_boxes, name):
        NewDonuts = Donuts()
        new_donuts = int(new_donuts_boxes) * 36
        self.name = name
        NewDonuts.StartEnd(self.name, new_donuts)


    def MinusDonuts(self, count_donuts, name):
        with open('items.json', 'r', encoding='utf-8') as file:
            donutsloader = json.load(file)

        Minusdonuts = count_donuts
        self.name = name
        donutsloader[name] = donutsloader[name] - Minusdonuts

        with open('items.json', 'w', encoding='utf-8') as file:
            json.dump(donutsloader, file, indent=4, ensure_ascii=False)