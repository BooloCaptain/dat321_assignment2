Feature: Turning on and off light

    Scenario: Turn on the light
        Given the bedroom light is off
        When the demo model detects that the bedroom light should be turned on
        Then the bedroom light should be turned on in the demo view

    Scenario: Turn off the light
        Given the bedroom light is on
        When the demo model detects that the bedroom light should be turned off
        Then the bedroom light should be turned off in the demo view

    Scenario: Turn on the light in one room and off in another
        Given the bedroom light is off
        And the kitchen light is on
        When the demo model detects that the bedroom light should be turned on
        And the demo model detects that the kitchen light should be turned off
        Then the bedroom light should be turned on in the demo view
        And the kitchen light should be turned off in the demo view

    Scenario: Turn on a light that is already on
        Given the bedroom light is on
        When the demo model detects that the bedroom light should be turned on
        Then the bedroom light should be turned on in the demo view

    Scenario: Turn off a light that is already off
        Given the kitchen light is off
        When the demo model detects that the kitchen light should be turned off
        Then the kitchen light should be turned off in the demo view

    Scenario: Toggle a non existent room
        Given the bedroom light is off
        When the demo model detects that the attic light should be turned on
        Then the bedroom light should be turned off in the demo view

    Scenario: No action taken after initial state
        Given the kitchen light is on
        Then the kitchen light should be turned on in the demo view