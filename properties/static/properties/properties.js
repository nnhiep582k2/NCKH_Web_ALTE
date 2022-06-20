//Sign up
// let checkMail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
// var mail1 = document.querySelector('.sign-up .form-input');
// var signUp = document.querySelector('.sign-up .done');
// var check;
// signUp.onclick = (e) => {
//     check = true;
//     if (!checkMail.test(mail1.value)) {
//         check = false;
//         e.preventDefault();
//         alert('Your email is invalid! Try again!');
//     } else check = true;
//     if (check) {
//         alert('Success!');
//     }
// }

// //Sign in
// var mail2 = document.querySelector('.sign-in .form-input');
// var psw = document.querySelector('.wrap-psw .form-input');
// var signIn = document.querySelector('.sign-in .done');
// var displayPsw = document.querySelector('.fa-eye');
// signIn.onclick = (e) => {
//     check = true;
//     if (!checkMail.test(mail2.value)) {
//         check = false;
//         e.preventDefault();
//         alert('Your email is invalid! Try again!');
//     }
//     if ((psw.value.length < 6 || psw.value.length > 12) && check) {
//         check = false;
//         e.preventDefault();
//         alert('Password is from 5 to 12! Try again!');
//     }
//     if (check) {
//         alert('Success!');
//     }
// }

// displayPsw.onclick = () => {
//     if (psw.type === 'password')
//         psw.type = 'text';
//     else
//         psw.type = 'password';
// }

// var myModal1 = document.querySelector('.my-modal.sign-up');
// var myModal2 = document.querySelector('.my-modal.sign-in');

// closeModal1 = () => {
//     myModal1.style.display = 'none';
// }

// closeModal2 = () => {
//     myModal2.style.display = 'none';
// }

// openModel1 = () => {
//     myModal1.style.display = 'block';
// }

// openModel2 = () => {
//     myModal2.style.display = 'block';
// }

// //Modal
// document.querySelector('.link-signup').onclick = () => openModel1();
// document.querySelector('.link-signin').onclick = () => openModel2();
// document.querySelector('.sign-up .fa-xmark').onclick = () => closeModal1();
// document.querySelector('.sign-in .fa-xmark').onclick = () => closeModal2();
// document.querySelector('.sign-up').onclick = () => closeModal1();
// document.querySelector('.sign-in').onclick = () => closeModal2();
// document.querySelector('.sign-in .form-modal').onclick = (e) => { e.stopPropagation(); }
// document.querySelector('.sign-up .form-modal').onclick = (e) => { e.stopPropagation(); }



// header-list__menu
var menuMobile = document.querySelector('.header-list__menu');
var HeaerListMenu = document.querySelector('.header__list');
var HeaderRightMenu = document.querySelector('.header__right');
var HeaerListMenuClose = document.querySelector('.header__right-close');
var menuHeight = HeaerListMenu.clientHeight;
menuMobile.addEventListener('click', () => {
    HeaderRightMenu.style.display = "block";
});

HeaerListMenuClose.addEventListener('click', () => {
    HeaderRightMenu.style.display = "none";
});


window.onscroll = () => {
    // console.info(document.documentElement.scrollTop);
    var headerPos = document.querySelector('.header');
    var levelUpGotoTop = document.querySelector('.gototop');
    if (document.documentElement.scrollTop > 1000) {
        // scroll header
        headerPos.style.position = "fixed";
        headerPos.style.left = 0;
        headerPos.style.right = 0;
        headerPos.style.background = "#fe6a00";

        // goto top
        levelUpGotoTop.style.display = 'block';

    } else {
        headerPos.style.background = "rgba(0, 0, 0, 0.5)";
        levelUpGotoTop.style.display = 'none';
    }
}

window.addEventListener('scroll', () => {
    var reveal__tranYs = document.querySelectorAll('.reveal__tranY');
    for (let i = 0; i < reveal__tranYs.length; i++) {
        var windowHeight = window.innerHeight;
        var reveal__tranYTops = reveal__tranYs[i].getBoundingClientRect().top;

        if (reveal__tranYTops < windowHeight) {
            reveal__tranYs[i].classList.add('active-tranY');
        } else {
            reveal__tranYs[i].classList.remove('active-tranY');
        }
    }

    var reveal__tranXs = document.querySelectorAll('.reveal__tranX');
    for (let i = 0; i < reveal__tranXs.length; i++) {
        var windowHeight = window.innerHeight;
        var reveal__tranXTops = reveal__tranXs[i].getBoundingClientRect().top;

        if (reveal__tranXTops < windowHeight) {
            reveal__tranXs[i].classList.add('active-tranX');
        } else {
            reveal__tranXs[i].classList.remove('active-tranX');
        }
    }

    var reveal__scales = document.querySelectorAll('.reveal__scale');
    for (let i = 0; i < reveal__scales.length; i++) {
        var windowHeight = window.innerHeight;
        var reveal__scaleTops = reveal__scales[i].getBoundingClientRect().top;

        if (reveal__scaleTops < windowHeight) {
            reveal__scales[i].classList.add('active-scale');
        } else {
            reveal__scales[i].classList.remove('active-scale');
        }
    }

    var reveal__tranAmXs = document.querySelectorAll('.reveal__tranAmX');
    for (let i = 0; i < reveal__tranAmXs.length; i++) {
        var windowHeight = window.innerHeight;
        var reveal__tranAmXTops = reveal__tranAmXs[i].getBoundingClientRect().top;

        if (reveal__tranAmXTops < windowHeight) {
            reveal__tranAmXs[i].classList.add('active-tranAmX');
        } else {
            reveal__tranAmXs[i].classList.remove('active-tranAmX');
        }
    }
});


