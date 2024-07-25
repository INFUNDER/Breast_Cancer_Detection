document.addEventListener("DOMContentLoaded", function() {
    var spinner = document.getElementById('loading-spinner');

    // Show the spinner on page load
    spinner.classList.remove('d-none');

    // Hide the spinner after the content is loaded
    window.addEventListener('load', function() {
        spinner.classList.add('d-none');
    });

    // Optionally, show the spinner on form submit
    var forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            spinner.classList.remove('d-none');
        });
    });
});


  

