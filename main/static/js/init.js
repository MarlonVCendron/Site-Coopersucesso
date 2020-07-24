(function($){
  $(function(){
    $('.sidenav').sidenav().on('click tap', 'li a', () => {
      $('.sidenav').sidenav('close');
    });

    $('.parallax').parallax();

    $('.owl-carousel').owlCarousel({
      loop:true,
      margin:0,
      nav:true,
      autoplay:true,
      autoplayTimeout:4000,
      autoplayHoverPause:true,
      responsive:{
        0:{
          items:1
        },
        600:{
          items:2
        },
        1200:{
          items:3
        }
      }
    });

    $("a").on('click', function(event) {
      if (this.hash !== "") {
        event.preventDefault();

        var hash = this.hash;

        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 500, function(){
          window.location.hash = hash;
        });
      }
    });

    'use strict';

    let c, currentScrollTop = 0, navbar = $('nav');

    $(window).scroll(function () {
      var a = $(window).scrollTop();
      var b = navbar.height();

      currentScrollTop = a;

      if (c < currentScrollTop && a > b + b) {
        navbar.addClass("scrollUp");
      } else if (c > currentScrollTop && !(a <= b)) {
        navbar.removeClass("scrollUp");
      }
      c = currentScrollTop;
    });
  });
})(jQuery);


const faders = document.querySelectorAll('.fade-in');
const sliders = document.querySelectorAll('.slide-in');

const options = {
  threshold: 0,
  rootMargin: "0px 0px -200px 0px"
};

const appearOnScroll = new IntersectionObserver(function(entries, appearOnScroll){
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('appear');
      const children = entry.target.children;
      for (let i = 0; i < children.length; i++) {
        children[i].classList.add('appear');
      }

      appearOnScroll.unobserve(entry.target);
    }
  });

}, options);

faders.forEach(fader => {
  appearOnScroll.observe(fader);
});

sliders.forEach(slider => {
  appearOnScroll.observe(slider);
});

let inOut = true;

setInterval(function(){
  if (inOut) {
    $('#logo-container div').find(".fadeTop").fadeIn(1000);
  }else {
    $('#logo-container div').find(".fadeTop").fadeOut(1000);
  }

  inOut = !inOut;
}, 5000);
