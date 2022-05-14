function searchAPI() {

    let realDate = document.getElementById('date').value;
    let searchData = new URLSearchParams()
    searchData.append('date', realDate); 
    

    fetch('/apod-api', {method:'POST', 
    body: searchData
    }).then((res) => res.json()).then((data) => {
        console.log(data);      
        console.log(data['info']['date'])
        let description = document.querySelector('.description');
        let pic = document.querySelector('.pic');
        let titleDate = document.querySelector('.text');
        description.innerHTML = data['info']['explanation']
        pic.src = data.info.url;
        titleDate.innerHTML = data.info.title + ', &nbsp;&nbsp;' + data.info.date
        
        
    }).catch((error) => alert(error));
    return false
};
