$(document).ready(function() {
	jQuery.noConflict();
	
	/*$("a#donate").bind("click", function() {
		$("#donate_form").submit()
	});*/

	/*$("a#single_1").fancybox();*/
		
	/*$("a#test-fancy").fancybox({
		'zoomOpacity'			: true,
		'overlayShow'			: false,
		'zoomSpeedIn'			: 500,
		'zoomSpeedOut'			: 500
	});*/
	
	/*$("a#single_3").fancybox({
		'overlayShow'			: false,
		'zoomSpeedIn'			: 600,
		'zoomSpeedOut'			: 500//,
		//'easingIn'				: 'easeOutBack',
		//'easingOut'				: 'easeInBack'
	});
	
	$("a.group").fancybox({
		'hideOnContentClick': false
	});*/
	
	jQuery("a#clic").click(function (e) {
		e.preventDefault();
		jQuery('#modal-content').modal(
			{
				onOpen: function (dialog) {
					dialog.overlay.fadeIn('slow', function () {
						dialog.data.hide();
						dialog.container.fadeIn('slow', function () {
							dialog.data.slideDown('slow');
						});
					});
				}, 
				containerCss:{						
					height:450,		
					width:550,
				},
				onClose: function (dialog) {
					dialog.data.fadeOut('slow', function () {
						dialog.container.hide('slow', function () {
							dialog.overlay.slideUp('slow', function () {
								jQuery.modal.close();
							});
						});
					});
				}
			}	
		);
	});
	
});/*cierra el document.ready Final del archivo*/

