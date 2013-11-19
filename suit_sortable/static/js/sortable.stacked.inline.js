django.jQuery(function () {
	var sortableStackedInline = function () {
		var init = function () {
			$('div.field-position').hide();

			if($('.inline-group').find('input[name$=-INITIAL_FORMS]').val() <= 1){
				return;
			}

			$('.inline-related:not(.last-related) h3').css('cursor', 'move');

			// hide the position column
			$('div.field-position').hide();
			$('.inline-group h2:first').append('<span class="description">Note: Drag &amp; drop rows to reorder. Save new inline row first</span>')

			$('.inline-group').sortable({
				axis: 'y',
				items: '.inline-related:not(.last-related)',
				cursor: 'move',
				update: function (event, ui) {
					$('.inline-related:not(.last-related)').each(function (i) {
						$('input[id$=position]', this).val(i + 1);
					});
				},
			});
		};
		init();
	};

	sortableStackedInline();

});