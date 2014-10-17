/*

	JS controller for barntarnst.com
	Free to use & copy.
	
	by Bärnt & Ärnst http://barntarnst.com

*/

var baa = (function() {

	//Holds all public funtions.
	var API = {};
	var view;
	var api_url;
	//Absolute path set to '/', used during testing.
	var root = "/";
	var at = 0;
	// Constants / options

	/**
	* Constructor
	*/
	API.init = function(baseurl) 
	{
		API.setbaseurl(baseurl);
		API.render();
		API.setevents();

		$(".title").lettertwist(12);
		$(".heading").lettertwist(12);
		$(".twist").lettertwist(12);
		$(".item").lettertwist(12);


	}
	API.scrolled = function(totop) 
	{
		if(totop > $(window).height()) {
			$(".go-up").fadeIn('slow');
		} else {
			$(".go-up").fadeOut('slow');
		}

		if(totop >= $("#work").offset().top-40 && totop <= ($("#work").offset().top + $("#work").outerHeight(false) - 50)) {
			$(".go-up").css("color", "#52c6b5");
		} else {
			$(".go-up").css("color", "#fff");
		}
	}
	API.setevents = function()
	{
		//API.setevents_resortlist();

		var stateObj = { foo: "bar" };


		// Menyknappar
		$(".item-news").click(function() {
			API.gotopage('news');
		});
		$(".item-about").click(function() {
			API.gotopage('about');
		});
		$(".item-work").click(function() {
			API.gotopage('work');
		});
		$(".item-contact").click(function() {
			API.gotopage('contact');
		});

		//totop
		$(".go-up").click(function() {
			API.gotopage('intro');
		});

		$("#toggle-newsletter").click(function() {
			$(this).slideUp("fast", function() {
				//$("#newsletter-form").css("display", "inline-block");
				$("#newsletter-form").slideDown("fast");
				$("#newsletter").focus();
				$("#newsletter").autoResize();
			});
		});
		$("#sendmail").click(function() {
			if($("#form-name").val() != "" && $("#form-name").val() != "Your name" && $("#contact-text").val() != "" && $("#contact-text").val() != "Your message") {
				//console.log(api_url+'signup');
				var fname = $("#form-name").val();
				var femail = $("#form-email").val();
				var fmessage = $("#contact-text").val();

				$("#form-name").val("Your name"); $("#form-email").val("Your email"); $("#contact-text").val("Your message");


				$("#contact-form").hide("fast", function() {
					$("#contact-form-info").html("<i class='icon-cloud-upload'></i> Sending message..<br /><br />");
				
				
					$.post($("#post-url").val()+'sendmail', { name: fname, email: femail, message: fmessage })
						.done(function(data) {
		  					//console.log(data);
		  					$("#contact-form-info").html("<i class='icon-ok'></i> Your message has been sent! Thank you.<br /><br />");	
						})
						.fail(function(xhr, textStatus, errorThrown) {
							$("#contact-form-info").html("<i class='icon-ban-circle'></i> Something went wrong..<br /><br />");
						})
						.always(function() {
							$("#contact-form").show("slow");
						});
				});
			}
			else {
				$("#contact-form-info").html("<i class='icon-warning-sign'></i> At least fill in your name and a message?<br /><br />");
			}
		});


	} 
	API.setbaseurl = function(baseurl) {
		//console.log("setting url");
		api_url = baseurl;
	}
	/**
	* Draws UI
	*/
	API.render = function() 
	{
		//UI settings.
		//API.start();
		//API.render_resortlist();

		//$("#intro-margin").height($(window).height()*0.19);
		$("#intro").css('min-height', $(window).height()+'px');
		$("#contact").css('min-height', $(window).height()+'px');
		$("#centerme").vcenterme();


		//Render 
	}

	/**
	*	Front page init.
	*/
	API.start = function()
	{

		
	}
	API.gotopage = function(page) {
		$('html,body').animate({
		    scrollTop: $("#"+page).offset().top
		}, 'slow');
	}
	/*
	*	Some basic stuff --> should be made a jquery extension.
	**/
	API.centerus = function(classname)
	{
		$("."+classname).each(function() {
			var height = $(this).outerHeight();
			var parentheight = $(this).parent().height();
			var margintop = parentheight/2 - height/2;
			$(this).css("margin-top", margintop);
		});		
	}

	/**
	*
	*	Code for wallpaper - Resortlist!
	*	
	**/
	var tempwidth = {
		left : 25,
		right: 25,
		g_left: 10,
		g_right: 10
	}
	API.render_resortlist = function() {
		var row_size = Math.ceil($(window).width()/$('.room').outerWidth(true));
		var wallpaper_size = row_size*$('.room').outerWidth(true);
		var wallpaper_margin = (-wallpaper_size+$(window).width())/2;
		$("#wallpaper-resortlist").width(wallpaper_size);
		$("#wallpaper-resortlist").css("margin-left", wallpaper_margin+"px")
	}
	API.setevents_resortlist = function() {
		$(".room").hover(function() {
			tempwidth.left = $(this).children('.curtains').children().eq(0).children('img').attr("width");
			tempwidth.right= $(this).children('.curtains').children().eq(1).children('img').attr("width");
			tempwidth.g_left = $(this).children('.curtains').children().eq(2).children('img').attr("width");
			tempwidth.g_right = $(this).children('.curtains').children().eq(3).children('img').attr("width");
			
			$(this).children('.curtains').children().eq(0).children('img').stop().animate({ width: "24%" }, 1300);
			$(this).children('.curtains').children().eq(1).children('img').stop().animate({ width: "24%" }, 1300);
			$(this).children('.curtains').children().eq(2).children('img').stop().animate({ width: "12%" }, 600);
			$(this).children('.curtains').children().eq(3).children('img').stop().animate({ width: "12%" }, 600);

		}, function() {
			$(this).children('.curtains').children().eq(0).children('img').stop().animate({ width: tempwidth.left  }, 300);
			$(this).children('.curtains').children().eq(1).children('img').stop().animate({ width: tempwidth.right  }, 300);
			$(this).children('.curtains').children().eq(2).children('img').stop().animate({ width: tempwidth.g_left  }, 600);
			$(this).children('.curtains').children().eq(3).children('img').stop().animate({ width: tempwidth.g_right  }, 600);
		});
		$(".room").click(function() {
			$(this).children('.lights').toggleClass('on');
			$(this).children('.lights-off').toggleClass('on');
		});
	}

	return API;
	
})();




