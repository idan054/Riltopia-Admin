$('.add-more-btn').click(function() {
  var clone = $('.form-main').clone('.form-block');
  $('.form-main').append(clone);
});