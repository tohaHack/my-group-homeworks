import random
import copy
sample_dict = {'class-_a':{
                'student':{
                    'name':'Misha',
                    'marks':{
                       'math':90,
                       'history':85
                    }
                }
            }
        }
print(sample_dict['class-_a']['student']['name'])
print(sample_dict['class-_a']['student']['marks']['history'])
sample_dict['class-_a']['new_student'] = {'name': 'Vova', 'marks':{
    'math':100, 'history':95
}}
sample_dict['class_b'] = copy.deepcopy(sample_dict['class-_a'])
line = 'Igor', 'Anton'
v = []
v_a = []
for elem in sample_dict['class_b']:
    sample_dict['class_b'][elem]['marks'].update({'physics': 70})
    sample_dict['class_b'][elem]['name'] = random.choice(line)
    v.append(list(i for i in sample_dict['class_b'][elem]['marks'].values()))
print(sample_dict['class_b'])
for elem_a in sample_dict['class-_a']:
    v_a.append(list(i for i in sample_dict['class-_a'][elem_a]['marks'].values()))
print(sample_dict['class-_a'])
print(v, v_a)
s = [13,44]
f_sum = round(sum(v[0])/len(v[0]), 2)
print(f_sum)
s_sum = round(sum(v[1])/len(v[1]), 2)
print(s_sum)
sum_all_students = {'student_1': f_sum, 'student_2': s_sum}
<<<<<<< HEAD
best_student = list(sum_all_students.keys())[list(sum_all_students.values()).index(max(sum_all_students.values()))]
=======
best_student = max(sum_all_students.values())
>>>>>>> 1175f9a96c95af86b9a48fbe91027193470b5f68
print(best_student)
new_v = v[0]+(v[1])
sum_all_students_in_all_class = round(sum(new_v)/len(new_v), 2)
print(sum_all_students_in_all_class)
new_v_a = v_a[0]+v_a[1]
sum_all_students_in_all_class_a = round(sum(new_v_a)/len(new_v_a), 2)
print(sum_all_students_in_all_class_a)
class_sum = {'class_a': sum_all_students_in_all_class_a, 'class_b': sum_all_students_in_all_class}
<<<<<<< HEAD
value = list(class_sum.values())
key = list(class_sum.keys())
best = key[value.index(max(class_sum.values()))]
=======
best = max(class_sum.values())
>>>>>>> 1175f9a96c95af86b9a48fbe91027193470b5f68
print(best)
