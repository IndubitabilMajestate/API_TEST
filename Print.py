def prettifyData(data, size = 100):
    print("\n data:\n")
    for data_index in range(min(size,len(data))):
        for field in data[data_index]:
            print(f"\t-{field}:{data[data_index][field]}")
        print('='*40)
