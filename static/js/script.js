// script.js
	//创建scotchApp模型
document.write("<script src='../flask_util.js'></script>");
var scotchApp = angular.module('scotchApp', ['ngRoute']);

//路由配置
scotchApp.config(function($routeProvider) {
		$routeProvider
			//个人信息
			// .when('/myInfo',{
			// 	templateUrl:flask_util.url_for('static',filename='pages/myinfo.html'),
			// 	controller: 'myinfoController'
			// })
			.when('/myInfo',{
				templateUrl:'static/pages/myinfo.html',
				controller: 'myinfoController'
			})
			//我的班级
			.when('/myClass',{
				templateUrl: 'static/pages/myclass.html',
				controller: 'myclassController'
			})
			//我的通知
			.when('/myinform',{
				templateUrl: 'static/pages/myinform.html',
				controller: 'myinformController'
			})
			//课程表
			.when('/syllabus',{
				templateUrl: 'static/pages/syllabus.html',
				controller: 'syllabusController'
			})
			//收件箱
			.when('/Inbox',{
				templateUrl: 'static/pages/Inbox.html',
				controller: 'InboxController'
			})
//			.when('/Inbox_look',{
//				templateUrl: 'pages/Inbox_look.html',
//				controller: 'Inbox_lookController'
//			})
			//写信
			.when('/Inbox_write',{
				templateUrl: 'static/pages/Inbox_write.html',
				controller: 'Inbox_writeController'	
			})
			.when('/examination',{
			//我的报考
				templateUrl: 'static/pages/examination.html',
				controller: 'examinationController'	
			})
			//我的成绩
			.when('/grade',{
				templateUrl: 'static/pages/grade.html',
				controller: 'gradeController'	
			})
			//我的书籍
			.when('/books',{
				templateUrl: 'static/pages/books.html',
				controller: 'booksController'	
			})
			//财务中心
			.when('/finance',{
				templateUrl: 'static/pages/finance.html',
				controller: 'financeController'	
			})
			//密码修改
			.when('/setpass',{
				templateUrl: 'static/pages/setpass.html',
				controller: 'setpassController'	
			})
			//默认-中心
			.otherwise({
				redirectTo:'/',
				templateUrl:'static/pages/personCenter.html'
			})
	})
	//创建mainController控制器
scotchApp.controller('mainController', function($scope,$http) {
	$scope.yzm="static/img/yzm.png"
	// create a message to display in our view
	$scope.message = 'Everyone come and see how good I look!';
	
	$scope.newTel='1';
	
	
//	myUrl='http://115.159.208.223/json.json?callback=angular.callbacks._0';
//	myUrl='http://115.159.208.223/json.json?callback=JSON_CALLBACK';
	myUrl='http://127.0.0.1:5000/json?callback=JSON_CALLBACK';
//	myUrl='http://123.207.139.130/json?callback=angular.callbacks._0';
//	myUrl='https://public-api.wordpress.com/rest/v1/sites/wtmpeachtest.wordpress.com/posts?callback=JSON_CALLBACK';

	//Add the following immediately before making a jsonp request.
//	var c = $window.angular.callbacks.counter.toString(36);
//	
//	$window['angularcallbacks_' + c] = function (data) {
//	    $window.angular.callbacks['_' + c](data);
//	    delete $window['angularcallbacks_' + c];
//	};
		$http.jsonp(myUrl)
		.success(
		　　function(data, status, headers, config){
				$scope.student = data.meta;
				$scope.messages = data.messages;
				$scope.informs = data.informs;
		　　　　console.log(data);
		　　　　console.log(status);
		　　}
		)
		.error(
			function(data, status, headers, config){
				console.log('error');
		　　　	console.log(status);
				
			}
		);
		
	//确认更改电话
	$scope.confirmNewtel=function(){
		var newTel=$("#newContact").val();
		var url="http://www.baidu.com";
		if(confirm('确认更改联系方式?')){
			if(newTel==''){
				alert('新的联系方式不能为空哦')
				return
			}
			$.post(url,newTel,function(data){
				if(data.msg==1){
					alert('修改成功!')
				}
				else{
					alert('参数错误')
				}
			},'json')

		}
	}
	//全选
	$scope.selectAll=function(){
		$(".inform-item-chexbox").each(function(){
		if($(this).hasClass('active')){
			$(".inform-item-select").removeClass('active')
			$(".inform-item-chexbox").each(function(){
				$(this).removeClass('active')
			})
		}else{
			$(".inform-item-select").addClass('active')
			$(".inform-item-chexbox").each(function(){
				$(this).addClass("active")
			})
		}
	})
	}
//	$scope.stduent={
//		"stu_name":'高慧鹏',//姓名
//		"stu_cardID":'142401199501284219',//身份证
//		"stu_sex":'男',//性别
//		"stu_NO":'132055110',
//		"stu_start_date":'2013',
//		"stu_record":'本科',
//		"stu_birthday":'1995-01-28',//出生日期
//		"stu_nation":'汉族',//民族
//		"stu_zzmm":'团员',//政治面貌
//		"stu_adress":'山西省晋中市榆次区乌金山镇',//联系地址
//		"stu_qq":'573941623',//qq
//		"stu_email":'573941623@qq.com',//电子邮箱
//		"stu_yzbm":'030600',//邮政编码
//		"stu_ksh":'0310612654',//考生号
//		"stu_rxsj":'2013-9',//入学时间
//		"stu_rxfs":'普通入学',//入学方式
//		"stu_xxxs":'普通全日制',//学习形式
//		"stu_pylx":'普通本科生',//培养类型
//		"stu_pydx":'统招',//培养对象
//		"stu_pycc":'本科',//培养层次
//		"stu_bxlx":'普通高等教育',//办学类型
//		"stu_bxxx":'国家任务',//办学形式
//		"stu_img":'img/default_user_logo.png',//照片
//		"stu_tel":'18835179550',//联系方式
//		"stu_dept":'计算机工程系',//系部
//		"stu_profession":'网络工程',//专业
//		"stu_class":'132055110',//班级
//		"stu_start_date":'2013',//入学年份
//		"stu_native":"中国",//籍贯
//	}
	
});

scotchApp.controller('myinfoController', function($scope) {
	$scope.message = 'I am about page';
});

scotchApp.controller('myclassController', function($scope) {
	$scope.message = 'I am contact page';
});
scotchApp.controller('myinformController', function($scope) {
});
scotchApp.controller('syllabusController', function($scope) {
});
scotchApp.controller('InboxController', function($scope) {
});
scotchApp.controller('Inbox_writeController', function($scope) {
});
scotchApp.controller('examinationController', function($scope) {
});
scotchApp.controller('gradeController', function($scope) {
});
scotchApp.controller('booksController', function($scope) {
});
scotchApp.controller('financeController', function($scope) {
});
scotchApp.controller('setpassController', function($scope) {
});


//面包屑导航更新
function breadcrumbF(){
	$("body,html").animate({
		scrollTop:0
	},500)
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
//测试
function test(){
	alert('test')
}
$(function(){
	$(".panel-collapse").collapse({
		toggle:false
	})
	//左侧项目点击
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
