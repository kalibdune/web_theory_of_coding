from hem import generate_task
from hamming.models import Task

print(Task)
s = 0
while s != 5:
    a, b = generate_task(2)
    if a != 0:
        s+=1
        print(b, a, (a-1)//2)
        Task.objects.create(text=b, answer=(a-1)//2, level=2)
s = 0

while s != 5:
    a, b = generate_task(5)
    if a != 0:
        s+=1
        print(b, a, (a-1)//2)
        Task.objects.create(text=b, answer=(a-1)//2, level=3)

s = 0

while s != 5:
    a, b = generate_task(6)
    if a != 0:
        s+=1
        print(b, a, (a-1)//2)
        Task.objects.create(text=b, answer=(a-1)//2, level=5)
print(Task.objects.all())