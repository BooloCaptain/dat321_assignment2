from behave import *
import datetime as dt

@given('we have a timer')
def step_impl(context):
    # Use an injected fake clock instead of patching globals
    context.fake_time = 1_700_000_000  # arbitrary fixed epoch seconds

    def fake_time():
        return context.fake_time

    class FrozenDateTime(dt.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls.fromtimestamp(context.fake_time, tz)

    from model.timer import Timer
    context.timer = Timer(time_fn=fake_time, datetime_cls=FrozenDateTime)

@given('we start the timer')
def step_impl(context):
    context.timer.start()

@given('we wait for {seconds:d} seconds')
def step_impl(context, seconds):
    context.fake_time += seconds
    # Trigger internal timer update by calling a method
    context.timer.get_time()

@given('we stop the timer')
def step_impl(context):
    context.timer.stop()

@when('we start the timer')
def step_impl(context):
    context.timer.start()

@when('we start the timer again')
def step_impl(context):
    context.timer.start()

@when('we wait for {seconds:d} seconds')
def step_impl(context, seconds):
    # Advance the fake clock instead of real sleeping
    context.fake_time += seconds
    # Trigger internal timer update by calling a method
    context.timer.get_time()

@when('we stop the timer')
def step_impl(context):
    context.timer.stop()

@when('we stop the timer again')
def step_impl(context):
    context.timer.stop()

@when('we reset the timer')
def step_impl(context):
    context.timer.reset()

@then('the reset_timer flag should be {expected}')
def step_impl(context, expected):
    expected_bool = expected == "True"
    assert context.timer.reset_timer == expected_bool, (
        f"Expected reset_timer={expected_bool}, got {context.timer.reset_timer}"
    )

@then('the stopped flag should be {expected}')
def step_impl(context, expected):
    expected_bool = expected == "True"
    assert context.timer.stopped == expected_bool, (
        f"Expected stopped={expected_bool}, got {context.timer.stopped}"
    )

@then('the elapsed_time should be {seconds:d} seconds')
def step_impl(context, seconds):
    actual = context.timer.elapsed_time.total_seconds()
    assert abs(actual - seconds) < 0.1, (
        f"Expected elapsed_time={seconds}s, got {actual}s"
    )

@then('the start_time should be at the current fake time')
def step_impl(context):
    expected_ts = context.fake_time
    actual_ts = context.timer.start_time.timestamp()
    assert abs(actual_ts - expected_ts) < 1e-3, (
        f"Expected start_time around {expected_ts}, got {actual_ts}"
    )

@then('current_seconds should equal previous_seconds')
def step_impl(context):
    assert context.timer.current_seconds == context.timer.previous_seconds, (
        f"Expected current_seconds == previous_seconds, got {context.timer.current_seconds} != {context.timer.previous_seconds}"
    )
