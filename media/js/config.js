var Example = function(config)
{
	this.initialize = function()
	{
		/*
		 * Initialize our textareas with the AP Text Counter plugin.
		 */
		$("#track").apTextCounter({
			maxCharacters: 25,
			direction: "down",
			tracker: "#track2",
			trackerTemplate: "%s character(s) left"
		});

		/*$("#textarea2").apTextCounter({
			maxCharacters: 25,
			direction: "up",
			tracker: "#tracker2",
			trackerTemplate: "%s character(s) typed"
		});

		$("#textarea3").apTextCounter({
			maxCharacters: 25,
			direction: "down",
			tracker: "#tracker3",
			trackerTemplate: "%s character(s) left",

			onTrackerUpdated: function(msg) {
				if (msg.count <= 0)
				{
					$(msg.config.tracker).css("color", "red");
				}
				else
				{
					$(msg.config.tracker).css("color", "black");
				}
			}
		});*/

		/*
		 * Set initial focus.
		 */
		//$("#textarea1").focus();
	};

	this.__config = (config || {});
	this.initialize();
};

