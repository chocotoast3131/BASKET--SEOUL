
$('.main_menu li').mouseenter(function() {
  $( this ).children('.sub_menu').stop().slideDown()
} )
$('.main_menu li').mouseleave(function() {
  $( this ).children('.sub_menu').stop().slideUp()
} )


$('.btn span:first-child').click(function() {
  $('.tab1').show()
  $('.tab2').hide()
  $(this).addClass('active')
  $(this).siblings().removeClass('active')
} )
$('.btn span:last-child' ).click( function() {
  $('.tab2').css({display:'flex'})
  $('.tab1').hide()
  $(this ).addClass('active')
  $(this ).siblings().removeClass('active')
})