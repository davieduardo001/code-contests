# imports
from fastapi import FastAPI

# problems
from contests.bee.bee_1002 import calculate_circle_area

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Welcome to the Code Contests API!'}

@app.get('/bee/1002')
def solve_problem_1002(radius: float):
    if radius < 0:
        return {'error': 'Radius must not be non-negative'}
    area = calculate_circle_area(radius)
    return {'radius': radius, 'area': f'{area:.4f}'}