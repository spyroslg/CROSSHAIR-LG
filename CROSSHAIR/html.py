Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
<!DOCTYPE html>
<html lang="el">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crosshair App</title>
    <style>
        /* Βασική μορφοποίηση για την οθόνη */
...         body {
...             margin: 0;
...             height: 100vh;
...             background-color: #f0f0f0;
...             display: flex;
...             justify-content: center;
...             align-items: center;
...             position: relative;
...             overflow: hidden;
...         }
... 
...         /* Στυλ για τον σταυρό */
...         .crosshair {
...             position: absolute;
...             width: 2px;
...             height: 100vh;
...             background-color: black;
...             left: 50%;
...             top: 0;
...             transform: translateX(-50%);
...         }
... 
...         .crosshair:after {
...             content: '';
...             position: absolute;
...             width: 100vh;
...             height: 2px;
...             background-color: black;
...             top: 50%;
...             left: 0;
...             transform: translateY(-50%);
...         }
...     </style>
... </head>
... <body>
...     <!-- Το crosshair θα είναι σε αυτήν την div -->
...     <div class="crosshair"></div>
... </body>
... </html>
