$(document).ready(function() {
    $('#contact-form').submit(function(e) {
        e.preventDefault();
        
        $.ajax({
            url: $(this).attr('action'), // URL from the form's action attribute
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                var popup = $('#popup');
                var popupContent = $('#popup-content');
                
                if (response.success) {
                    popupContent.text('Form saved successfully!');
                    popup.addClass('success');
                } else {
                    popupContent.text('Error saving form.');
                    popup.addClass('error');
                }
                popup.removeClass('hidden');
            },
            error: function() {
                var popup = $('#popup');
                var popupContent = $('#popup-content');
                
                popupContent.text('An error occurred.');
                popup.addClass('error');
                popup.removeClass('hidden');
            }
        });
    });
});
