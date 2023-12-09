bd_division_info = {}
bd_division_info['Barisal'] = {'district':6,'upazila':39,'union':333}
bd_division_info['chittagong'] = {'district':11,'upazila':97,'union':336}
bd_division_info['dhaka'] = {'district':13,'upazila':93,'union':1833}
bd_division_info['khulna'] = {'district':10,'upazila':59,'union':270}
bd_division_info['mymensingh'] = {'district':4,'upazila':34,'union':350}
bd_division_info['rajshahi'] = {'district':8,'upazila':70,'union':558}
bd_division_info['rangpur'] = {'district':8,'upazila':58,'union':536}
bd_division_info['sylhet'] = {'district':4,'upazila':38,'union':334}
print(bd_division_info)
print('......................')
devisions = bd_division_info.keys()
print(devisions)
print('...............................')
for dicision in devisions:
    print('Division',dicision)
print('..........................')
for division in devisions:
    print(division,'upazila',
          bd_division_info[division]['upazila'])
print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
for item in bd_division_info:
    print(item)
print('...........................')
for key in bd_division_info:
    print(key)
    print(bd_division_info[key])
print('.........................')
for key,value in bd_division_info.items():
    print(key)
    print(value)