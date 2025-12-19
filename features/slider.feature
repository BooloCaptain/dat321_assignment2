Feature: time slider

  Scenario: slider moves forward 
     Given the app is running
      When the slider is dragged more than half way to the right
      Then the time will be later than 12:00

  Scenario: slider is moved all the way left
     Given the app is running
      When the slider is dragged all the way left
      Then the time will be 00:00

  Scenario: slider is moved all the way right
     Given the app is running
      When the slider is dragged all the way right
      Then the time will be 23:59