from hem import generate_task
from hamming.models import Task


for i in range(5):
    a, b = generate_task(2)
    Task.objects.create(text=b, answer=a, level=2)
for i in range(5):
    a, b = generate_task(3)
    Task.objects.create(text=b, answer=a, level=3)
for i in range(5):
    a, b = generate_task(5)
    Task.objects.create(text=b, answer=a, level=5)
print(Task.objects.all())