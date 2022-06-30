window.addEventListener('load', () => {

    let temperaturaValor = document.getElementById("temperatura-valor")
    //let temperaturaCiudad = document.getElementById("temperatura-ciudad")
    let temperaturaIcon = document.getElementById("temperatura-icono")

    const urlCh = `https://api.openweathermap.org/data/2.5/weather?q=Chihuahua&lang=es&appid=118fce7e8a401d0ba946654ca50a2bd6&units=metric`
        //console.log(url)
        fetch(urlCh)
            .then(response => { return response.json() })
            .then(data => {
                temperaturaValor.textContent = `${data.main.temp} °`
                //temperaturaCiudad.textContent = data.name
                temperaturaIcon.src = `http://openweathermap.org/img/wn/${data.weather[0].icon}.png`
            })
            .catch(error => {
                console.log(error)
            })

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            lat = position.coords.latitude
            lon = position.coords.longitude

            const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&lang=es&appid=118fce7e8a401d0ba946654ca50a2bd6&units=metric`
            fetch(url)
                .then(response => { return response.json() })
                .then(data => {
                    temperaturaValor.textContent = `${data.main.temp} °`
                    //temperaturaCiudad.textContent = data.name
                    temperaturaIcon.src = `http://openweathermap.org/img/wn/${data.weather[0].icon}.png`
                })
                .catch(error => {
                    console.log(error)
                })
        })
    }
})