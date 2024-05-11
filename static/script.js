document.addEventListener('DOMContentLoaded', function () {
    console.log('Page is loaded!')
    // Define all constants at the beginning
    const Spinner = document.querySelector('#spinner');
    const CloseAnswer = document.querySelector('#close-answer');
    const Answer = document.querySelector('#answer');
    const Form = document.querySelector('form');
    const Date = document.querySelector('#Date');
    const Company = document.querySelector('#Company');
    const Price = document.querySelector('#Price');
    const Volume = document.querySelector('#Volume');
    const SymbolInput = document.querySelector('#name');

    // Function to toggle spinner visibility
    function spinner(flag) {
        Spinner.style.display = flag ? 'block' : 'none';
    }

    // Close answer button event listener
    CloseAnswer.addEventListener('click', function () {
        Answer.style.display = 'none';
    });

    // Form submission event listener
    Form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Display a message
        const symbol = SymbolInput.value;
        getQuote(symbol);

        // Reset the form after submission
        event.target.reset();
    });

    // Function to get stock quote
    async function getQuote(symbol) {
        spinner(true);
        const response = await fetch(`/get_quote_query_param?symbol=${symbol}`);
        const data = await response.json();
        Answer.style.display = 'block';
        Company.textContent = `Company: ${data.Company}`;
        Date.textContent = `Date: ${data.Date}`;
        Price.textContent = `Price: ${data.Price}`;
        Volume.textContent = `Volume Traded: ${data.Volume}`;
        spinner(false);
    }
});
