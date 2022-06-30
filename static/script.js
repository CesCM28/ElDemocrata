window.addEventListener('load', () => {

    let temperaturaValor = document.getElementById("temperatura-valor")
    let temperaturaCiudad = document.getElementById("temperatura-ciudad")

    const urlCh = `https://api.openweathermap.org/data/2.5/weather?q=Chihuahua&lang=es&appid=118fce7e8a401d0ba946654ca50a2bd6&units=metric`
        //console.log(url)
        fetch(urlCh)
            .then(response => { return response.json() })
            .then(data => {
                console.log(data)
                let temp = Math.round(data.main.temp)
                temperaturaValor.textContent = `${temp} °C`
                temperaturaCiudad.textContent = data.name
            })
            .catch(error => {
                console.log(error)
            })

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            console.log(position);
            lat = position.coords.latitude
            lon = position.coords.longitude

            const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&lang=es&appid=118fce7e8a401d0ba946654ca50a2bd6&units=metric`
            console.log(url)
            fetch(url)
                .then(response => { return response.json() })
                .then(data => {
                    console.log(data.main.temp)
                    let temp = Math.round(data.main.temp)
                    temperaturaValor.textContent = `${temp} °C`
                    temperaturaCiudad.textContent = data.name
                })
                .catch(error => {
                    console.log(error)
                })
        })
    }
})