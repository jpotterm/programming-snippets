$(function(){
    var messages = $('ul.django-messages li');
    messages.on('click', click);

    function click(e) {
        $(e.currentTarget).addClass('display-none');
    }
});
