// JavaScript for label effects only
	$(window).load(function(){
		$(".col-3 input").val("");
		
		$(".input-effect input").focusout(function(){
			if($(this).val() != ""){
				$(this).addClass("has-content");
			}else{
				$(this).removeClass("has-content");
			}
		})
	});

	window.onscroll = () => {
  const nav = document.querySelector('#navbar');
  if(this.scrollY <= 10) nav.className = ''; else nav.className = 'scroll';

    const div = document.querySelector('#RichFeyn');
  if(this.scrollY <= 10) div.className = ''; else div.className = 'scroll';
};