// header slider
// var counter = 1;
// setInterval(function() {
//     document.getElementById('radio' + counter).checked = true;
//     document.querySelector('.header__slide-hidden' + counter).style.display = 'block';
//     counter++;
//     // document.querySelector('.header__slide-hidden' + counter - 1).style.display = 'none';
//     if (counter > 4) {
//         counter = 1;
//     }
// }, 2000);

// const sliderHeaderItems = document.querySelectorAll('.header__slide-img');
// const sliderHeaderItemsLength = sliderHeaderItems[0].clientWidth;
// console.log(sliderHeaderItemsLength);

var counter = 1;
setInterval(function() {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    // document.querySelector('.header__slide-hidden' + counter - 1).style.display = 'none';
    if (counter > 4) {
        counter = 1;
    }
}, 3000);


// // viewPhoto

const viewPhotos = document.querySelectorAll('.js__view-header-info-photo');
const showHeaderInfoPhotos = document.querySelectorAll('.view__header-info-photo');
const clickHeaderInfoCloseOnes = document.querySelectorAll('.view__header-info-photo-close');



for (let index = 0; index < viewPhotos.length; index++) {
    viewPhotos[index].addEventListener('click', function showInfoPhotoOne() {
        showHeaderInfoPhotos[index].style.display = 'flex';
    });
}



for (let index = 0; index < clickHeaderInfoCloseOnes.length; index++) {
    clickHeaderInfoCloseOnes[index].addEventListener('click', function() {
        showHeaderInfoPhotos[index].style.display = 'none';
    });
}


const viewPhotosSlider = document.querySelector('.view__header-info-photo-slider');
const viewPhotosMain = document.querySelector('.view__header-info-photo-slide');
var viewPhotosItems = document.querySelectorAll('.view__header-info-photo-img');
const viewPhotosBtnNext = document.querySelector('.view__header-photo-next-after');
const viewPhotosBtnPrev = document.querySelector('.view__header-photo-next-before');
var imgPhotoWidth = document.getElementById('widthPhotosImg');

let viewPhotosItemsLength = viewPhotosItems.length;
let positionPhotoX = 0;
let indexPhoto = 0;

viewPhotosBtnNext.addEventListener('click', function() {
    handleChangeSlideViewPhotos(1);
})

viewPhotosBtnPrev.addEventListener('click', function() {
    handleChangeSlideViewPhotos(-1);
});



function handleChangeSlideViewPhotos(check) {
    if (check === 1) {
        if (indexPhoto >= viewPhotosItemsLength - 1) {
            indexPhoto = viewPhotosItemsLength - 1;
            return;
        }
        positionPhotoX -= imgPhotoWidth.clientWidth;
        viewPhotosMain.style = `transform: translateX(${positionPhotoX}px)`;
        indexPhoto++;
    } else if (check === -1) {
        if (indexPhoto <= 0) {
            indexPhoto = 0;
            return;
        }
        positionPhotoX += imgPhotoWidth.clientWidth;
        viewPhotosMain.style = `transform: translateX(${positionPhotoX}px)`;
        indexPhoto--;
    }
}

// viewMap
const viewMaps = document.querySelectorAll('.js__view-header-info-map');
const showHeaderInfoMaps = document.querySelectorAll('.view__header-info-map');
const clickHeaderInfoCloseTwos = document.querySelectorAll('.view__header-info-map-close');



for (let index = 0; index < viewMaps.length; index++) {
    viewMaps[index].addEventListener('click', function showInfoMapOne() {
        showHeaderInfoMaps[index].style.display = 'flex';
    });
}




for (let index = 0; index < clickHeaderInfoCloseTwos.length; index++) {
    clickHeaderInfoCloseTwos[index].addEventListener('click', function() {
        showHeaderInfoMaps[index].style.display = 'none';
    });
}

//  viewStreet 
const viewStreers = document.querySelectorAll('.js__view-header-info-street');
const showHeaderInfoStreers = document.querySelectorAll('.view__header-info-street');
const clickHeaderInfoCloseThrees = document.querySelectorAll('.view__header-info-street-close');



