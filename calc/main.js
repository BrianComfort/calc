{
    const input = document.querySelector('#input');
    const answers = document.querySelector('#answers')


    function handleKeyUp(event) {
        // Check if the pressed key is Enter (key code 13)
        if (event.keyCode === 13 || event.key === "Enter") {
            send = input.value;

            function invokeLambda() {
                // Replace 'YOUR_PUBLIC_LAMBDA_URL' with the actual public URL of your AWS Lambda function
                const lambdaURL = "https://xptjp1lbk6.execute-api.us-west-1.amazonaws.com/calculator-testing?eq=12-5@var(x)&var=[{%27letter%27:%20%27x%27,%20%27val%27:%20%2729%27},%20{%27letter%27:%20%27y%27,%20%27val%27:%20%2729%27}]";
                fetch(lambdaURL)
                    .then(response => response.json()) // Assuming the Lambda returns JSON data
                    .then(data => {
                        // Handle the response data here
                        console.log('Response from Lambda:', data);

                        const newRowElement = document.createElement("span");
                        newRowElement.classList.add("row");
                        newRowElement.innerText = data['answer']

                        answers.appendChild(newRowElement)
                    })
                    .catch(error => {
                        // Handle any errors that occurred during the request
                        console.error('Error:', error);
                    });
            }

            invokeLambda();
        }
    }

    document.addEventListener("keyup", handleKeyUp);
}