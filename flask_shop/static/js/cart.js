$(function() {

var html = [].slice.call(document.querySelectorAll('.thumbnail'));
			
			html.map(function (node, index) {
				node.querySelector('form').setAttribute('ng-submit', 'addItem(' + index + ')');
			});

			var shop = angular.module('shopApp', []);
	   	 	shop.controller('CartController', ['$scope', function($scope) {
	   		 $scope.cart = [];
	   		 
	   		 $scope.store = html.map(function (node, index) {
	   		 	var dataset = {};
	   		 	dataset.title = node.querySelector('.item_name').innerHTML;
	   		 	dataset.description = node.querySelector('.item_description').innerHTML;
	   		 	dataset.quantity = node.querySelector('.item_Quantity');
	   		 	dataset.price = node.querySelector('.item_price').innerHTML;
	   		 	return dataset;
	   		 });
	     
		    $scope.addItem = function(id) {
		    	var item = $scope.store[+id];
		    	
		   		$scope.cart.push(
		   			{
		   				title: item.title, 
		   				description: item.description, 
		   				price: item.price, 
		   				quantity: item.quantity.value || 1
		   			}
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

});