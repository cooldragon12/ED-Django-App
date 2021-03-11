//Admin Style Util
var backGro = document.getElementById('ms-cont-back');
var bttonComp = document.querySelector('.compose_bttn');
var composer = document.getElementById('compose-container');
var vicomp = document.querySelector('.msactive1');
let closeBtton = document.getElementById('ms-closer');
let nextBtn = document.querySelector('.p-next');
let prevBtn = document.querySelector('.p-previous');
let pubBtn = document.querySelector('.p-submit');
let page_article = document.querySelector('.page-article');
//Index Style Util
let nextTrend = document.getElementById('next')
let prevTrend = document.getElementById('prev')

let page_media = document.querySelector('.page-media');
let fileElem =document.getElementById('fileElem');
function goBack() {
    window.location.hash = window.location.lasthash[window.location.lasthash.length-1];
    window.location.lasthash.pop();
}


nextTrend.

bttonComp.addEventListener('click', ()=>{
    composer.classList.add('msactive1')
    vicomp.style.visibility = 'visible';
    vicomp.style.opacity = '1';
    backGro.classList.add('ms-active')
    
    
});
closeBtton.addEventListener('click',()=>{
    backGro.classList.remove('ms-active')
    composer.classList.remove('msactive1');
    goBack()
});
backGro.addEventListener('click', ()=>{
    backGro.classList.remove('ms-active')
    composer.classList.remove('msactive1');
    goBack()
});
nextBtn.addEventListener('click', ()=>{
    page_article.style.marginLeft = "-50%";
});
prevBtn.addEventListener('click', ()=>{
    page_article.style.marginLeft = "0%";
});

        