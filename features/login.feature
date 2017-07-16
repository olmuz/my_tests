Feature: Login
	
	Scenario: Login
		Given I am on 'Login' page
		When Fill text form
			| label         | value                    |  
			| Email Address | semensosnitski@gmail.com |  
			| Password      | abrakadabra              |  
		When click on button 'Login'
		Then Header 'My Dashboard' should be displayed
