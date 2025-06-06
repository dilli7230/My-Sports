<!DOCTYPE html>
<html>
<head>
    <title>Register | My-Sports Online Store</title>
    <link rel="stylesheet" type="text/css" href="../static/style.css">
</head>
<body>
    <div class="container">
        <h2>Register</h2>
        <form action="/register" method="POST">
            <label>Username:</label>
            <input type="text" name="username" required>
            
            <label>Password:</label>
            <input type="password" name="password" required>
            
            <button type="submit">Register</button>
        </form>
    </div>
</html>
