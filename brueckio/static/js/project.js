/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/

$( document ).ready(function() {
    // make whole project teaser clickable
    $('.project-teaser .project').click(function(event) {
        $(this).closest('.col').find('a')[0].click();
    });
    // toggle navbar class 
    $('#main-menu').on('show.bs.collapse', function () {
        $('header').addClass('open');
    })
    $('#main-menu').on('hide.bs.collapse', function () {
            $('header').removeClass('open');
    })

    $('form.contact-form').submit( function(event) {
        event.preventDefault();
        var $form = $(this);
        var button = $form.find('button').html('sending ...');
        var formData = {};
        $form.serializeArray().map(function(x){formData[x.name] = x.value;});
        $.ajax({
            url: '/api/contact-form/',
            type: 'post',
            dataType: 'json',
            data: formData,
            success: function(data) {
                $form.find('.form-group, button').fadeOut(800, function(){
                    $form.find('p.success').show();
                });
            },
            error: function(data) {
                $form.find('p.error').show().find('span.error-message').text(data.responseText);
            }
        });
    });
});