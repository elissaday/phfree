<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];

    $to = 'eday@g.harvard.edu';
    $subject = 'Contact Form Submission';
    $body = "Name: $name\nEmail: $email\n\nMessage:\n$message";

    // Send email
    if (mail($to, $subject, $body)) {
        echo '<p>Your message has been sent successfully!</p>';
    } else {
        echo '<p>Oops! Something went wrong. Please try again later.</p>';
    }
}
?>
