document.addEventListener("DOMContentLoaded", function () {
    let description = document.getElementById('description');
    console.dir(description);
    // -------------------------

    // Toggle menu on click
    // document.querySelector('#menu-toggler').addEventListener('click', (e) => {
    //     toggleBodyClass('menu-active');
    // });

    // function toggleBodyClass(className) {
    //     document.body.classList.toggle(className);
    // }

    // $(window).on('scroll', function () {
    //     if (window.pageYOffset > 0) {
    //         $('.menu').addClass('.active-scroll');
    //     } else {
    //         $('.menu').removeClass('.active-scroll');
    //     }
    // })

    // window.addEventListener('scroll', function () {
    //     let navigation = document.querySelector('menu-bar')
    //     if (this.window.pageYOffset > 0) {
    //         navigation.classList.add('active-scroll')
    //     } else {
    //         navigation.classList.remove('active-scroll')
    //     }
    // })

    $(document).ready(function () {

        $('.first-button').on('click', function () {

            $('.animated-icon1').toggleClass('open');
        });
        $('.second-button').on('click', function () {

            $('.animated-icon2').toggleClass('open');
        });
        $('.third-button').on('click', function () {

            $('.animated-icon3').toggleClass('open');
        });
    });


});

// -------------------------

//  ---
// AOS.init();
