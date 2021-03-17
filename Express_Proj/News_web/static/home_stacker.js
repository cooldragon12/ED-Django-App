
var today = new Date();
var day = 1

//To Get Dates Between
// function getDates( day1, day2 ){
// 	var oneDay = 24*3600*1000;
// 	for (var d=[],ms=day1*1,last=day2*1;ms<last;ms+=oneDay){
// 		d.push( new Date(ms) );
// 	}
// 	return d;
// }
//Carousel

main_loader()
function dateConverter(dateIso) {
	var date = new Date(dateIso)
	var yr = date.getFullYear()
	var month = date.getMonth() + 1
	var dt = date.getDate()
	if (dt < 10) {
		dt = '0' + dt;
	}
	if (month < 10) {
		month = '0' + month;
	}
	var newDate = (yr + '-' + month + '-' + dt);
	return newDate
}

async function loader_article(categid, name) {
	// Artcle Loader
	var url = `http://127.0.0.1:8000/api/article/?category=${categid}`;
	var wrapper = document.getElementById(`a${name}-cont`);
	await fetch(url)
		.then(resp => resp.json())
		.then(data => {

			for (i = 0; i < data.length; i++) {

				var e = data[i];
				var tmplt = `
            <a href="${e.get_absolute_url}">
                <div class="card-holder md">
					<div class="item-cont"></div>
					<h4>${e.headline}</h4>
                    <div class = "artima-m dark" style="background-image:linear-gradient(to bottom, rgba(99, 99, 99, .0), rgba(99, 99, 99, .0), rgba(61, 61, 61, 0.6)), url(${e.picture})">
                    </div>
					
                </div>
            </a>
            `
				wrapper.innerHTML += tmplt
			}
			console.log(data + "loader_article")
		})

};
//Getting the latest
var latest = ''
async function latest_article(latest) {
	let err = 'Nothing Found'
	await fetch(`http://127.0.0.1:8000/api/article/?category=&date_published=${latest}`)
		.then(resp => resp.json())
		.then(data => {
			if (data == "") {
				return err
			} else {
				const wrapper = document.getElementById('aLatest-cont')
				console.log(data)
				for (i = 0; i < data.length; i++) {
					d = data[i]
					var tmplt = `
					<a href="${d.get_absolute_url}">
						<div class="card-holder md">
							<div class="item-cont"></div>
							<h4>${d.headline}</h4>
							<div class = "artima-m dark" style="background-image:linear-gradient(to bottom, rgba(99, 99, 99, .0), rgba(99, 99, 99, .0), rgba(61, 61, 61, 0.6)), url(${d.picture})">
							</div>
							
						</div>
					</a>
					`
					wrapper.innerHTML += tmplt

				}
				console.log(data + "Latest Article")
			}

		}).catch(() => {
			return err
		})
};
async function getTrending() {
	let err = 'Nothing Found'
	await fetch(`http://127.0.0.1:8000/api/article/?category=&date_published=&trending=true`)
		.then(resp => resp.json())
		.then(data => {
			if (data == "") {
				return err
			} else {
				const wrapper_left = document.getElementById('photoholder')
				const wrapper_right = document.getElementById('texts-holder')
				console.log("Trending Loader")
				for (i = 0; i < data.length; i++) {
					d = data[i]
					var tmplt = `
					<div class="slide-photo">
						<div class ="back-photo" id="back-photo" style="background-image:linear-gradient(to bottom, rgba(99, 99, 99, .0), rgba(99, 99, 99, .0), rgba(61, 61, 61, 0.6)), url(${d.picture})">
					</div>
						`
					var con = `
				<div class="parent-cons">
					<div id="text-cons" class="text-cons">
						<h1>Trending.</h1>
						<p>${d.body}</p>
						<a href="${d.get_absolute_url}">See article here</a>
					</div>
				</div>
				`
					wrapper_left.innerHTML += tmplt
					wrapper_right.innerHTML += con
					console.log(`Trending Loader Succes ${i}`)

				}

			}

		}).catch(() => {
			return err
		})

}



async function main_loader() {
	await getTrending()
	var url = 'http://127.0.0.1:8000/api/category/'
	await fetch(url)
		.then(resp => resp.json())
		.then(data => {
			for (i = 0; i < data.length; i++) {
				var cet = data[i]
				loader_article(cet.categr_id, cet.category_name)
			}
		}).then(() => {
			latest = dateConverter(today)
			if (latest_article(latest) == 'Nothing Found') {
				latest = dateConverter(today - 1)
				latest_article(latest)
			}
		})







}



//<----Index=Carousel---->


// Latest Carousel




