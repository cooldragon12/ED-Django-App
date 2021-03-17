
const prev = document.getElementById('prev');
const next = document.getElementById('next');
const focus = document.getElementById('focus-cont')
const photoSlider_cont = document.querySelector('.phot-cont');
var textHolder = document.querySelector('.texts-holder')

let index = 1;
// const fClone =document.getElementById('photo-clone')
// const lClone =document.getElementById('last-photo-clone')
// var ftClone = document.getElementById('ftClone')
// var ltClone = document.getElementById('ltClone')
document.addEventListener("DOMContentLoaded", ()=>{
	prev.addEventListener('click', ()=>{
		prevFunction()
	})
	next.addEventListener('click',()=>{
		nextFunction()
	})
	
})

	
class SwipeScroll {
	constructor (container) {
		this.container = container
		this.speed = 5
		this.debounceAfter = 50

		// binds
		this.scrolled = this.scrolled.bind(this)
		this.animate = this.animate.bind(this)

		// state
		this.to = 0
		this.current = 0
		this.animating = false
		this.frameId = 0

		this.container.addEventListener('scroll', _.debounce(this.scrolled, this.debounceAfter))
	}

	scrolled (event) {
		if (this.animating)
			return

		// current position to animate from
		this.current = this.container.scrollLeft

		// calculate position to animate to (closest div)
		const children = this.container.children
		const index = Math.round(this.current / children[0].offsetWidth)
		this.to = children[index].offsetLeft

		// run animation
		this.animating = true
		this.frameId = requestAnimationFrame(this.animate)
	}

	animate () {
		this.frameId = requestAnimationFrame(this.animate)
		this.current += (this.to - this.current) / this.speed
		this.container.scrollLeft = this.current.toFixed(2)

		// quit animation if goal reached
		if (Math.round(this.current) === this.to) {
			this.animating = false
			cancelAnimationFrame(this.frameId)
		}
	}
}

const container = document.getElementById('aNews-cont');
new SwipeScroll(container);

const nextFunction = () => {
	var photoSlides = document.querySelectorAll('.slide-photo');
	var textSlides = document.querySelectorAll('.parent-cons');
	
	var textCont = textSlides[index].clientHeight;
	var slidesViewLength = photoSlides[index].clientWidth;
	// photoSlides = getSlides();
	// index++;
	textHolder.style.transition = 'transform .5s ease-out'
	textHolder.style.transform = `translateY(${-textCont * index}px)`
	photoSlider_cont.style.transition = 'transform .7s ease-out';
	photoSlider_cont.style.transform = `translateX(${-slidesViewLength * index}px)`;
};
const prevFunction = () => {
	var photoSlides = document.querySelectorAll('.slide-photo');
	var textSlides = document.querySelectorAll('.parent-cons');
	
	var textCont = textSlides[index].clientHeight;
	var slidesViewLength = photoSlides[index].clientWidth;
	// index--;

	textHolder.style.transition = 'transform .5s ease-out'
	textHolder.style.transform = `translateY(${textCont % index}px)`

	photoSlider_cont.style.transition = 'transform .7s ease-out';
	photoSlider_cont.style.transform = `translateX(${slidesViewLength % index}px)`;
};
function slider(){
	return setInterval(() => {
		nextFunction()
	}, 3000)
}
slider()


