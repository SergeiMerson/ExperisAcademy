with open(r'd:\Projects\ExperisAcademy\Exercises\Try-Except\ex25-swallow-speeds.txt', 'r') as swallow_data:
    data = []
    for line in swallow_data:
        try:
            data.append(float(line.strip()))
        except ValueError:
            print(f'{line} is not a valid data point')

    print(f'Average swallow speed is {sum(data)/len(data):.3f}')