Feature: time slider

  Scenario: slider moves forward 
     Given the app is running
      When the slider is dragged more than half way to the right
      Then the time will be later than 12:00