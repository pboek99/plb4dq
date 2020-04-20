<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>New Account</title>
      <style>
        button{
            font-size:32px;
        }
    </style>
  </head>
  <body>
    <h1>Register</h1>
    <form action="/register" method="post">
      <div>
        <label for="username">Username</label>
        <input>
      </div>
      <div>
        <label for="password">Password</label>
        <input>
      </div>
      <button type="submit">Register</button><br>
         <a href = "/login">Login</a>
    </form>
   
  </body>
</html>
