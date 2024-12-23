$(document).ready(function () {
    // Show modal when "Apply" button is clicked
    $(".apply-btn").on("click", function () {
        const jobTitle = $(this).siblings("h3").text();
        $("#job-title").text(jobTitle);
        $("#applicationModal").fadeIn(); // Show modal
    });

    // Hide modal when close button is clicked
    $(".close-btn").on("click", function () {
        $("#applicationModal").fadeOut(); // Hide modal
    });

    // Hide modal when clicking outside of the modal content
    $(window).on("click", function (event) {
        if ($(event.target).is("#applicationModal")) {
            $("#applicationModal").fadeOut();
        }
    });

    // Prevent modal from displaying on page load
    $("#applicationModal").hide();

    // Handle form submission
    $("#job-application-form").on("submit", function (e) {
        e.preventDefault();
        alert("Application submitted successfully!");
        $("#applicationModal").fadeOut(); // Hide modal after submission
        this.reset(); // Clear form fields
    });
});
