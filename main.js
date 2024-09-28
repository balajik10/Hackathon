// Function to send user input to the Flask backend for prediction
function sendToBackend() {
    // Retrieve values from the form
    var time = document.getElementById("time").value;
    var day = document.getElementById("day").value;
    var month = document.getElementById("month").value;
    var year = document.getElementById("year").value;
    var upiNumber = document.getElementById("upiNumber").value;
    var age = document.getElementById("age").value;
    var transactionAmount = document.getElementById("transactionAmount").value;
    var zipcode = document.getElementById("zipcode").value;

    // Construct the data point
    var data_point = {
        'trans_hour': time,
        'trans_day': day,
        'trans_month': month,
        'trans_year': year,
        'upi_number': upiNumber,
        'age': age,
        'trans_amount': transactionAmount,
        'zip': zipcode
    };

    // Validate the inputs
    if (!validateInputs(data_point)) {
        alert("Please fill in all the fields with valid values.");
        return;
    }

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data_point),
    })
    .then(response => response.json())
    .then(data => {
       
        console.log("Prediction Result:", data);

    })
    .catch((error) => {
        console.error('Error:', error);
    });
}


function validateInputs(data_point) {
  
    
    for (var key in data_point) {
        if (!data_point[key]) {
            return false;
        }
    }

    // Additional validation logic can be added here

    return true;
}
