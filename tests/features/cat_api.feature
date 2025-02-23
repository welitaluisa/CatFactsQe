Feature: Validate Cat Breeds API

  Scenario: Validate API response without pagination
    Given I send a GET request to "/breeds"
    Then the response status should be 200
    And the response should contain "current_page" with value 1
    And the response should contain "per_page" with value 25
    And the last breed in the list should be "Chausie"

  Scenario: Validate API response for page 2
    Given I send a GET request to "/breeds?page=2"
    Then the response status should be 200
    And the response should contain "current_page" with value 2
    And the response should contain "per_page" with value 25
    And the last breed in the list should be "Kurilian Bobtail, or Kuril Islands Bobtail"

  Scenario: Validate API response for page 4
    Given I send a GET request to "/breeds?page=4"
    Then the response status should be 200
    And the response should contain "current_page" with value 4
    And the response should contain exactly 23 breeds
    And the last breed in the list should be "York Chocolate"
    And the list should start from item 76

  Scenario: Validate API response with limit 45 on page 1
    Given I send a GET request to "/breeds?page=1&limit=45"
    Then the response status should be 200
    And the response should contain "current_page" with value 1
    And the response should contain "per_page" with value 45
    And the last breed in the list should be "Karelian Bobtail"
    And the last page should be 3

  Scenario: Validate API response with limit 1
    Given I send a GET request to "/breeds?limit=1"
    Then the response status should be 200
    And the response should contain "per_page" with value 1

  Scenario: Validate API response for non-existent page
    Given I send a GET request to "/breeds?page=9999"
    Then the response status should be 200
    And the response should contain an empty list

  Scenario: Validate API response for negative limit
    Given I send a GET request to "/breeds?limit=-1"
    Then the response status should be 400
