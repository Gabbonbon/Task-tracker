import random
tasks = []
run_time = int(input("How many tasks do you have to complete?"))
for i in range(run_time):
    tasks_input = input(F"What is task {i+1} you have to do today?")
    tasks.append(tasks_input)
    print(tasks)
    priority = random.randint(1,run_time)
    tasks.append((tasks_input, priority))

    print("\nAll tasks with priorities:")
    for task in tasks:
            print(task)

print("The task you have to complete is: " + tasks[0])
