$(document).ready(function () {
    console.log($);
    console.log(jQuery);
    console.log("We are using jQuery");
    //$('selector').action() or $('selector').function();
  //  $('p').click();
    $('p').click(function () {
        console.log('you clicked on p ', this);
        //$('p').hide();
       // $(this).hide();
        //$('#id').hide();
        //$('.class').hide();
    });
//  $('#second').click();
//  $('.odd').click();
// $('*').click()
// $('p.odd').click();
 $('p:first').click()

})
$('#first').focus()
$('input').focus(function() { $(this).css('background', '#ff0') } )
$('input') .blur(function() { $(this).css('background', '#aaa') } )
$('#test').mouseover(function() { $(this).html('Hey, stop tickling!') } )
$('#test').mouseleave(function() { $(this).html('Where did you go?') } )

// $('#hide').click(function() { $('#text').hide() })
// $('#show').click(function() { $('#text').show('slow', 'linear') })
$('#toggle').click(function() { $('#text').toggle() })
$('button').click(function()
{
var elem = ''
if ($(this).parent().is('div')) elem = 'div'
else elem = 'span'
$('#info').html('You clicked a ' + elem)
})