// Up to top
window.onscroll = function() { scrollFunction() };

scrollFunction = () => {
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        document.querySelector('.up').style.bottom = '40px';
    } else document.querySelector('.up').style.bottom = '-40px';
}

// Change primary color
var rootStyle = document.documentElement.style;
var changeColor = document.querySelector('.change-color');

changeColor.onclick = function() {
    if (changeColor.style.backgroundColor == 'black') {
        setTimeout(function() {
            rootStyle.setProperty('--primary-color', 'rgb(253, 124, 32)');
            rootStyle.setProperty('--secondary-color', 'rgb(226, 108, 24)');
            rootStyle.setProperty('--bg-color', '#f7f7f7');
            rootStyle.setProperty('--subtext-color', 'rgb(87, 87, 87)');
            rootStyle.setProperty('--properties-color', '#ff6a00');
            changeColor.style.backgroundColor = 'rgb(253, 124, 32)';
            changeColor.style.hover = 'black';
        }, 300);
    } else {
        setTimeout(function() {
            rootStyle.setProperty('--primary-color', 'black');
            rootStyle.setProperty('--secondary-color', 'rgb(110, 110, 110)');
            rootStyle.setProperty('--bg-color', 'rgb(39, 39, 39)');
            rootStyle.setProperty('--subtext-color', 'white');
            rootStyle.setProperty('--properties-color', 'rgb(28, 28, 28)');
            changeColor.style.backgroundColor = 'black';
            changeColor.style.hover = '#3f56ff';
        }, 300);
    }
}

// Agents
var agents = document.getElementsByClassName('our-agents');
for (var i = 0; i < agents.length; i++) {
    agents[i].addEventListener("mouseover", function() {
        this.style.transform = 'translateY(-8px)';
        this.style.transition = '0.4s';
    })
    agents[i].addEventListener("mouseout", function() {
        this.style.transform = 'translateY(0)';
        this.style.transition = '0.4s';
    })
}

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

//Sign in
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
// var closeBtn1 = document.querySelector('.sign-up .fa-xmark');
// var closeBtn2 = document.querySelector('.sign-in .fa-xmark');

// closeModal1 = () => {
//     myModal1.style.display = 'none';
//     closeBtn1.style.display = 'none';
// }

// closeModal2 = () => {
//     myModal2.style.display = 'none';
//     closeBtn2.style.display = 'none';
// }

// openModel1 = () => {
//     myModal1.style.display = 'block';
//     closeBtn1.style.display = 'block!important';
// }

// openModel2 = () => {
//     myModal2.style.display = 'block';
//     closeBtn2.style.display = 'block!important';
// }

// //Modal
// document.querySelector('.link-signup').onclick = () => openModel1();
// document.querySelector('.link-signin').onclick = () => openModel2();
// closeBtn1.onclick = () => closeModal1();
// closeBtn2.onclick = () => closeModal2();
// document.querySelector('.sign-up').onclick = () => closeModal1();
// document.querySelector('.sign-in').onclick = () => closeModal2();
// document.querySelector('.sign-in .form-modal').onclick = (e) => { e.stopPropagation(); }
// document.querySelector('.sign-up .form-modal').onclick = (e) => { e.stopPropagation(); }

//Mobile
document.querySelector('.header__right .fa-xmark').onclick = () => {
    document.querySelector('.header__right').style.display = 'none';
}
document.querySelector('.mobile-bars').onclick = () => {
    document.querySelector('.header__right').style.display = 'block';
}

// footer
const SendEmailFooter = document.querySelector(".footer__sendemail input:nth-of-type(2)");
SendEmailFooter.setAttribute("placeholder", "Your email address");