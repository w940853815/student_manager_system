// script.js
	//创建scotchApp模型
var scotchApp = angular.module('scotchApp', ['ngRoute']);

//路由配置
scotchApp.config(function($routeProvider) {
		$routeProvider
			.when('/myInfo', {
				templateUrl: 'pages/myinfo.html',
				controller: 'mainController'
			})
			.when('/myClass', {
				templateUrl: 'pages/myclass.html',
				controller: 'aboutController'
			})
			.when('/myMessage', {
				templateUrl: 'pages/myMessage.html',
				controller: 'contactController'
			})
			.otherwise({
				redirectTo:'/',
				templateUrl:'pages/personCenter.html'
			})
	})
	//创建mainController控制器
scotchApp.controller('mainController', function($scope) {

	// create a message to display in our view
	$scope.message = 'Everyone come and see how good I look!';
});

scotchApp.controller('aboutController', function($scope) {
	$scope.message = 'I am about page';
});

scotchApp.controller('contactController', function($scope) {
	$scope.message = 'I am contact page';
});
//面包屑导航更新
function breadcrumbF(){
	$(".breadcrumb li").remove()
	$(".breadcrumb").append('<li><a href="#!" class="">'+$(".list-group-item.active").parents('.panel-collapse').prev('.panel-heading').text().trim()+'</a></li>')
	$(".breadcrumb").append('<li class="active">'+$(".list-group-item.active>a").text()+'</li>')
}
function breadcrumbF2(obj){
	$(".breadcrumb li").remove()
	$(".breadcrumb").append('<li class="active">'+obj.text()+'</li>')
	
}
//退出按钮
$("#logout_btn").click(function(){
	if(confirm("是否退出当前账号?")){
		javascript:window.history.forward(1); 
		window.location.replace("index.html")
	}
	
})
$(function(){
	$(".panel-collapse").collapse({
		toggle:false
	})
	$(".panel-group li").each(function(i){
		$(this).click(function(){
			$(".list-group-item").removeClass('active')
			$(this).addClass('active')
			breadcrumbF()
		})
	})
	$(".panel-heading").click(function(){
			$(".list-group-item").removeClass('active')
			breadcrumbF2($(this))
	})
})
