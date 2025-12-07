import json
import os
from print_result  import print_result
from cm_timer import cm_timer_1
from gen_random import gen_random
from unique import Unique

path = os.path.join(os.path.dirname(__file__), "data_light.json")

with open(path) as f:
    data = json.load(f)

@print_result
def f1(vacancies):
    jobs = [vacancy["job-name"] for vacancy in vacancies]
    return sorted(Unique(jobs, case_sensitive=False))

@print_result
def f2(jobs):
    return list(filter(lambda job: isinstance(job, str) and job.lower().startswith("программист"), jobs))

@print_result
def f3(jobs):
    return list(map(lambda job: job + " с опытом Python", jobs))

@print_result
def f4(jobs):
    salaries = gen_random(len(jobs), 100_000, 200_000)
    result = []
    for job, salary in zip(jobs, salaries):
        result.append(f"{job}, зарплата {salary} руб.")
    return result

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))