

function predict(){
	
	$.ajax({
		type: "POST",
		url: "../cgi-bin/php/predict_xray.php",
		async: false,
		datatype: 'json',
		data: {
			imgBase64: canvas.toDataURL("image/png")
		},
		success: function(response){
			try {
				pneumonia_id.innerHTML = "Error";
				non_pneumonia_id.innerHTML = "Error";
				console.log(response);
				var obj = JSON.parse(response);
				console.log(obj.normal);
				console.log(obj.pneumonia);
				pneumonia_id.innerHTML = (parseFloat(obj.pneumonia)*100).toFixed(1) + "%";
				non_pneumonia_id.innerHTML = (parseFloat(obj.normal)*100).toFixed(1) + "%";
			}
			catch(err){
				console.log(response);
				pneumonia_id.innerHTML = "Error1";
				non_pneumonia_id.innerHTML = "Error1";
			}

		},
		error: function(response){
			console.log(response);
			pneumonia_id.innerHTML = "Error2";
			non_pneumonia_id.innerHTML = "Error2";
		}
	})
	
}
var image_xray = new Image();

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    //ev.preventDefault();
    img_id = ev.dataTransfer.getData("text");
    //ev.target.appendChild(document.getElementById(data));
	//alert(img_id);
	var img_element = document.getElementById(img_id);
	image_xray = img_element;
	//alert(image_xray);
	canvas = document.getElementById('canvas');
	ctx = canvas.getContext("2d");
	
	ctx.drawImage(image_xray, 0, 0, 250, 250, 0, 0, 400, 400);
}

function allowDrop(ev) {
    ev.preventDefault();
}



function page_load(){
	

	pneumonia_id = document.getElementById("pneumonia");
	non_pneumonia_id = document.getElementById("non_pneumonia");
	
	x_ray_image_id = document.getElementById("x_ray_image");
}