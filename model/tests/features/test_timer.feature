Feature: unit testing timer

    Scenario: Start initializes timer state
        Given we have a timer
        When we start the timer
        Then the reset_timer flag should be False
        And the stopped flag should be False
        And the elapsed_time should be 0 seconds
        And the start_time should be at the current fake time
        And current_seconds should equal previous_seconds

    Scenario: Start does nothing when already running
        Given we have a timer
        And we start the timer
        And we wait for 2 seconds
        When we start the timer again
        Then the elapsed_time should be 2 seconds
        And the stopped flag should be False

    Scenario: Stop sets the stopped flag
        Given we have a timer
        And we start the timer
        And we wait for 3 seconds
        When we stop the timer
        Then the stopped flag should be True
        And the elapsed_time should be 3 seconds

    Scenario: Stop is idempotent
        Given we have a timer
        And we start the timer
        And we wait for 2 seconds
        And we stop the timer
        When we stop the timer again
        Then the stopped flag should be True
        And the elapsed_time should be 2 seconds

    Scenario: Resume after stop clears stopped flag
        Given we have a timer
        And we start the timer
        And we wait for 3 seconds
        And we stop the timer
        When we start the timer again
        Then the stopped flag should be False
        And the elapsed_time should be 3 seconds
        When we wait for 2 seconds
        Then the elapsed_time should be 5 seconds

    Scenario: Reset sets reset flag and restarts
        Given we have a timer
        And we start the timer
        And we wait for 4 seconds
        When we reset the timer
        Then the reset_timer flag should be False
        And the stopped flag should be False
        And the elapsed_time should be 0 seconds
        When we wait for 3 seconds
        Then the elapsed_time should be 3 seconds