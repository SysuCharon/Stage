$(function(){
	// nav active
	var pgurl = window.location.href.split('/')
	if(pgurl.length > 4) {
		temp = pgurl[pgurl.length - 2]
	} else {
		temp = ''
	}
	var active = '/' + temp
	$("nav a").each(function(){
		if($(this).attr("href") == active)
			$(this).addClass("active");
	})
})