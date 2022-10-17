from settings.create import create_celery
import code

Task = create_celery()

t_add = Task('tasks.add')

s_add = t_add.s().set(queue='ones')

print(t_add.delay(1,2).get())
print(t_add.delay(1,2).get())
print(t_add.delay(1,2).get())
print(t_add.delay(1,2).get())
print(t_add.delay(1,2).get())