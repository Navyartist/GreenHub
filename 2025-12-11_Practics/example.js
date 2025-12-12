$(function(){
	// var prizeBox = $('.prizeBox').bxSlider({
	// 	mode: "vertical",
	// 	auto: true,
	// 	pager:false,
	// 	controls:false,
	// 	autoControls:false,
	// 	slideMargin: 20,
	// 	slideWidth: 450,
	// 	onSliderLoad: function(){ $(".prizeBox").css("visibility", "visible").animate({opacity:1}); }
	// });
	var prizeBox_hTop = $('.prizeBox_hTop').bxSlider({
		mode: "vertical",
		auto: true,
		pager:false,
		controls:false,
		autoControls:false,
		slideMargin: 20,
		slideWidth: 450,
		onSliderLoad: function(){ $(".prizeBox_hTop_wrap").css("visibility", "visible").animate({opacity:1}); }
	});

	var prizeBox_hLeft = $('.prizeBox_hLeft').bxSlider({
		mode: "vertical",
		auto: true,
		pager:false,
		controls:false,
		autoControls:false,
		slideMargin: 20,
		slideWidth: 450,
		onSliderLoad: function(){ $(".prizeBox_hLeft_wrap").css("visibility", "visible").animate({opacity:1}); }
	});


	$('.mobMenuBtn').on('click', function(){ // 모바일 메뉴
	if(	!$('.subBox').hasClass('onMenu')){
			$('.subBox').addClass('onMenu');
			$(this).addClass('mobMenuBtn_on');
			$('html, body').css({'height': '100%'});
		}else{
			$('.subBox').removeClass('onMenu');
			$(this).removeClass('mobMenuBtn_on');
			$('html, body').css({'height': 'auto'});
		}
	});
	$('.campus > h4').on('click', function(){ //모바일 캠퍼스 열기
		var campus = $(this).siblings('div');
		var winH = $(window).height();
		var campusBox = $('.campus > div');
		if(campus.css('display') == 'none'){
			if(campusBox.height() > winH){
				campusBox.css({'height': winH});
			}else{
				campusBox.css({'height': 'auto'});
				$('.whole').on('scroll touchmove mousewheel', function(event) {
					event.preventDefault();
					event.stopPropagation();
					return false;
				});
			}
			// campus.css('display', 'block');
			campus.slideDown(200);
			//$(this).children('span').addClass('loc');
			$('.mobMenuBtn').removeClass('mobMenuBtn_on');
			$('.subBox').removeClass('onMenu');
		}else{
			campus.slideUp(200);
			// campus.css('height', '0');
			//$(this).children('span').removeClass('loc');
		}
	});

	$('.campusClose').on('click', function(){ //모바일 캠퍼스 닫기
		var campus = $('.campus > div');
		if(campus.css('display') == 'none'){
			// campus.css('display', 'block');
			campus.slideDown(200);
			// $(this).children('span').addClass('loc');
			$('.mobMenuBtn').removeClass('mobMenuBtn_on');
			$('.subBox').removeClass('onMenu');
		}else{
			campus.slideUp(200);
			$('.campus > div').height('auto');
			$('html, body').css({'height': 'auto'});
			$('.whole').off('scroll touchmove mousewheel');
			// campus.css('height', '0');
			// $(this).children('span').removeClass('loc');
		}
	});

	var ww = $(window).width();
	var wh = $(window).height();
	if(ww < 1080){
		$('.subBox').height(wh - $('.header').height());
		/*$('.menuLi > h3').addClass('mobMenu');*/
		$('.ncsMenu > h5').addClass('mobOn');
	}else{
		/*$('.menuLi > h3').removeClass('mobMenu');*/
		$('.ncsMenu > h5').removeClass('mobOn');
	}

	$(window).resize(function(){
		var ww = $(window).width();
		var wh = $(window).height();
		if(ww < 1080){
			$('.subBox').height(wh - $('.header').height());
			if(!$('.menuLi > h3').hasClass('mobMenu')){
					/*$('.menuLi > h3').addClass('mobMenu');*/
					$('.ncsMenu > h5').addClass('mobOn');
			}
			/*mobMenu();*/
		}else{
			/*$('.menuLi > h3').removeClass('mobMenu');*/
			$('.ncsMenu > h5').removeClass('mobOn');
			$('.subBox').removeClass('onMenu');
			$('.mobMenuBtn').removeClass('mobMenuBtn_on');
			$('.menuLi > div').slideUp();
			$('.ncsMenu > div').slideUp();
			$('.ncsMenu > h5').children('span').text('+');
			$('.curriMenu01 > ul').slideUp();
			$('.curriMenu01 > h5').children('span').text('+');
		}
	})

	$('.mobMenu').on('click', function(){ //모바일 메뉴
		var ww = $(window).width();
		if(ww < 1080){
			var menuBox = $(this).siblings('div');
			if(menuBox.css('display') == 'none'){
				$(this).parent('li').siblings().children('div').slideUp();
				menuBox.slideDown(400);
			}else{
				menuBox.slideUp(400);
			}
		}

	});
	ncsMenu();
	curriMenu();
	campusPick();
});
function ncsMenu(){// 모바일 NCS지원센터
	$('.ncsMenu > h5').on('click', function(){
		var ncsOn = $('.ncsMenu > div');
		var ww = $(window).width();
		if(ww < 1080){
			if(ncsOn.css('display') == 'none'){
				ncsOn.slideDown(400);
				$(this).children('span').text('-');
			}else{
				ncsOn.slideUp(400);
				$(this).children('span').text('+');
			}
		}
	});
}
function curriMenu(){// 커리큘럼
	$('.curriMenu01 > h5').on('click', function(){
		var ww = $(window).width();
		if(ww < 1080){
			var curriOn = $('.curriMenu01 > ul');
			if(curriOn.css('display') == 'none'){
				curriOn.slideDown(400);
				$(this).children('span').text('-');
			}else{
				curriOn.slideUp(400);
				$(this).children('span').text('+');
			}
		}
	});
}
function campusPick(){
	//var campusH = $('.campusBox > div').height() - 24;
	//$('.campusBox > div').css('top', -campusH);
	$('.campusBox > div > button').off().on('click', function(){
		if($('.campusBox').hasClass('on') == false){
			$('.campusBox').addClass('on');
			//$('.campusBox > div').css('top', '0');
			$('.campusBox > div > div').slideDown();
		}else{
			$('.campusBox').removeClass('on');
			//$('.campusBox > div').css('top', -campusH);
			$('.campusBox > div > div').slideUp();
		}
	});
}
function getSubDomain(vals){
	switch (vals){
		case "1": sDomain = "gangnam"; break;
		case "2": sDomain = "jongro"; break;
		case "3": sDomain = "sinchon"; break;
		case "33": sDomain = "sc"; break;
		case "4": sDomain = "ydp"; break;
		case "5": sDomain = "gangnamac"; break;
		case "7": sDomain = "anyang"; break;
		case "8": sDomain = "incheon"; break;
		case "9": sDomain = "suwon"; break;
		case "10": sDomain = "cheongju"; break;
		case "11": sDomain = "daejeon"; break;
		case "12": sDomain = "daegu"; break;
		case "112": sDomain = "dgg"; break;
		case "13": sDomain = "busan"; break;
		case "913": sDomain = "busanac"; break;
		case "113": sDomain = "bs"; break;
		case "15": sDomain = "ca"; break;
		case "16": sDomain = "ansan"; break;
		case "17": sDomain = "ujb"; break;
		case "18": sDomain = "seongnam"; break;
		case "19": sDomain = "bucheon"; break;
		case "22": sDomain = "jeonju"; break;
		case "23": sDomain = "ilsan"; break;
		case "24": sDomain = "ulsan"; break;
		case "25": sDomain = "daejeonc"; break;
		case "26": sDomain = "gwangju"; break;
		case "27": sDomain = "nowon"; break;
		case "28": sDomain = "guwol"; break;
		case "29": sDomain = "gangnamit"; break;
		case "30": sDomain = "cheongra"; break;
		case "31": sDomain = "isac"; break;
		case "32": sDomain = "gjdg"; break;
		case "34": sDomain = "yeoksam"; break;
		case "35": sDomain = "cheonan"; break;
		case "36": sDomain = "nowon"; break;

	}
	return sDomain;
}