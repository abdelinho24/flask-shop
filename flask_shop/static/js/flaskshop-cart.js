angular.module('flaskshopApp', [])
   	 .controller('CartController', ['$scope', function($scope) {
   		 $scope.cart = [];
     
	    $scope.addItem = function() {
	   		$scope.cart.push(
	   			{title:$scope.title, description:$scope.description, price:$scope.price, quantity:$scope.quantity}
	   		);
	    };

	    $scope.removeItem = function(index) {
	   		$scope.cart.splice(index, 1);
	    };
	     
	    $scope.getTotalPrice = function(){
		    var total = 0;
		    for(var i = 0; i < $scope.cart.length; i++){
		        var product = $scope.cart[i];
		        total += (product.price * product.quantity);
		    }
		    return total;
		}
    }]);