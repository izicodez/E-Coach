function update() {
    console.log("Update List")
    aname = document.getElementById('title').value
    age = document.getElementById('age').value
    if ((aname == " " || age == " " )){
        return
    }
    
    
    if (localStorage.getItem('itemsJson') == null) {
        itemJsonArray = [];
        itemJsonArray.push([aname, age])
        localStorage.setItem('itemsJson', JSON.stringify(itemJsonArray))
    }
    else {
        itemJsonArrayStr = localStorage.getItem('itemsJson')
        itemJsonArray = JSON.parse(itemJsonArrayStr)
        itemJsonArray.push([aname, age])
        localStorage.setItem('itemsJson', JSON.stringify(itemJsonArray))
    }
    
    // Populate Table

    let tableBody = document.getElementById('tableBody')
    let str = ""
    itemJsonArray.forEach((element, index) => {
        str += `
            <tr>
                <th scope="row">${index+1}</th>
                <td>${element[0]}</td>
                <td>${element[1]}</td>
                <td><button class="btn btn-sm btn-primary" onclick="deletevalue(${index})">Delete</button></td>
            </tr>
            `
    });

    tableBody.innerHTML = str
           
}

add = document.getElementById("add");
add.addEventListener("click", update);
populate()

function populate(){
    itemJsonArrayStr = localStorage.getItem('itemsJson')
    itemJsonArray = JSON.parse(itemJsonArrayStr)
    localStorage.setItem('itemsJson', JSON.stringify(itemJsonArray))

    let tableBody = document.getElementById('tableBody')
    let str = ""
    itemJsonArray.forEach((element, index) => {
        str += `
            <tr>
                <th scope="row">${index+1}</th>
                <td>${element[0]}</td>
                <td>${element[1]}</td>
                <td><button class="btn btn-sm btn-primary" onclick="deletevalue(${index})">Delete</button></td>
            </tr>
            `
    });

    tableBody.innerHTML = str
}

function deletevalue(itemIndex){
    itemJsonArrayStr = localStorage.getItem('itemsJson')
    itemJsonArray = JSON.parse(itemJsonArrayStr)
    itemJsonArray.splice(itemIndex,1)

    localStorage.setItem('itemsJson', JSON.stringify(itemJsonArray))
    populate()
}



