		// Define the module for our AngularJS application.
		var app = angular.module( "myLogic", [] );
		
		app.controller("textController", function($scope){ 
			$scope.demo="Voici du text";
		});

httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };


function access(name){ 
	old= $("textarea").text();
    $("textarea").text(old+"\nNode "+name+" created");
}
