<?php
session_start();

//database conn params
$servername = "sql210.infinityfree.com";
$username = "if0_35906520";
$password = "kRllXLo8At";
$dbname = "if0_35906520_fedding";

// create conn
$conn = new mysqli($servername, $username, $password, $dbname);

// check conn
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["login-username"];
    $password = $_POST["login-password"];

    // hashed pw retreival from db
    $sql = "SELECT * FROM users WHERE username = '$username'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $hashedPassword = $row['password_hash'];

        // verify pw
        if (password_verify($password, $hashedPassword)) {
            // variables for success
            $_SESSION["loggedin"] = true;
            $_SESSION["username"] = $username;

            // new page
            header("Location: dashboard.php");
            exit();
        } else {
            // no pass
            echo "Invalid password.";
        }
    } else {
         // retards
        echo "User not found.";
    }
}

// clolse db
$conn->close();
?>