for (let index = 0; index < viewStreers.length; index++) {
    viewStreers[index].addEventListener('click', function showInfoStreerOne() {
        showHeaderInfoStreers[index].style.display = 'flex';
    });
}




for (let index = 0; index < clickHeaderInfoCloseThrees.length; index++) {
    clickHeaderInfoCloseThrees[index].addEventListener('click', function() {
        showHeaderInfoStreers[index].style.display = 'none';
    });
}

//viewShare
const viewShares = document.querySelector('.js__view-header-info-share');
const showHeaderInfoShares = document.querySelector('.view__header-info-share');
const clickHeaderInfoCloseShare = document.querySelector('.view__header-info-share .view__header-info-street-close');

viewShares.addEventListener('click', function() {
    showHeaderInfoShares.style.display = 'flex';
});


clickHeaderInfoCloseShare.addEventListener('click', function() {
    showHeaderInfoShares.style.display = 'none';
});



// header search

const headerSearchRent = document.querySelector('.header__search-right-head .rent');
const headerSearchSale = document.querySelector('.header__search-right-head .sale');
headerSearchRent.style.background = '#fe6a00';
headerSearchRent.addEventListener('click', function() {
    headerSearchRent.style.background = '#fe6a00';
    headerSearchSale.style.background = '#2c2c2c';
});

headerSearchSale.addEventListener('click', function() {
    headerSearchSale.style.background = '#fe6a00';
    headerSearchRent.style.background = '#2c2c2c';
});

const SearchList = document.querySelector(".header__search-right-body-search textarea");
SearchList.setAttribute("placeholder", "Search district here");




const slideValue = document.querySelectorAll('.range .sliderValue span');
const inputSlider = document.querySelectorAll('.field input');
const slideSizeRight = document.querySelectorAll('.header__search-right-size-r');
for (let index = 0; index < inputSlider.length; index++) {
    inputSlider[index].oninput = (() => {
        let value = inputSlider[index].value;
        slideValue[index].textContent = value;
        slideSizeRight[index].textContent = value;
        slideValue[index].style.left = (value / 10) + "%";
        slideValue[index].classList.add('show');
    });
}
for (let index = 0; index < inputSlider.length; index++) {
    inputSlider[index].onblur = (() => {
        slideValue[index].classList.remove('show');
    });
}




// slide lists
const prevBtn = document.querySelector('.property__header-next-before');
const nextBtn = document.querySelector('.property__header-next-after');
const sliderListsItems = document.querySelectorAll('.property__list-body');
const sliderListsMain = document.querySelector('.property__lists-slide');
const sliderListsItemWidth = sliderListsItems[0].clientWidth;
const sliderListLength = sliderListsItems.length;
let positionX = 0;
let index = 0;
const sliderViewAllHidden = document.querySelector('.property__header-btn-right a');
var checkViewAll = 0;
nextBtn.addEventListener('click', function() {
    ++checkViewAll;
    if (checkViewAll != 0) {
        sliderViewAllHidden.style.cursor = 'no-drop';
    } else if (checkViewAll == 0) {
        sliderViewAllHidden.style.cursor = 'pointer';
    }
    handleChangeSlide(1);
})

prevBtn.addEventListener('click', function() {
    --checkViewAll;
    if (checkViewAll != 0) {
        sliderViewAllHidden.style.cursor = 'no-drop';
    } else if (checkViewAll == 0) {
        sliderViewAllHidden.style.cursor = 'pointer';
    }
    handleChangeSlide(-1);
});


function handleChangeSlide(check) {
    if (check === 1) {
        if (index >= sliderListLength - 1) {
            index = sliderListLength - 1;
            return;
        }
        positionX -= sliderListsItemWidth;
        sliderListsMain.style = `transform: translateX(${positionX}px)`;
        index++;
    } else if (check === -1) {
        if (index <= 0) {
            index = 0;
            return;
        }
        positionX += sliderListsItemWidth;
        sliderListsMain.style = `transform: translateX(${positionX}px)`;
        index--;
    }
}



// Like home
// const btnLikeProperties = document.querySelector(".property_list-btn-like");
// btnLikeProperties.onclick = () => {
//     if (btnLikeProperties.style.background == "red") {
//         btnLikeProperties.style.background = "chartreuse";
//     } else {
//         btnLikeProperties.style.background = "red";
//     }
// }

// ViewAll properties

const sliderViewbefore = document.querySelector('.property__header-next-before');
const sliderViewAfter = document.querySelector('.property__header-next-after');



sliderViewAllHidden.addEventListener('click', () => {
    sliderListsMain.style.display = 'block';
    sliderViewAllHidden.style.cursor = 'no-drop';
    sliderViewbefore.style.cursor = 'no-drop';
    sliderViewAfter.style.cursor = 'no-drop';
});


// footer
const SendEmailFooter = document.querySelector(".footer__sendemail input:nth-of-type(2)");
SendEmailFooter.setAttribute("placeholder", "Your email address");