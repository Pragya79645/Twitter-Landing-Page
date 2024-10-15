<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Join X - The New Twitter</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <!-- Header Section -->
    <header>
        <div class="container">
            <div class="logo">
                <h1>X</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#signup">Sign Up</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1>Connect, Share, and Engage on X</h1>
                <p>Join a global community where you can share your thoughts and connect with others instantly.</p>
                <a href="#signup" class="cta-btn">Join Now</a>
            </div>
            <div class="hero-image">
                <img src="https://via.placeholder.com/500x300" alt="X platform screenshot">
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features">
        <div class="container">
            <h2>Features</h2>
            <div class="features-grid">
                <div class="feature-item">
                    <h3>Instant Updates</h3>
                    <p>Stay updated with real-time notifications and trending topics that matter to you.</p>
                </div>
                <div class="feature-item">
                    <h3>Connect with Friends</h3>
                    <p>Follow friends, influencers, and discover new voices in your interests.</p>
                </div>
                <div class="feature-item">
                    <h3>Share Your Thoughts</h3>
                    <p>Post updates, photos, and videos, and express yourself with ease.</p>
                </div>
                <div class="feature-item">
                    <h3>Engage in Conversations</h3>
                    <p>Join discussions, reply to tweets, and engage with your community directly.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About X</h2>
            <p>X is a platform that empowers users to express themselves freely and connect with others globally. Join us to discover and share what matters most to you.</p>
        </div>
    </section>

    <!-- Sign Up Section -->
    <section id="signup" class="signup">
        <div class="container">
            <h2>Sign Up for X</h2>
            <form action="#">
                <input type="email" placeholder="Enter your email" required>
                <input type="password" placeholder="Create a password" required>
                <button type="submit">Get Started</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2024 X. All rights reserved.</p>
        </div>
    </footer>




<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    background-color: #f5f8fa;
    color: #14171a;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

header {
    background: #ffffff;
    padding: 10px 0;
    border-bottom: 1px solid #e1e8ed;
}

header .logo h1 {
    font-size: 32px;
    font-weight: 700;
}

nav ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
}

nav ul li {
    margin-left: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #1da1f2;
    font-weight: 700;
}

.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 50px 0;
}

.hero-content {
    flex: 1;
}

.hero-content h1 {
    font-size: 36px;
    margin-bottom: 20px;
}

.hero-content p {
    font-size: 18px;
    margin-bottom: 30px;
}

.cta-btn {
    background-color: #1da1f2;
    color: white;
    padding: 15px 25px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: 700;
}

.hero-image img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
}

.features {
    padding: 50px 0;
    background: #ffffff;
}

.features h2 {
    text-align: center;
    margin-bottom: 30px;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
}

.feature-item {
    background: #f5f8fa;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

.feature-item h3 {
    margin-bottom: 10px;
}

.about {
    padding: 50px 20px;
    background: #e1e8ed;
}

.about h2 {
    text-align: center;
    margin-bottom: 20px;
}

.signup {
    padding: 50px 20px;
}

.signup h2 {
    text-align: center;
    margin-bottom: 20px;
}

.signup form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.signup input {
    width: 300px;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.signup button {
    padding: 10px 20px;
    background-color: #1da1f2;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

footer {
    text-align: center;
    padding: 20px;
    background: #ffffff;
    border-top: 1px solid #e1e8ed;
}
</style>
</body>
</html>
