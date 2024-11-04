studentA = {'name':'Eva',
           'address':'monteal',
           'phone':5148765466,
           'level':'masters1',
           }
studentA = {'name':'Daniel',
           'address':'Papineuve',
           'phone':5134534466,
           'level':'masters2',
           }
print(studentA.pop('height', None))
#print(studentA['name'])
print(studentA.pop('name', None))
print(studentA)
studentA['name']='Miguel'
print(studentA)
# for each in studentA:
#     print(f'{each} -->>  {studentA[each]}')

school={'courses':{'masters1':{'students':[studentA, ],
                               'subjects':['python', 'animation',]},
                   'masters2':{'students':[studentA, ]},},
        'teachers':{'danielRuiz':{ 'name':'Daniel',
                                   'lastName':'ruiz',
                                   'address':'monteal',
                                   'phone':5148765466
                                   },
                    'juan':{}},
        'classrooms':{}
        }


