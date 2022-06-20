// header Content
const BtnHeaderRightShare = document.querySelector('.content__header-right-social-share button');
const HeaderRightShareList = document.querySelector('.header__right-social-list');
const HeaderRightShareclose = document.querySelector('.header__right-cocial-close');
BtnHeaderRightShare.onclick = () => {
    HeaderRightShareList.style.display = 'block';
}

HeaderRightShareclose.onclick = () => {
    HeaderRightShareList.style.display = 'none';
}


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


// search
const SearchList = document.querySelector(".header__search-right-body-search textarea");
SearchList.setAttribute("placeholder", "Search district here");


// menu list

const navbarMennu = document.querySelector('.content__main-left-navbar-menu');
const navbarMennuShow = document.querySelector('.content__main-left-navbar');
const navbarMenuClose = document.querySelector('.content__main-left-navbar-close');
navbarMennu.onclick = () => {
    navbarMennuShow.style.display = 'block';
    navbarMenuClose.style.display = 'block';
}

navbarMenuClose.onclick = () => {
    navbarMennuShow.style.display = 'none';
}


// contact me
const inputList = document.querySelectorAll('.content__main-right-input, .content__main-left-contactMe textarea, .content__main-left-contactMe input');
const checkName = /^[a-zA-Z ]{2,30}$/;
const checkMail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
const checkPhone = /^0*[0-9]{10}$/
const btnSubmit = document.querySelector('.content__main-left-contact-btn[type="submit"]');

const labelContact = document.querySelectorAll('.content__main-left-contactMe label');
for (let index = 0; index < labelContact.length; index++) {
    labelContact[index].style.display = 'none';
}



btnSubmit.onclick = (e) => {
    check = true;
    if (!checkName.test(inputList[0].value)) {
        check = false;
        e.preventDefault();
        alert('Your name is invalid! Try again!');
    }

    if (!checkMail.test(inputList[1].value) && check) {
        check = false;
        e.preventDefault();
        alert('Your email is invalid! Try again!');
    }

    if (!checkPhone.test(inputList[2].value) && check) {
        check = false;
        e.preventDefault();
        alert('Your Phone is invalid! Try again!');
    }
    if (check) {
        alert('Success!');
    }
}

resetInput = () => {
    for (let i = 0; i < inputList.length; i++) {
        inputList[i].value = '';
    }
    inputList[inputList.length - 1].value = 'Reset';
}


// convert Html in map
const ConvertHtmlMap = document.querySelectorAll('.content__main-left-map');
const HtmlCode = document.querySelectorAll('.content__main-left-map-Converthtml');
const TittleMap = '<h3>Map</h3>';
for (let index = 0; index < ConvertHtmlMap.length; index++) {
    ConvertHtmlMap[index].innerHTML = TittleMap + HtmlCode[index].textContent;
}

const HeaderConvertHtml = document.querySelectorAll('.view__header-info-map-container');
const HtmlHeaderCode = document.querySelectorAll('.view__header-info-map-HeaderConverthtml');
for (let index = 0; index < HeaderConvertHtml.length; index++) {
    HeaderConvertHtml[index].innerHTML = HtmlHeaderCode[index].textContent;
}

const HeaderConvertHtmlStreet = document.querySelectorAll('.view__header-info-street-container');
const HtmlHeaderCodeStreet = document.querySelectorAll('.view__header-info-street-container .view__header-info-map-HeaderConverthtml');
for (let index = 0; index < HeaderConvertHtmlStreet.length; index++) {
    HeaderConvertHtmlStreet[index].innerHTML = HtmlHeaderCodeStreet[index].textContent;
}

// footer
const SendEmailFooter = document.querySelector(".footer__sendemail input:nth-of-type(2)");
SendEmailFooter.setAttribute("placeholder", "Your email address");