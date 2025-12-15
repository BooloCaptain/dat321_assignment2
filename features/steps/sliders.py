from datetime import datetime
from behave import *

from App import Application
from model.algorithm.nn_model.nn_alg import NNAlg
from model.demo_model import DemoModel
from model.timer import Timer

@given('the app is running')
def step_impl(context):
    start_time = datetime.now().replace(hour=0,minute=0,second=0)
    timer = Timer()
    scheduler = NNAlg()
    model = DemoModel(scheduler, timer, start_time)
    context.app = Application(model, start_time)

@when('the slider is dragged more than half way to the right')
def step_impl(context):
    context.app.slider._slider.set(721)  # simulate dragging the slider 
    context.app.slider.set_time(None)    # trigger the time update
      

@then('the time will be later than 12:00')
def step_impl(context):
    time = context.app.model.get_time()
    assert time.hour >= 12 and time.minute > 0