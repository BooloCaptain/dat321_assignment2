
from typing import List
from behave import given, when, then
from model.abstract_timer import ATimer
from model.algorithm.abstract_mimicking_algorithm import MimickingAlgorithm
from model.demo_model import DemoModel
from model.events.lamp_action import LampAction
from datetime import datetime
from unittest.mock import Mock
from model.abstract_event_observer import EventObserver
from model.events.lamp_event import LampEvent
from model.schedule import Schedule

class FakeScheduler(MimickingAlgorithm):
    def __init__(self) -> None:
        pass

    def createSchedule(self, user_actions: List[LampEvent]) -> Schedule:
        pass


class FakeTimer(ATimer):

    def __init__(self) -> None:
        pass

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def reset(self) -> None:
        pass

    def get_time(self) -> datetime:
        pass

    def set_time(self, new_time: datetime) -> None:  
        pass
        

# Mocked AptLayout for headless testing (no graphics)
class MockAptLayout(EventObserver):
    def __init__(self, model):
        self.model = model
        self.room_states = {
            "bedroom": False,
            "livingroom": False,
            "kitchen": False,
            "bathroom": False,
            "hall": False
        }
    def notify(self, event):
        # event.action is a LampAction
        if event.lamp in self.room_states:
            if event.action.value == "on":
                self.room_states[event.lamp] = True
            elif event.action.value == "off":
                self.room_states[event.lamp] = False


# Only set up model and view once per scenario
def setup_model_and_view(context):
    if not hasattr(context, 'model'):
        scheduler = FakeScheduler()
        timer = FakeTimer()
        start_time = datetime.now()
        context.model = DemoModel(scheduler, timer, start_time)
        context.view = Mock()  # Not used, but placeholder if needed
        context.apt_layout = MockAptLayout(context.model)
        context.model.add_observer(context.apt_layout)


@given('the {room} light is off')
def step_given_light_is_off(context, room):
    setup_model_and_view(context)
    context.apt_layout.room_states[room] = False

@given('the {room} light is on')
def step_given_light_is_on(context, room):
    setup_model_and_view(context)
    context.apt_layout.room_states[room] = True


@when('the demo model detects that the {room} light should be turned on')
def step_when_model_detects_light_on(context, room):
    event = LampEvent(datetime.now(), room, LampAction.ON)
    context.model.publish(event)

@when('the demo model detects that the {room} light should be turned off')
def step_when_model_detects_light_off(context, room):
    event = LampEvent(datetime.now(), room, LampAction.OFF)
    context.model.publish(event)


@then('the {room} light should be turned on in the demo view')
def step_then_light_on_in_view(context, room):
    assert context.apt_layout.room_states[room] is True, f'{room.capitalize()} light should be ON in the view.'

@then('the {room} light should be turned off in the demo view')
def step_then_light_off_in_view(context, room):
    assert context.apt_layout.room_states[room] is False, f'{room.capitalize()} light should be OFF in the view.'
