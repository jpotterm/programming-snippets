// ----------------------------------------
// Similar to Firefox native scrollIntoView
//
// Dependencies
//     gsap (with ScrollToPlugin)
// ----------------------------------------

TweenLite.to(window, 0.65, {scrollTo: {y: scrollAmount}, ease: Power4.easeOut});

// Or using glove-js animation
new Animation(650, Easings.outQuart, function(progress) {
    window.scrollTo(0, start + delta * progress);
}).start();
